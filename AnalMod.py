

from .. import loader, utils

import logging
import asyncio
import time

logger = logging.getLogger(__name__)

@loader.tds
class GroupAnalMod(loader.Module):
	"""GroupAnal fuck your ass"""
	strings = {"name": "GroupAnal"}
	def __init__(self):
		self.name = self.strings["name"]
	def config_complete(self):
		pass
	async def analcmd(self, message):
		"""GroupAnal fuck your ass"""
		i = 0
		while i <= 99:
			await message.edit("<strong>Анальное проникновение админу выполнено на " + str(i) + "%</strong>")
			i += 1
			time.sleep(0.3)
		time.sleep(0.3)
		await message.edit("<strong>Жопа админа порвана! Поздравляю!!!</strong>")
		return

