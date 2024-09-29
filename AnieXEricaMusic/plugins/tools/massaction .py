from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions, Message
from AnieXEricaMusic import app
from AnieXEricaMusic.misc import SUDOERS

def get_keyboard(command):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes", callback_data=f"{command}_yes"),
         InlineKeyboardButton("No", callback_data=f"{command}_no")]
    ])

@app.on_message(filters.command("banall"))
async def banall(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    
    if user_id != owner_id and user_id not in SUDOERS:
        await message.reply_text(f"Hey {message.from_user.mention}, 'banall' can only be executed by the group owner.")
        return
    confirm_msg = await message.reply(
        f"{message.from_user.mention}, are you sure you want to ban all group members?",
        reply_markup=get_keyboard("banall")
    )
@app.on_callback_query(filters.regex(r"^banall_(yes|no)$"))
async def handle_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await callback_query.answer("Only the group owner can confirm this action.", show_alert=True)
        return
    if callback_query.data == "banall_yes":
        await callback_query.message.edit("Banall process started...")
        bot = await app.get_chat_member(chat_id, app.me.id)
        if not bot.privileges.can_restrict_members:
            await callback_query.message.edit("I don't have permission to restrict members in this group.")
            return
        banned = 0
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator'] or member.user.id == app.me.id:
                continue 
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                banned += 1
            except Exception as e:
                print(f"Failed to ban {member.user.id}: {e}")
        await callback_query.message.edit(f"Banned {banned} members successfully.")
    elif callback_query.data == "banall_no":
        await callback_query.message.edit("Banall process canceled.")


@app.on_message(filters.command("unbanall"))
async def unbanall(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await message.reply_text(f"Hey {message.from_user.mention}, 'unbanall' can only be executed by the group owner.")
        return
    confirm_msg = await message.reply(
        f"{message.from_user.mention}, are you sure you want to unban all group members?",
        reply_markup=get_keyboard("unbanall")
    )

@app.on_callback_query(filters.regex(r"^unbanall_(yes|no)$"))
async def handle_unbanall_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await callback_query.answer("Only the group owner can confirm this action.", show_alert=True)
        return
    if callback_query.data == "unbanall_yes":
        await callback_query.message.edit("Unbanall process started...")
        bot = await app.get_chat_member(chat_id, app.me.id)
        if not bot.privileges.can_unban_members:
            await callback_query.message.edit("I don't have permission to unban members in this group.")
            return
        unbanned = 0
        async for member in app.get_chat_banned_members(chat_id):
            try:
                await app.unban_chat_member(chat_id, member.user.id)
                unbanned += 1
            except Exception as e:
                print(f"Failed to unban {member.user.id}: {e}")
        await callback_query.message.edit(f"Unbanned {unbanned} members successfully.")
    elif callback_query.data == "unbanall_no":
        await callback_query.message.edit("Unbanall process canceled.")


@app.on_message(filters.command("unmuteall"))
async def unmuteall(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await message.reply_text(f"Hey {message.from_user.mention}, 'unmuteall' can only be executed by the group owner.")
        return
    
    confirm_msg = await message.reply(
        f"{message.from_user.mention}, are you sure you want to unmute all group members?",
        reply_markup=get_keyboard("unmuteall")
    )

@app.on_callback_query(filters.regex(r"^unmuteall_(yes|no)$"))
async def handle_unmuteall_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await callback_query.answer("Only the group owner can confirm this action.", show_alert=True)
        return
    if callback_query.data == "unmuteall_yes":
        await callback_query.message.edit("Unmuteall process started...")
        bot = await app.get_chat_member(chat_id, app.me.id)
        if not bot.privileges.can_restrict_members:
            await callback_query.message.edit("I don't have permission to restrict members in this group.")
            return
        unmuted = 0
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator']:
                continue 
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=True))
                unmuted += 1
            except Exception as e:
                print(f"Failed to unmute {member.user.id}: {e}")
        await callback_query.message.edit(f"Unmuted {unmuted} members successfully.")
    elif callback_query.data == "unmuteall_no":
        await callback_query.message.edit("Unmuteall process canceled.")


@app.on_message(filters.command("muteall"))
async def muteall(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await message.reply_text(f"Hey {message.from_user.mention}, 'muteall' can only be executed by the group owner.")
        return
    confirm_msg = await message.reply(
        f"{message.from_user.mention}, are you sure you want to mute all group members?",
        reply_markup=get_keyboard("muteall")
    )
@app.on_callback_query(filters.regex(r"^muteall_(yes|no)$"))
async def handle_muteall_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
    if user_id != owner_id and user_id not in SUDOERS:
        await callback_query.answer("Only the group owner can confirm this action.", show_alert=True)
        return
    if callback_query.data == "muteall_yes":
        await callback_query.message.edit("Muteall process started...")
        bot = await app.get_chat_member(chat_id, app.me.id)
        if not bot.privileges.can_restrict_members:
            await callback_query.message.edit("I don't have permission to restrict members in this group.")
            return
        muted = 0
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator']:
                continue 
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=False))
                muted += 1
            except Exception as e:
                print(f"Failed to mute {member.user.id}: {e}")
        await callback_query.message.edit(f"Muted {muted} members successfully.")
    elif callback_query.data == "muteall_no":
        await callback_query.message.edit("Muteall process canceled.")
