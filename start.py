import config
from config import first_name, last_name
from rich.console import Console
from rich.table import Table
from rich import print
from cls import cls
import sys
import os

cls()

table = Table(header_style="bold magenta", border_style="green", title="Опции:", caption="t.me/matazimov_official")
table.add_column("№")
table.add_column("Описание")
table.add_row(
    "1",
    "Добавить друзей со стен групп/страниц"
)
table.add_row(
    "2",
    "Добавить друзей с раздела рекоменд."
)
table.add_row(
    "3",
    "Принять [bold yellow]новые[/bold yellow] заявки в друзья"
)
table.add_row(
    "4",
    "Принять [bold red]все[/bold red] заявки в друзья"
)
table.add_row(
    "5",
    "Отписаться от [bold red]всех[/bold red] исходящих заявок"
)
table.add_row(
    "6",
    "Удалить неактивных друзей"
)
table.add_row(
    "7",
    "Удалить невидимых друзей"
)
table.add_row(
    "8",
    "Удалить собачек из друзей"
)
table.add_row(
    "9",
    "Удалить [bold red]всех[/bold red] друзей"
)
table.add_row(
    "10",
    "Написать в \"Добавь в друзья\""
)
table.add_row(
    "11",
    "Коммент в \"Добавь в друзья\""
)
table.add_row(
    "0",
    "Помощь"
)
table.caption_style = "bold cyan"

console = Console()
console.print(table)

print("")
vid = input(f"({first_name} {last_name}) Выберите опцию: ")

if vid == "1":
    import handlers.friends_add_from_wall
elif vid == "2":
    import handlers.friends_add_from_recommended_section
elif vid == "3":
    import handlers.request_accept.new
elif vid == "4":
    import handlers.request_accept.all
elif vid == "5":
    import handlers.unsubscribe
elif vid == "6":
    import handlers.friends_delete.one_day_and_more
elif vid == "7":
    import handlers.friends_delete.without_last_seen
elif vid == "8":
    import handlers.friends_delete.deleted
elif vid == "9":
    import handlers.friends_delete.all
elif vid == "10":
    import handlers.write
elif vid == "11":
    import handlers.comment
elif vid == "0":
    cls()
    print("1. [bold]Добавить друзей со стен групп/страниц[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "Допустим вы захотели добавить друзей с группы \"добавь в друзья\". "
          "Там каждую секунду, на стену этой группы пишут десятки людей. "
          "Безусловно, можно нажать на аватарки пользователей, перейти на их страницу и добавить. "
          "Но спустя некоторое время вы обнаруживаете, что так больше не можете, ведь это так муторно. "
          "Тем более этот пользователь может и так являться вашим другом. "
          "Так как быть? 1 опция - вам в помощь!"
          "\n[/bold cyan]"
          "2. [bold]Добавить друзей с раздела рекоменд[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "Такая же история, как и на первом, только тут всего лишь раздел \"рекомендованные друзья\". "
          "Что такого в этом разделе? В этом разделе ВК подготавливает список пользователей с теми, "
          "с кем у вас есть больше всего общих друзей. Минус этого раздела в том, что ВК "
          "может подсунуть неактивных пользователей. Но все же 2 опция существует, которая "
          "автоматически добавляет всех существующих пользователей в этом списке. "
          "Алгоритмы ВК не часто подготавливают этот список. Почему? Я думаю, что это из-за того, "
          "что у них и других забот хватает. Кстати, это второй минус. "
          "Так что не удивляйтесь, если вы получите ошибку в этой опции, что "
          "\"Вконтакте пока что не подготовил рекомендованных друзей((\"."
          "\n[/bold cyan]"
          "3. [bold]Принять новые заявки в друзья[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "По сути в названии все и так написано, но я объясню подробнее. "
          "Что означает \"новые\"? Это означает, что скрипт примит только те заявки в друзья, "
          "которые вы еще не обработали (не отклонили/не приняли). Кстати, скрипт не может принимать собачек."
          "\n[/bold cyan]"
          "4. [bold]Принять все заявки в друзья[/bold].\n"
          "5. [bold]Отписаться от всех исходящих заявок[/bold].\n"
          "6. [bold]Удалить неактивных друзей[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "Что делает эта опция? Удаляет друзей, которые не заходили более 1 дня."
          "\n[/bold cyan]"
          "7. [bold]Удалить невидимых друзей[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "Что означает невидимых? Это те люди, которые включили невидимку в VK ME. Ну и зачем мне их удалять? "
          "Да затем, что при использовании невидимки от VK ME, у пользователей пропадает время посещения. "
          "При том не только в самом ВК пропадает, а от всего. Даже, если api запросом получить информацию "
          "о пользователи, то поле \"last_seen\" (последнее посещение) отсутствует. Почему это плохо? "
          "Потому что пользователи могут уже давно не заходить на свою страницу, а вы об этом даже не узнаете. "
          "Конечно, в ВК будет отображаться, что \"заходил давно\", но скрипт не сможет отфильтровать их "
          "по последнему посещению. То есть при удалении друзей 6 опцией, невидимые друзья не удаляться. "
          "Для решения этой проблемы есть 7 опция!"
          "\n[/bold cyan]"
          "8. [bold]Удалить собачек из друзей[/bold].\n"
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          "Удаляет всех заблокированных/замороженных/удаленных друзей."
          "\n[/bold cyan]"
          "9. [bold]Удалить всех друзей[/bold].\n"
          '10. [bold]Написать в "Добавь в друзья"[/bold]\n'
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          'Вы когда-нибудь пиарились в группах взаимного пиара? Согласитесь, что это очень сложно и '
          'муторно вручную. Для этого есть десятая функция, которая автоматически за вас пишет в '
          'группы взаимного пиара. Список групп вы можете изменить (добавить/удалить). Для этого '
          f'вам нужно зайти в эту директорию {os.getcwd()} найти папку "handlers" затем '
          f'"write" и изменить файл groups.py.'
          "\n[/bold cyan]"
          '11. [bold]Коммент в "Добавь в друзья"[/bold]\n'
          "[bold yellow]Подробнее[/bold yellow]:"
          "\n[bold cyan]"
          'Замечали, что когда пиаришься в группах взаимного пиара, под вашим постом юзеры пишут комменты, '
          'которые тоже пиарятся? Так вот, 11 функция автоматизирует этот процесс'
          "\n[/bold cyan]"
          )
else:
    print("[red]Выберите только из предложенных вариантов[/red]")
    sys.exit()
