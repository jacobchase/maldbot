import discord
from discord.ext import commands
import os # default module
from dotenv import load_dotenv
import random
# Create a bot instance with a command prefix
load_dotenv()
TOKEN = os.getenv('token')
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

async def check_malding(message):
    if "malding" in message.content.lower():
        await message.channel.send("MALDING")

async def check_malder(message):
    if "malder" in message.content.lower():
        await message.channel.send("MALDING")

async def skill_issue(message):
    if "skill issue" in message.content.lower():
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
## need to replace the links if i am actually going to use this
async def choose_gif(number):
    if number == 1:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 2:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 3:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 4:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 5:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 6:  
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 7:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 8:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 9:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")
    elif number == 10:
        await message.channel.send("https://media.discordapp.net/attachments/533385207789649950/990629824374665236/ezgif-5-43ee149553.gif?ex=673ca56b&is=673b53eb&hm=1353acbe06993a8a380239d101dd6f8ec47243d706c6e0abcdc7233b712cd71d&")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await check_malding(message)
    await check_malder(message)
    await skill_issue(message)

@bot.command(description="responds with bot latency")
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="Generates a random number between 1 and 10")
async def random_number(ctx):
    number = random.randint(1, 10)
    await ctx.respond(f"Your random number is: {number}")

@bot.command(description="Bans a specified user from the server")
async def ban(ctx, member: discord.Member, *, reason=None):
    # Check if the user has the permission to ban members
    if not ctx.author.guild_permissions.ban_members:
        await ctx.respond("You don't have permission to ban members!")
        return
    
    # Check if the bot has permission to ban members
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.respond("I don't have permission to ban members!")
        return
        
    # Check if the target member can be banned by the bot
    if member.top_role >= ctx.guild.me.top_role:
        await ctx.respond("I cannot ban this user as their role is higher than or equal to mine!")
        return
        
    try:
        await member.ban(reason=reason)
        await ctx.respond(f"{member.name} has been banned.\nReason: {reason if reason else 'No reason provided'}")
    except discord.Forbidden:
        await ctx.respond("I don't have permission to ban this user!")
    except discord.HTTPException:
        await ctx.respond("An error occurred while trying to ban the user.")
@bot.command(description="Mutes a user for a specified duration (permanent if no duration given)")
async def mute(ctx, member: discord.Member, duration: str = None, *, reason=None):
    # Check if the user has permission to manage roles
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don't have permission to mute members!")
        return
    
    # Check if the bot has permission to manage roles
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.respond("I don't have permission to manage roles!")
        return
        
    # Check if the target member can be muted by the bot
    if member.top_role >= ctx.guild.me.top_role:
        await ctx.respond("I cannot mute this user as their role is higher than or equal to mine!")
        return

    # Look for a "Muted" role or create one if it doesn't exist
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        try:
            muted_role = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            # Set up permissions for the muted role
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)
        except discord.Forbidden:
            await ctx.respond("I don't have permission to create roles!")
            return
        except discord.HTTPException:
            await ctx.respond("An error occurred while creating the muted role.")
            return

    try:
        # If user already has muted role
        if muted_role in member.roles:
            await ctx.respond(f"{member.name} is already muted!")
            return

        await member.add_roles(muted_role, reason=reason)
        
        if duration:
            try:
                # Convert duration string to seconds
                time_units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
                unit = duration[-1].lower()
                if unit not in time_units:
                    await ctx.respond("Invalid time unit! Use s (seconds), m (minutes), h (hours), or d (days)")
                    return
                time = int(duration[:-1]) * time_units[unit]
                
                await ctx.respond(f"{member.name} has been muted for {duration}.\nReason: {reason if reason else 'No reason provided'}")
                
                # Wait for the specified duration then unmute
                await asyncio.sleep(time)
                if muted_role in member.roles:  # Check if still muted
                    await member.remove_roles(muted_role)
                    await ctx.channel.send(f"{member.name} has been automatically unmuted.")
            except ValueError:
                await ctx.respond("Invalid time format!")
                return
        else:
            await ctx.respond(f"{member.name} has been muted permanently.\nReason: {reason if reason else 'No reason provided'}")
            
    except discord.Forbidden:
        await ctx.respond("I don't have permission to mute this user!")
    except discord.HTTPException:
        await ctx.respond("An error occurred while trying to mute the user.")

@bot.command(description="Unmutes a muted user")
async def unmute(ctx, member: discord.Member):
    # Check if the user has permission to manage roles
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don't have permission to unmute members!")
        return
        
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.respond("There is no muted role set up!")
        return
        
    if muted_role not in member.roles:
        await ctx.respond(f"{member.name} is not muted!")
        return
        
    try:
        await member.remove_roles(muted_role)
        await ctx.respond(f"{member.name} has been unmuted.")
    except discord.Forbidden:
        await ctx.respond("I don't have permission to unmute this user!")
    except discord.HTTPException:
        await ctx.respond("An error occurred while trying to unmute the user.")



# Replace 'YOUR_TOKEN' with your actual bot token
bot.run(TOKEN)
