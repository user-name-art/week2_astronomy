import os
import telegram
from dotenv import load_dotenv


load_dotenv()

bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])

bot.send_message(text='Hello!', chat_id='@astronomy_tatarstan')
bot.send_document(chat_id='@astronomy_tatarstan', document=open('images/spacex0.jpg', 'rb'))
