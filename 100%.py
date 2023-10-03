from .. import loader, utils
from asyncio import sleep

class AMod(loader.Module):
    strings = {"name": "100%"}

    async def trmodcmd(self, message):
        args = utils.get_args_raw(message)
        for i in range(101):
            await message.edit(f"{args} {str(i)}%")
            await sleep(0.3)
