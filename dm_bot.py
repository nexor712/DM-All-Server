import discord
import asyncio

TOKEN = "TOKEN"  # Put here the token of your bot
GUILD_ID = GUILD_ID  # Put here the guid id of your server
MESSAGE = "THE_MESSAGE"
COOLDOWN = COOLDOWN  # Seconds

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print("Το bot δεν είναι σε αυτό το guild.")
        return  # We do not shut down the bot, we just stop sending.

    members = [m for m in guild.members if not m.bot]
    total_members = len(members)
    count = 0

    for member in members:
        try:
            await member.send(MESSAGE)
            count += 1
            print(f"Sent to {member} ({count}/{total_members})")
            await asyncio.sleep(COOLDOWN)
        except Exception as e:
            print(f"Could not sent to {member}: {e}")

    print(f"All the messages have been sent! Total: {count}")

# The bot stays online and can do other things or resend a DM if you want
client.run(TOKEN)
