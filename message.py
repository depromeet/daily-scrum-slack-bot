import slacker
from datetime import datetime

def send_message(msg, error = ''):
    send_msg = msg
    if error:
        send_msg = '🚨 Error 🚨 \n ' + str(error)

    today = datetime.now().strftime('$Y-%m-%d')
    slacker.Chat.post_message(channel = '00-1조-디프만-1번출구-데일리스크럼',text = today + send_msg, as_user = True)