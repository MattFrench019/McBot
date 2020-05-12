import discord
import mcstatus as mc
import asyncio

# Auth Token for Discord
TOKEN = "XXXXXXX"

# Minecraft Server
IP = "5.196.83.64"
PORT = 25584

# Set up bot with the command prefix (";;")
client = discord.Client()


async def update():
	await asyncio.sleep(5)

	server = mc.server.MinecraftServer(IP, PORT)

	while True:
		print("Updating")

		try:
			status = server.status()

			if status:
				print("Normal")
				await client.change_presence(activity=discord.Game(name=f": {server.status().players.online} online"))

		except ConnectionRefusedError:
			print("ConnectionRefusedError")
			await client.change_presence(activity=discord.Game(name="OFFLINE"))

		except OSError:
			print("OSError")
			await client.change_presence(activity=discord.Game(name="STARTING"))

		await asyncio.sleep(10)


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


if __name__ == '__main__':
	asyncio.run_coroutine_threadsafe(update(), asyncio.get_event_loop())
	client.run(TOKEN)
