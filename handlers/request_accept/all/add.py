from config import token, v
from .get_id import humans
from rich import print
import requests
import sys

if len(humans) > 0:
    print(f"[purple]У вас {len(humans)} подписчиков[/purple]")
    confirm = input("Принять все заявки? [Да/Нет] ")
    if confirm.lower() == "да":
        print("[cyan]Начинаю добавлять...[/cyan]")
    elif confirm.lower() == "нет":
        print("[red]Действие отменено[/red]")
        sys.exit()
    else:
        print("[red]Выберите только из предложенных вариантов[/red]")
        sys.exit()

    i = 0
    while i < len(humans):
        data = requests.post("https://api.vk.com/method/friends.add", params={
            "v": v,
            "user_id": humans[i],
            "access_token": token
        }).json()
        if "response" in data:
            print(f"[blue]id{humans[i]}[/blue]: Принял")
        elif "error" in data:
            if data["error"]["error_code"] == 1:
                print("[green]Лимит на добавления в друзья[/green]")
                sys.exit()
            elif data["error"]["error_code"] == 29:
                print('[red]Достигнут количественный лимит на вызов метода[/red]'
                      'Подробнее об ограничениях на количество вызовов см. на странице '
                      'https://vk.com/dev/data_limits')
                sys.exit()
            print(f"[blue]id{humans[i]}[/blue]: Пользователь заблокирован/удален")
        else:
            print("упс... произошла неизвестная ошибка")
            sys.exit()
        i += 1
    print("[green]Все![/green]")
else:
    print("[red]У вас нет подписчиков[/red]")
