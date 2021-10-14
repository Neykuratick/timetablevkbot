CHANGE_GROUP_MESSAGE = "Напишите мне новый номер группы"
INVALID_INPUT_MESSAGE = "Мне нужны только циферки!"
DEFAULT_ANSWER_MESSAGE = 'Oк'
INVALID_COMMAND = 'Я нинаю таких команд((( Попробуй написать "Старт" или "Привет" чтобы открыть меню, ' \
                  'а потом зайти в "Настройки"'


def Settings(group_index):
    return f"""Ваша группа: {group_index}

Список команд:
https://vk.com/mpsu_schedule?w=wall-206763355_30
https://vk.com/wall-206763355_42


F.A.Q:
https://vk.com/topic-206763355_48153565

Если чё-то не работает, пиши мне @baboomka"""


def Spreadsheet_update_info():
    with open('Assets/spreadsheet_lastupdatetime', 'r') as f:
        last_update_time = f.read()

    with open('Assets/spreadsheet_id', 'r') as f:
        spreadsheet_id = f.read()

    return f"Расписание последний раз обновлялось сегодня в {last_update_time}\n\nid: {spreadsheet_id}"