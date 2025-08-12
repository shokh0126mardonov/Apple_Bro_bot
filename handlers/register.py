from telegram import Update
from telegram.ext import CallbackContext,ConversationHandler
from .elements import NAME,LOCATION,CONTACT
from keyboards.button import get_location_button,get_contact_button


#get_name,get_contact,get_location
def start_registr(update: Update,context: CallbackContext):
    
    update.message.reply_text("Registratsiya uchun ushbu malumotlaringizni yuboring")
    update.message.reply_text("Ismingizni yuboring")
    
    return NAME
    
def get_name(update: Update,context: CallbackContext):
    context.user_data["name"] = update.message.text
    
    update.message.reply_text("Ismingiz qabul qilindi")
    update.message.reply_text("Contact yuboring",reply_markup = get_contact_button())
    
    return CONTACT

def get_contact(update: Update,context: CallbackContext):
    context.user_data["contact"] = update.message.contact.phone_number
    
    update.message.reply_text("Contact qabul qilindi")
    update.message.reply_text("Locatsiya yuboring",reply_markup=get_location_button())
    
    return LOCATION

def get_location(update: Update,context: CallbackContext):
    
    location = {
        "latitude":update.message.location.latitude,
        "longitude":update.message.location.longitude
        }
    context.user_data["location"] = location
    print(context.user_data)
    update.message.reply_text("Locatsiya qabul qilindi")
    update.message.reply_text("Siz registratsiya qilindingiz")
    
    return ConversationHandler.END