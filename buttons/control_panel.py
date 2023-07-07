from typing import Optional
import disnake 
from disnake.ext import commands
import html
import sqlite3
import asyncio
import io
from time import time
from buttons.accept_button import AcceptTicketButton


class ControlPanel(disnake.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot

    @disnake.ui.button(label='Закрыть тикет', style=disnake.ButtonStyle.red)
    async def close_ticket(self, button, interaction: disnake.Interaction):
        with sqlite3.connect('ticket.db') as con:
            if interaction.user.id == interaction.author.id:
                cursor = con.cursor()
                row = cursor.execute("SELECT channel_id FROM ticket WHERE channel_id = ?", [interaction.channel_id]).fetchone()
                channel_id = interaction.channel_id
                channel = self.bot.get_channel(channel_id)
                if interaction.channel_id == row[0]:
                    cursor.execute("DELETE FROM ticket WHERE channel_id = ?",[interaction.channel_id])
                    con.commit()
                    timestamp = int(time() + 5)
                    await interaction.send(f'Спасибо за созданный тикет, он закроется <t:{timestamp}:R>',ephemeral=True)
                    await asyncio.sleep(5)
                    messages = await channel.history(limit=1000).flatten()
                    messages = reversed(messages)
                    page = (
                        f"""
                        <html>
                            <head>
                                <meta charset='UTF-8'>
                                <title>Сообщения из тикета {channel.name}</title>
                                <style>
                                    body {{
                                        background-color: #36393F;
                                        color: #DCDDDE;
                                        font-family: Whitney,Helvetica Neue,Helvetica,Arial,sans-serif;
                                        font-size: 16px;
                                    }}
                                    .avatar {{
                                        border-radius: 50%;
                                        width: 32px;
                                        height: 32px;
                                        margin-right: 10px;
                                    }}
                                    .chat {{
                                        margin: 0 auto;
                                        max-width: 800px;
                                    }}
                                    .message {{
                                        display: flex;
                                        margin-bottom: 10px;
                                    }}
                                    .message-content {{
                                        color: #DCDDDE;
                                        font-size: 16px;
                                        margin-bottom: 10px;
                                        background-color: #2F3136;
                                    }}
                                    .message-author {{
                                        display: flex;
                                        align-items: center;
                                        margin-bottom: 5px;
                                    }}
                                    .message-nickname {{
                                        color: #B9BBBE;
                                        font-size: 16px;
                                        font-weight: 700;
                                        margin-right: 5px;
                                    }}
                                    .message-date {{
                                        color: #B9BBBE;
                                        font-size: 12px;
                                        margin-left: auto;
                                    }}
                                    .embed {{
                                        display: flex;
                                        flex-direction: column;
                                        background-color: #2F3136;
                                        border-radius: 8px;
                                        padding: 10px;
                                        margin: 10px 50px;
                                    }}
                                    .embed-header {{
                                        color: #DCDDDE;
                                        font-size: 18px;
                                        font-weight: 700;
                                        margin-bottom: 5px;
                                    }}
                                    .embed-description {{
                                        color: #DCDDDE;
                                        font-size: 16px;
                                        margin-bottom: 10px;
                                    }}
                                    .embed-image {{
                                        border-radius: 8px;
                                        margin-top: 10px;
                                    }}
                                </style>
                            </head>
                            <body>
                            <h1 align="center">Сервер INTCODE</h1>
                            <h2 align="center">{channel.name}</h2>
                            """
                    )
                    for message in messages:
                        if message.embeds:
                            for embed in message.embeds:
                                page += (
                                    f"""
                                    <div class='chat'>
                                    <div class="embed">
                                        <img class='avatar' src='{message.author.avatar.url}'>
                                        <span class="message_author">{message.author}</span>
                                        <span class="message-date">{message.created_at}</span>
                                        <div class="embed-header">{embed.title}</div>
                                        <div class="embed-description">{embed.description}</div>
                                    </div>
                                    </div>
                                    """
                                )
                        else:
                            page += (
                                f"""
                                <div class='chat'>
                                <div class='embed'>
                                <img class='avatar' src='{message.author.avatar.url}'>
                                <span class="message_author">{message.author}</span>
                                <span class="message-date">{message.created_at}</span>
                                <div class="message-content">{message.content}</div>
                                </div>
                                </div>
                                """
                            )
                    page += (
                        '</body>\n</html>'
                    )
                    html_file = io.BytesIO(page.encode())
                    await self.bot.get_channel(1126954076123447317).send(file=disnake.File(fp=html_file, filename=f'ticket-{channel.name}.html'))

                    # Удаляем тикет
                    await channel.delete()

    @disnake.ui.button(label='Передать тикет', style=disnake.ButtonStyle.green)
    async def ticket_admin(self, button, interaction: disnake.Interaction):
        if interaction.user.id == interaction.author.id:
            channel = self.bot.get_channel(interaction.channel_id)
            await channel.set_permissions(target=interaction.author, send_messages=False, view_channel=True)
            await interaction.response.edit_message(view=AcceptTicketButton(self.bot), embed=disnake.Embed(
                title='Смена отвечающего',
                description='Подождите немного,вам скоро ответят',
                color=disnake.Color.from_rgb(106, 250, 227)
            ))


                