import sqlite3
import disnake
from disnake.ext import commands
from buttons.control_panel import ControlPanel

class TicketСontrol(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Тикет контрол')

    role_ids = [1113738297529868298, 1080080370688606219, 1118053740738510918, 1080080316884074496, 1114114078118510632,  # жалобы
                1118053740738510918, 1080080316884074496, 1126529399454441553,  # идеи
                1113738297529868298, 1080080370688606219, 1118053740738510918, 1080080316884074496,  # вопросы
                1118053740738510918, 1080080316884074496, 1126529399454441553, 1113738289019621407,
                1113738290428915762,  # партнёрки
                1118053740738510918, 1126529399454441553, 1126530371870265355, 1126530382930640998,  # Проверка и помощь в коде
                1118053740738510918, 1126529399454441553  # услуги сервера (Шоп ночная бабочка Марина)
                ]
    roles = [disnake.Object(id) for id in role_ids]

    @commands.command(name='ticket-control')
    async def ticket_control(self, interaction: disnake.Interaction):
        member_roles = [role.id for role in interaction.author.roles]
        if any(role_id in member_roles for role_id in self.role_ids):
            with sqlite3.connect('ticket.db') as con:
                cursor = con.cursor()
                channel = self.bot.get_channel(interaction.channel.id)
                channel_check = cursor.execute("SELECT channel_id FROM ticket WHERE channel_id = ?", [channel.id]).fetchone()
                if channel_check is not None:
                    await channel.send(embed=disnake.Embed(
                        title='Система управления тикетом',
                        description='Выберите действие',
                        color=disnake.Color.from_rgb(106, 250, 227)
                    ), view=ControlPanel(self.bot))


def setup(bot):
    bot.add_cog(TicketСontrol(bot))

            