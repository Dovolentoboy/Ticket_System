import disnake 
from disnake.ext import commands
from buttons.create_ticket import CreateTicketButton

class TicketCog(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        print('Тикеты готовы')
    

    @commands.command(name='ticket_public')
    async def ticket_public(self,ctx):
        embed = disnake.Embed(
            title='Связь с персоналом',
            description='Чтобы связаться с персоналом нажмите на кнопку ниже\n**Рофлотикеты наказуемы**',
            color=disnake.Color.from_rgb(101, 201, 180)
        )
        view = CreateTicketButton(bot=self.bot)
        await ctx.send(embed=embed,view=view)


    @commands.Cog.listener()
    async def on_ready(self):
        channel = await self.bot.fetch_channel(1126618053581484032)
        message = await channel.fetch_message(1126966106041634968)
        embed = disnake.Embed(
            title='Связь с персоналом',
            description='Чтобы связаться с персоналом нажмите на кнопку ниже\n**Рофлотикеты наказуемы**',
            color=disnake.Color.from_rgb(101, 201, 180)
        )
        await message.edit(view=CreateTicketButton(self.bot),embed=embed)
        print('Всё готово,сообщение отредактировано')


def setup(bot):
    bot.add_cog(TicketCog(bot))
