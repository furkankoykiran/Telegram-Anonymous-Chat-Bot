from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Enter your bot's token here
TOKEN = "6030402521:AAELW7sI4qGgPJeC6ExKWYtN1pk7d3LyljU"

# Enter the ID of the group you want to forward messages to here
GROUP_ID = -1001857468674

def echo(update, context):
    # Get user ID
    user_id = update.message.from_user.id
    
    # Receive the message and tag it with the user ID at the beginning
    message = f"@{update.message.from_user.username}: {update.message.text}"
    
    # Send message to group
    context.bot.send_message(chat_id=GROUP_ID, text=message)
    
    # Send response to user
    update.message.reply_text("🇺🇸 This message has been sent to the creator.\n\n🇹🇷 Bu mesaj kurucuya iletildi.")

def start(update, context):
    # Send response to user
    update.message.reply_text("🇺🇸 Hello! I am a bot that forwards your messages to the creator. Please leave a message.\n\n🇹🇷 Merhaba! Mesajlarınızı kurucuya ileten bir botum. Lütfen bir mesaj bırakın.")

def main():
    # Create your Telegram bot and get the dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Capture user messages
    echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dispatcher.add_handler(echo_handler)
    
    # Capture startup command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start the bot
    updater.start_polling()

    # Keep the bot running
    updater.idle()

main()