import sys
import time
import config
import random
import requests
from cls import cls
from rich import print
from .groups import groups
from config import token, v, first_name, last_name

cls()

message = input(f"({first_name} {last_name}) Введите сообщение: ")

cls()

print("[cyan]Начинаю отправлять...[/cyan]")
print("Для отмены, нажмите ctrl + c + enter")


while True:
    group = random.choice(groups)
    data = requests.post("https://api.vk.com/method/wall.post", params={
        "v": v,
        "access_token": token,
        "owner_id": group,
        "message": message
    }).json()
    if "response" in data:
        print(f"[blue]public{group.replace('-', '')}[/blue]: Отправил")
    elif "error" in data:
        if data["error"]["error_code"] == 14:
            captcha_sid = data["error"]["captcha_sid"]
            print(f"Введите код с капчи:\nhttps://api.vk.com/captcha.php?"
                  f"sid={captcha_sid}")
            code = input()
            data_captcha = requests.post("https://api.vk.com/method/wall.post", params={
                "v": v,
                "access_token": token,
                "owner_id": group,
                "message": message,
                "captcha_sid": captcha_sid,
                "captcha_key": code
            }).json()
            if "response" in data_captcha:
                print("[green]Верно[/green]")
                print(f"[blue]public{group.replace('-', '')}[/blue]: Отправил")
            elif "error" in data_captcha:
                if data_captcha["error"]["error_code"] == 14:
                    print("[red]Неверно[/red]")
            else:
                print("упс... произошла неизвестная ошибка")
                sys.exit()
        elif data["error"]['error_code'] == 214:
            print("Сообщения временно запрещены")
    else:
        print("упс... произошла неизвестная ошибка")
        sys.exit()
    time.sleep(1)
