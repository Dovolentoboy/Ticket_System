from typing import Optional
import disnake
from disnake.ext import commands


class AcceptTicketButton(disnake.ui.View):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        super().__init__(timeout=None)
    
    @disnake.ui.button(label='Принять тикет', style=disnake.ButtonStyle.green)
    async def accept_ticket(self, button, interaction: disnake.Interaction):
        role_ids = [1113738297529868298, 1080080370688606219, 1118053740738510918, 1080080316884074496,1114114078118510632, #жалобы
                    1118053740738510918, 1080080316884074496, 1126529399454441553, #идеи
                    1113738297529868298, 1080080370688606219, 1118053740738510918, 1080080316884074496, #вопросы
                    1118053740738510918, 1080080316884074496, 1126529399454441553, 1113738289019621407, 1113738290428915762, #партнёрки
                    1118053740738510918, 1126529399454441553, 1126530371870265355, 1126530382930640998, #Проверка и помощь в коде
                    1118053740738510918, 1126529399454441553 #услуги сервера (Шоп ночная бабочка Марина)
                    ]
        roles = [interaction.guild.get_role(role_id) for role_id in role_ids]
        if any(role in interaction.user.roles for role in roles):
            channel = self.bot.get_channel(interaction.channel_id)
            await channel.set_permissions(target=interaction.user,send_messages=True)
            await interaction.response.edit_message(view=None)
            await interaction.send(
                embed=disnake.Embed(
                    title='Найден отвечающий',
                    description=f'Отвечающий {interaction.user.mention}'
                )
            )

    

