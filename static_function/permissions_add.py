import disnake
from buttons.accept_button import AcceptTicketButton


async def permissions_move(roles, channel, embed, message_delete_ticket, message_theme_choose, member, bot, interaction: disnake.Interaction):
    for role_id in roles:
        role = interaction.guild.get_role(role_id)
        await channel.set_permissions(target=role, overwrite=disnake.PermissionOverwrite(view_channel=True, send_messages=False))
    await channel.set_permissions(target=member, overwrite=disnake.PermissionOverwrite(view_channel=True, send_messages=True))
    
    # Используем первую роль из списка для упоминания в сообщении
    role_to_mention = interaction.guild.get_role(roles[0])
    await channel.send(content=f'{role_to_mention.mention}', embed=embed, view=AcceptTicketButton(bot=bot))
    await message_delete_ticket.edit(view=None)
    await message_theme_choose.edit(view=None)
