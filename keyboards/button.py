from telegram import ReplyKeyboardMarkup,KeyboardButton


def get_language_keyboard():
    
    keyboard =   [
                   [
                    KeyboardButton("Uzbek"),
                    KeyboardButton("English")
                    ]
                ]
    
    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

def get_register_menu():
    
    keyboard = [
        [
            KeyboardButton("Menu"),KeyboardButton("Registratsiya")
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True,one_time_keyboard=True)

def get_contact_button():
    
    keyboard = [
        [
            KeyboardButton("Contact",request_contact=True)
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True,one_time_keyboard=True)

def get_location_button():
    
    keyboard = [
        [
            KeyboardButton("Location",request_location=True)
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True,one_time_keyboard=True)
