import discord;
from discord.ext import commands, tasks;
import random
from datetime import datetime
import os #environment variable


TOKEN = os.environ['token']; #Switch to user bot token


intents = discord.Intents().all();
client = commands.Bot(command_prefix = '!', intents = intents);


@tasks.loop(seconds=20)
async def change_status():
    return;


@client.event
async def on_ready():
    change_status.start();
    print('Bot ready');


@client.command (
        name = "roll", 
        help = "given command ndk, where n is the number of dice and k is the number of sides the dice have, simulate dice roll and return sum"
)
async def roll(ctx):
    curr_dt = datetime.now()
   
    timestamp = int(round(curr_dt.timestamp()))
    random.seed(timestamp);
  
    ctx_list = ctx.message.content.split();
    list_len = len(ctx_list);

    if list_len > 2:
        await ctx.send("Error: invalid arguments");
    
    else:
        num_dice = 1;
        roll_spec = ctx_list[1];
        argument_list = roll_spec.split("d");

        dice_sides = int(argument_list[1]);
    
    if not argument_list[0] == "":
        num_dice = int(argument_list[0]);

    sum = 0;
    
    for x in range(num_dice):
        sum += random.randint(1, dice_sides);

    if num_dice == 1 and dice_sides == 20 and sum == 20:
        await ctx.send("Critical Success! Natural 20!");
    else:
        if num_dice == 1 and dice_sides == 20 and sum == 1:
            await ctx.send("Critical Failure! Natural 1!")
        else:
            await ctx.send(sum);


client.run(TOKEN);