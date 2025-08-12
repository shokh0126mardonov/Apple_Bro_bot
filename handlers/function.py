from telegram import Update
from telegram.ext import CallbackContext
from keyboards import get_register_menu

def echo_uz(update:Update,context: CallbackContext):
    
    update.message.reply_text(
        text="Siz o'zbek tilini tanladingiz!",
        reply_markup = get_register_menu()
    )