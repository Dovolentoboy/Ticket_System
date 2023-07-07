import disnake
from disnake.ext import commands
from static_function import check_role_function



class HSButtons(disnake.ui.View):
    def __init__(self, bot, user, author):
        super().__init__(timeout=None)
        self.bot = bot
        self.user = user
        self.author = author
        self.guild = self.bot.get_guild(964552339845431307)
        self.member = self.guild.get_member(self.user)

    @disnake.ui.button(label='Модератор', style=disnake.ButtonStyle.primary)
    async def mod(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            view = ModStaffSelect(bot=self.bot, user=self.user, author=self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Менеджер', style=disnake.ButtonStyle.danger)
    async def pm(self, button, interaction):
        if interaction.user != self.author:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            view = PMStaffSelect(bot=self.bot, user=self.user, author=self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Кодер', style=disnake.ButtonStyle.success)
    async def code(self, button, interaction):
        if interaction.user != self.author:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            view = CodeStaffSelect(bot=self.bot, user=self.user, author=self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Закрыть', style=disnake.ButtonStyle.secondary, emoji='❌', row=1)
    async def close(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Управление персоналом',
                description=f'Вы закрыли управление пользователем - **{self.member.name}**'
            )
            embed.set_footer(
                text=f'Модератор: {interaction.author.name}'
            )
            msg = await interaction.message.edit(embed=embed, view=None)
            await msg.delete(delay=20)

class CodeStaffSelect(disnake.ui.View):
    def __init__(self, user, bot: commands.Bot, author):
        super().__init__(timeout=None)
        self.bot = bot
        self.user = user
        self.author = author
        self.guild = self.bot.get_guild(964552339845431307)
        self.member = self.guild.get_member(self.user)
        self.code = self.guild.get_role(1126530371870265355)
        self.senior_code = self.guild.get_role(1126530382930640998)

        mod = [
            disnake.SelectOption(
                label=('Назначить на роль Coder' if self.code not in self.member.roles else 'Снять с роли Coder'),
                description=('Выдает роль Coder' if self.code not in self.member.roles else 'Снимает Coder'),
                value='c1'
            ),
            disnake.SelectOption(
                label=(
                    'Назначить на роль Senior Coder' if self.senior_code not in self.member.roles else
                    'Снять с роли Senior Coder'),
                description='Выдает роль Senior Coder',
                value='c2'
            )
        ]

        self.select = disnake.ui.Select(placeholder='Выберите действие', options=mod)
        self.add_item(self.select)
        self.select.callback = self.callback

    async def callback(self, interaction: disnake.Interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            selected_value = self.select.values[0]
            if selected_value == 'c1':
                await check_role_function(interaction=interaction, role=self.code, member=self.member, post='Coder',
                                          view=CodeStaffSelect(bot=self.bot, user=self.user, author=self.author))
            elif selected_value == 'c2':
                await check_role_function(interaction=interaction, role=self.senior_code, member=self.member,
                                          post='Senior Coder',
                                          view=CodeStaffSelect(bot=self.bot, user=self.user, author=self.author))


    @disnake.ui.button(label='Назад', emoji='⬅️', row=1)
    async def back(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Взаимодействие с пользователем',
                description=f'Пользователь - {self.member.name}'
            )
            embed.set_thumbnail(
                url=self.member.avatar.url
            )
            embed.set_footer(
                text=f'Модератор - {interaction.author.name}',
                icon_url=interaction.author.avatar.url
            )

            view = HSButtons(self.bot, self.user, self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Закрыть', style=disnake.ButtonStyle.secondary, emoji='❌', row=1)
    async def close(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Управление персоналом',
                description=f'Вы закрыли управление пользователем - **{self.member.name}**'
            )
            embed.set_footer(
                text=f'Модератор: {interaction.author.name}'
            )
            msg = await interaction.message.edit(embed=embed, view=None)
            await msg.delete(delay=20)


class ModStaffSelect(disnake.ui.View):
    def __init__(self, user, bot: commands.Bot, author):
        super().__init__()
        self.author = author
        self.bot = bot
        self.user = user
        self.guild = self.bot.get_guild(964552339845431307)
        self.mod = self.guild.get_role(1080080370688606219)
        self.senior_mod = self.guild.get_role(1113738297529868298)
        self.member = self.guild.get_member(self.user)

        coder = [
            disnake.SelectOption(
                label=('Назначить на Модератора' if self.mod not in self.member.roles else 'Снять с модератора'),
                description='Выдает роль модератора',
                value='m1'
            ),
            disnake.SelectOption(
                label=('Назначить на Куратора модерации' if self.senior_mod else 'Снять с куратора модерации'),
                description='Выдает роль Куратора',
                value='m2'
            )
        ]

        self.select = disnake.ui.Select(placeholder='Выберите действие', options=coder)
        self.add_item(self.select)
        self.select.callback = self.callback

    async def callback(self, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            selected_values = self.select.values[0]
            if selected_values == 'm1':
                await check_role_function(interaction=interaction, role=self.mod, member=self.member, post='Модератора',
                                          view=ModStaffSelect(self.user, self.bot, self.author))
            elif selected_values == 'm2':
                await check_role_function(interaction=interaction, role=self.senior_mod, member=self.member,
                                          post='Куратора модерации',
                                          view=ModStaffSelect(self.user, self.bot, self.author))

    @disnake.ui.button(label='Назад', emoji='⬅️', row=1)
    async def back(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Взаимодействие с пользователем',
                description=f'Пользователь - {self.member.name}'
            )
            embed.set_thumbnail(
                url=self.member.avatar.url
            )
            embed.set_footer(
                text=f'Модератор - {interaction.author.name}',
                icon_url=interaction.author.avatar.url
            )

            view = HSButtons(self.bot, self.user, self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Закрыть', style=disnake.ButtonStyle.secondary, emoji='❌', row=1)
    async def close(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Управление персоналом',
                description=f'Вы закрыли управление пользователем - **{self.member.name}**'
            )
            embed.set_footer(
                text=f'Модератор: {interaction.author.name}'
            )
            msg = await interaction.message.edit(embed=embed, view=None)
            await msg.delete(delay=20)

class PMStaffSelect(disnake.ui.View):
    def __init__(self, user, bot: commands.Bot, author):
        super().__init__(timeout=None)
        self.author = author
        self.bot = bot
        self.user = user
        self.guild = self.bot.get_guild(964552339845431307)
        self.pm = self.guild.get_role(1113738289019621407)
        self.senior_pm = self.guild.get_role(1113738290428915762)
        self.member = self.guild.get_member(self.user)

        pm = [
            disnake.SelectOption(
                label='Назначить на Пиар-Менеджера' if self.pm not in self.member.roles else 'Снять с пиар менеджера',
                description='Выдает роль пиар-менеджера',
                value='p1'
            ),
            disnake.SelectOption(
                label='Назначить на Руководителя Пиар Отделом' if self.pm not in self.member.roles else
                'Снять с Руководителя Пиар Отделом',
                description='Выдает роль РПО',
                value='p2'
            )
        ]

        self.select = disnake.ui.Select(placeholder='Выберите действие', options=pm)
        self.add_item(self.select)
        self.select.callback = self.callback

    async def callback(self, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            selected_values = self.select.values[0]
            if selected_values == 'p1':
                await check_role_function(interaction=interaction, role=self.pm, member=self.member,
                                          post='Пиар менеджера',
                                          view=PMStaffSelect(bot=self.bot, user=self.user, author=self.author))
            elif selected_values == 'p2':
                await check_role_function(interaction=interaction, role=self.senior_pm, member=self.member,
                                          post='Руководителя пиар отдела',
                                          view=PMStaffSelect(bot=self.bot, user=self.user, author=self.author))

    @disnake.ui.button(label='Назад', emoji='⬅️', row=1)
    async def back(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Взаимодействие с пользователем',
                description=f'Пользователь - {self.member.name}'
            )
            embed.set_thumbnail(
                url=self.member.avatar.url
            )
            embed.set_footer(
                text=f'Модератор - {interaction.author.name}',
                icon_url=interaction.author.avatar.url
            )

            view = HSButtons(self.bot, self.user, self.author)
            await interaction.response.edit_message(view=view)

    @disnake.ui.button(label='Закрыть', style=disnake.ButtonStyle.secondary, emoji='❌', row=1)
    async def close(self, button, interaction):
        if interaction.user.id not in [self.author.id,994275496298827868]:
            await interaction.response.send_message('Это не ваша кнопка', ephemeral=True)
        else:
            embed = disnake.Embed(
                title='Управление персоналом',
                description=f'Вы закрыли управление пользователем - **{self.member.name}**'
            )
            embed.set_footer(
                text=f'Модератор: {interaction.author.name}'
            )
            msg = await interaction.message.edit(embed=embed, view=None)
            await msg.delete(delay=20)