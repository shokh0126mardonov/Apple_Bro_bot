from telegram import Update,ReplyKeyboardMarkup,KeyboardButton



def register_menu_keyboard():
    keyboard = [
        [KeyboardButton("Menu"),KeyboardButton("Registratsiya")]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,one_time_keyboard=True,resize_keyboard=True
    )