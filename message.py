import json
import requests
from datetime import datetime


def send_message(send_msg, channel_name):
    TOKEN = json.loads(open('secret_key.json').read())["SLACK_NOTIFY"]["BOT_USER_OAUTH_TOKEN"]
    URL = "https://slack.com/api/chat.postMessage"

    try:
        response = requests.post(URL,
                                 headers={"Authorization": "Bearer " + TOKEN},
                                 data={"channel": channel_name, "text": send_msg}
                                 )
    except Exception as e:
        send_msg = '๐จ Error ๐จ \n ' + str(e)
        response = requests.post(URL,
                                 headers={"Authorization": "Bearer " + TOKEN},
                                 data={"channel": channel_name, "text": send_msg}
                                 )
    print(response)


if __name__ == '__main__':
    today = datetime.now().strftime('%Y-%m-%d')
    channel_name = "#00-1์กฐ-๋ํ๋ง-1๋ฒ์ถ๊ตฌ-๋ฐ์ผ๋ฆฌ์คํฌ๋ผ"
    message = f' ๐ข {today} ๋ฐ์ผ๋ฆฌ ์คํฌ๋ผ ์๊ฐ์๋๋ค. ๐ข \n' \
              "์ค๋ ํ  ์ผ\n" \
              "highest\n" \
              "- ํ ์ผ \n" \
              "- ํ ์ผ \n" \
              "high \n" \
              "- ํ ์ผ \n" \
              "- ํ ์ผ \n" \
              "์ด๋ค ์ฅ์ ๋ฌผ์ด๋ ๋ฌธ์ ๊ฐ ์๋์?\n" \
              "- ex. OAUTH2.0 ์ธ์ฆ ๊ณผ์ ์ ๋ฌธ์ ๊ฐ ์์\n" \

    send_message(message, channel_name)
