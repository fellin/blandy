import random
import asyncio
from .. import loader, utils


@loader.tds
class TagAllMod(loader.Module):
    """Тегает всех в чате."""
    strings = {"name": "TagAll"}

    async def tagallcmd(self, message):
        """Используй .tagall <число> <текст (по желанию)>."""
        args: str = utils.get_args_raw(message)
        num, text = args.split(" ", maxsplit=1)
        tag = text or "говно залупное\n                пашет."

        users = [
            f"<a href='tg://user?id={user.id}'>\u2060</a>"
            async for user in message.client.iter_participants(message.to_id)
            if not (user.bot or user.deleted)
        ]

        random.shuffle(users)
        await message.delete()

        return await asyncio.gather(
            *[
                message.respond(
                    tag + '\u2060'.join(chunk))
                for chunk in list(chunks(users, int(num)))
            ]
        )


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
