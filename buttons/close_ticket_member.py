from typing import Optional
import disnake 
from disnake.ext import commands
import sqlite3
import asyncio
from time import time


class CloseTicketButton(disnake.ui.View):
    def __init__(self,bot:commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot


    @disnake.ui.button(label='Закрыть тикет',style=disnake.ButtonStyle.red)
    async def close_ticket(self,button,interaction:disnake.Interaction):
        with sqlite3.connect('ticket.db') as con:
            cursor = con.cursor()
            row = cursor.execute("SELECT user_id,channel_id,status,message_id FROM ticket WHERE user_id = ?",[interaction.user.id]).fetchone()

            if row[0] not in [interaction.user.id,516221569614479379]:
                await interaction.send('Это не ваша кнопка')
            else:
                channel = self.bot.get_channel(row[1])
                timestamp = int(time() + 5)
                await interaction.send(f'Спасибо за созданный тикет, он закроется <t:{timestamp}:R>',ephemeral=True)
                await asyncio.sleep(5)
                await channel.delete(reason='Закрытие канала')
                cursor.execute("DELETE FROM ticket WHERE user_id = ?",[interaction.user.id])
                con.commit()
    
    
