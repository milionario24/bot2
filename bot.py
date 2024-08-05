from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Configuração do logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

# Substitua pelo seu token do bot
TOKEN = "6373715280:AAF3w1GTFQSn3zBH90GHv-tM0sEjX6I02o8"

# Lista de produtos, preços e informações
PRODUCTS = {
    "SNAPGOD FOLDER": {
        "name": "SNAPGOD FOLDER",
        "price": 60.00,
        "file_id": "BAACAgQAAxkBAANVZq807EAwYmYa-tGhPH85jjIre5wAAmUZAAJ7mSlRh8zU7ftvZAg1BA",
        "description":"‼️SNAPGOD FOLDER📁\n\n✅ OVER 60000 VIDEOS\n✅ 500GB IN TOTAL\n✅ MORE THAN 200 BLACKMAIL VIDEOS\n✅ LEAKED SNAP OF REAL GIRLS\n✅ MY COMPLETE FOLDER\n\n⚠️don’t waste my time⚠️ "
    },
    "TOP TIER": {
        "name": "TOP TIER",
        "price": 25.00,
        "file_id": "BAACAgQAAxkBAANbZq81TKgwKtz3K8W2tGKBX138UJoAAjwSAAI9wGFTIDpL14SToew1BA",
        "description": "‼️TOP TIER NEW FOLDER AVAILABLE (again) ‼️\n✅biggest folder so far\n✅more than 1200 videos\n✅omegle game\n✅monkey app\n✅hot teens on omgle"
    },
    "MONKEY APP": {
        "name": "MONKEY APP",
        "price": 20.00,
        "file_id": "BAACAgQAAxkBAANZZq81OQfVJOJLbYamMt_hKi-8pjUAAgsWAAIPy9lQP5X5YzOybaI1BA",
        "description": "‼️MONKEY APP WINS (FOLDER)⚠️\n\n✅ABOUT 500 girls\n✅MY BEST MONKEY APP FOLDER"
    },
    "ANXIOUS PANDA": {
        "name": "ANXIOUS PANDA",
        "price": 25.00,
        "file_id": "BAACAgQAAxkBAANXZq81GbHMfCmWtZ9aMsmdyM_uxBYAAlYTAAJx5MhQ7xODsKqGYZE1BA",
        "description": "⚠️THE FULL VIDEO OVER 4 HOURS 🔞 GAME‼️\n\n‼️ANXIOUS PANDA FOLDER‼️\n‼️the most searched folder‼️\n\n✅OMEGLE GAME\n✅SPANISH GIRLS\n✅OVER 100GB"
    },
    "vip_group": {
        "name": "VIP GROUP",
        "price": 20.00,
        "file_id": "BAACAgQAAxkBAANdZq81XyAJj9c8cdBk5WjGK8PQg5AAAsUWAAL-4RBRcVup6i0im_81BA",
        "description": "‼️THE FULL VIDEO IS TWO HOURS LONG‼️\n\nYou can have it\n+\nVip Access for\n+\nMy mega folder"
    }
}

# Dicionário para armazenar informações de usuários
user_data = {}

async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id

    if user_id in user_data:
        greeting = f"Welcome back, {user.first_name}!"
    else:
        greeting = f"Welcome {user.first_name}, This bot will help you buy leaked content from folders such as (omegle, snapgod, anxious panda, black mail, monkey app as well as our vip group), choose the content you want below."
        user_data[user_id] = {"first_interaction": True}

    keyboard = [
        [
            InlineKeyboardButton("SNAPGOD FOLDER", callback_data='SNAPGOD FOLDER'),
            InlineKeyboardButton("TOP TIER", callback_data='TOP TIER'),
        ],
        [
            InlineKeyboardButton("MONKEY APP", callback_data='MONKEY APP'),
            InlineKeyboardButton("ANXIOUS PANDA", callback_data='ANXIOUS PANDA'),
        ],
        [
            InlineKeyboardButton("VIP GROUP", callback_data='vip_group'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(greeting, reply_markup=reply_markup)

async def menu(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    greeting = f"Welcome back, {user.first_name}!"

    keyboard = [
        [
            InlineKeyboardButton("SNAPGOD FOLDER", callback_data='SNAPGOD FOLDER'),
            InlineKeyboardButton("TOP TIER", callback_data='TOP TIER'),
        ],
        [
            InlineKeyboardButton("MONKEY APP", callback_data='MONKEY APP'),
            InlineKeyboardButton("ANXIOUS PANDA", callback_data='ANXIOUS PANDA'),
        ],
        [
            InlineKeyboardButton("VIP GROUP", callback_data='vip_group'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(greeting, reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    product = query.data
    user = query.from_user

    logging.info(f"Callback received: {product}")

    if product in PRODUCTS:
        item = PRODUCTS[product]
        keyboard = [
            [
                InlineKeyboardButton("Buy", callback_data=f'buy_{product}'),
                InlineKeyboardButton("Back to Menu", callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_video(
            video=item['file_id'],
            caption=f"{item['name']}\n\n{item['description']}\nPrice: ${item['price']:.2f}",
            reply_markup=reply_markup
        )
    elif product.startswith('buy_'):
        _, prod = product.split('_', 1)
        if prod in PRODUCTS:
            item = PRODUCTS[prod]
            # Apagar a mensagem antiga
            await query.message.delete()
            # Enviar novos detalhes com opções de suporte
            await query.message.reply_text(
                f"You chose to buy: {item['name']}.\nPrice: ${item['price']:.2f}\n\n"
                f"Please send the payment to PayPal using the email: clesiolucas7@gmail.com\n"
                f"If you need another payment method, contact support.\n"
                f"After payment, please send the proof to support:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Support", url="https:https://t.me/cleyadmin")],
                    [InlineKeyboardButton("Back to Menu", callback_data='back')]
                ])
            )
    elif product == 'back':
        # Enviar uma nova mensagem com o menu principal
        greeting = f"Welcome back, {user.first_name}!"
        keyboard = [
            [
                InlineKeyboardButton("SNAPGOD FOLDER", callback_data='SNAPGOD FOLDER'),
                InlineKeyboardButton("TOP TIER", callback_data='TOP TIER'),
            ],
            [
                InlineKeyboardButton("MONKEY APP", callback_data='MONKEY APP'),
                InlineKeyboardButton("ANXIOUS PANDA", callback_data='ANXIOUS PANDA'),
            ],
            [
                InlineKeyboardButton("VIP GROUP", callback_data='vip_group'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Enviar uma nova mensagem com o menu principal
        await query.message.reply_text(greeting, reply_markup=reply_markup)

    # Responder ao callback com uma confirmação
    await query.answer()

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
