from config.config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters
    )
from handlers import start
from handlers.function import echo_uz
from handlers.register import start_registr,get_name,get_contact,get_location
from handlers.elements import NAME,CONTACT,LOCATION
from handlers.cancel import cancel


def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    #Comand handler
    dispatcher.add_handler(CommandHandler('start',start))
    
    #MessageHandler
    dispatcher.add_handler(MessageHandler(Filters.text("Uzbek"),echo_uz))
    # dispatcher.add_handler(MessageHandler(Filters.text("Registratsiya"),registratsiya))
    
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("^(Registratsiya|Registration)$"),start_registr)],
        states={
           NAME:[MessageHandler(Filters.text,get_name)],
           CONTACT:[MessageHandler(Filters.contact,get_contact)],
           LOCATION:[MessageHandler(Filters.location,get_location)]
        },
         fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()