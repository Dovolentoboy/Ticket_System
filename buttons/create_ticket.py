import disnake 
from disnake.ext import commands
import sqlite3
from buttons.close_ticket_member import CloseTicketButton
from buttons.theme_dropdown import ChooseThemeTicket
from datetime import datetime


class CreateTicketButton(disnake.ui.View):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        super().__init__(timeout=None)
        with sqlite3.connect('ticket.db') as con:
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS ticket (
                   user_id INTEGER,
                   status INTEGER,
                   channel_id INTEGER,
                   message_id INTEGER,
                   theme_message INTEGER
                   )""")
            con.commit()


    @disnake.ui.button(label='Создать тикет',style=disnake.ButtonStyle.green)
    async def create_ticket_button(self,button,interaction:disnake.Interaction):
        with sqlite3.connect('ticket.db') as con:
            cursor = con.cursor()
            row = cursor.execute("SELECT user_id,status,channel_id FROM ticket WHERE user_id=?",[interaction.user.id]).fetchone()
            if row is not None:
                await interaction.send(f'Ваш тикет уже создан и ожидает вас в <#{row[2]}>',ephemeral=True)
            else:
                await interaction.response.defer()
              

                category = await self.bot.fetch_channel(1079492916826882180)
                channel = await interaction.guild.create_text_channel(category=category, name=f'ticket-{interaction.user}')


                await channel.set_permissions(target=interaction.guild.default_role, view_channel=False)
                await channel.set_permissions(target=interaction.user, view_channel=True, send_messages=False)

                await interaction.send(f'Ваш тикет в канале {channel.mention}',ephemeral=True)

                warning_message = disnake.Embed(
                    title='ВНИМАНИЕ!',
                    description='Итак,вы в канале тикета. Надеюсь,что вы полностью осознаете свои действия и готовы продолжить дальше\n'
                                'Если тикет был создан по ошибке,то нажмите на кнопку ниже ,дабы не создавать проблем нашей администрации',
                    timestamp=datetime.now(),
                    color=disnake.Color.from_rgb(106, 250, 227)
                    
                )
                choose_theme_ticket = disnake.Embed(
                    title='Выберите тему тикета',
                    description='Надеюсь,что после прочтения предыдущего сообщения вы готовы продолжить. \nПри помощи меню ниже пожалуйста выберите тему вашего обращения\n Это поможет нашему персоналу легче помочь вам\n',
                    timestamp=datetime.now(),
                    color=disnake.Color.from_rgb(106, 250, 227)
                )

                delete_message = await channel.send(embed=warning_message,view=CloseTicketButton(self.bot))
                message = await channel.send(embed=choose_theme_ticket,view=ChooseThemeTicket(self.bot))
                message_id = message.id
                cursor.execute("INSERT INTO ticket(user_id, status, channel_id,message_id,theme_message) VALUES (?,?,?,?,?)", [interaction.user.id, 1, channel.id,delete_message.id,message_id])
                con.commit()
