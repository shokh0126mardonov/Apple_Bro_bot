from telegram import Update
from telegram.ext import CallbackContext
from keyboards import get_language_keyboard

def start(update:Update,context:CallbackContext):
    name = update.effective_user.full_name
    
    update.message.reply_text(text=f"Assalomu alekum {name}")
    
    update.message.reply_text(
        text = "Tilni tanlang/Select language",
        reply_markup = get_language_keyboard()
    )