import disnake 
from disnake.ext import commands
import sqlite3
from disnake.interactions import MessageInteraction
from modals.ticket_mod_modal import TicketModModal
from modals.ticket_idea_modal import TicketIdeaModal
from modals.ticket_partner_modal import TicketPartnerModal
from modals.ticket_question_modal import TicketQuestionModal
from modals.ticket_code_helper_modal import TicketCodeModal
from modals.ticket_shop_modal import TicketShopModal



class ChooseThemeTicket(disnake.ui.View):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        super().__init__(timeout=None)
        options = [
            disnake.SelectOption(label='Жалоба на пользователя',value='Жалоба на пользователя',emoji='🛡'),
            disnake.SelectOption(label='Ваши идеи',value='Идеи',emoji='🧩'),
            disnake.SelectOption(label='Заключения партнёрства',value='Партнёрка',emoji='🤝'),
            disnake.SelectOption(label='Заказать услугу',value='Заказ услуг',emoji='🎟'),
            disnake.SelectOption(label='Вопрос',value='Вопрос',emoji='❓'),
            disnake.SelectOption(label='Помощь по коду',value='Помощь по коду',emoji='👩‍💻')
        ]
        self.select = disnake.ui.Select(placeholder='Выберите тему тикета',options=options,custom_id='choose_option')
        self.add_item(self.select)
        self.select.callback = self.callback

    async def callback(self, interaction: MessageInteraction):
        with sqlite3.connect('ticket.db') as con:
            cursor = con.cursor()
            row = cursor.execute("SELECT user_id,channel_id,message_id FROM ticket WHERE user_id = ?",[interaction.user.id]).fetchone()
            selected_values = self.select.values[0]
            if selected_values == 'Жалоба на пользователя':
                await interaction.response.send_modal(TicketModModal(self.bot))
            elif selected_values == 'Идеи':
                await interaction.response.send_modal(TicketIdeaModal(self.bot))
            elif selected_values == 'Партнёрка':
                await interaction.response.send_modal(TicketPartnerModal(self.bot))
            elif selected_values == 'Заказ услуг':
                await interaction.response.send_modal(TicketShopModal(self.bot))
            elif selected_values == 'Вопрос':
                await interaction.response.send_modal(TicketQuestionModal(self.bot))
            elif selected_values == 'Помощь по коду':
                await interaction.response.send_modal(TicketCodeModal(self.bot))

    