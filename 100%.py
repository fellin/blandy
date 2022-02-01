#by @CREATIVE_tg1
"""
59 Модуль 100%.

Команды:
.tr (текст) - модуль, как "Взлом чата на ...%" и тд, только вы можете выберать текст.

Для загрузки модуля перешлите сообщение с файлом себе в лс и напишете .loadmod в ответ на него, или скопируйте ссылку ниже и просто вставьте её в чат.

(Ссылка будет, как подключу домен)
"""

from .. import loader, utils
from asyncio import sleep

class AMod(loader.Module):
    strings = {"name": "100%"}

    async def trmodcmd(self, message):
        args = utils.get_args_raw(message)
        for i in range(101):
            await message.edit(f"{args} {str(i)}%")
            await sleep(0.3)
