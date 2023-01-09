import discord
from discord.ext import commands
# import os


import datetime

from datetime import datetime
from pytz import timezone

intents = discord.Intents.all()  # or .all() if you ticked all, that is easier
intents.members = False  # If you ticked the SERVER MEMBERS INTENT

client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print('Wakey Wakey I am {0.user}'.format(client))


@client.command(name="loc")
async def whereIsWaldo(ctx, arg):
    if arg == "Gabe":
        await ctx.send(GabeSchedule())
    elif arg == "Name":
        await ctx.channel.send(NameSchedule())
    elif arg == "Name":
        await ctx.channel.send(NameSchedule())
    elif arg == "Name":
        await ctx.channel.send(NameSchedule())
    elif arg == "Name":
        await ctx.channel.send(NameSchedule())
    elif arg == "Name":
        await ctx.channel.send(NameSchedule())



@client.command(name="locAll")

async def whereIsWaldo(ctx):

    await ctx.channel.send(GabeSchedule())
    await ctx.channel.send(NameSchedule())
    await ctx.channel.send(NameSchedule())
    await ctx.channel.send(NameSchedule())
    await ctx.channel.send(NameSchedule())
    await ctx.channel.send(NameSchedule())


def GabeSchedule():
    # Imports

    # Set timezone
    tz = timezone("US/Eastern")
    # Date with timezone
    date = datetime.now(tz)

    # Formatting
    print(date)
    current_time = date.strftime("%H:%M")
    current_date = date.strftime("%A")
    print(current_date)
    current_time_inhours = int(current_time[0:2])

    if current_date == "Monday":

        if "08:00" <= current_time <= "10:59":
            return "Gabe is in EES 512 Lecture"
        elif "11:00" <= current_time <= "12:00":
            return "Gabe is in CHE 217 Tutorial"
        elif "12:00" <= current_time <= "13:00":
            return "Gabe is on a break his next class is in " + str(12 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "13:00" <= current_time <= "15:00":
            return "Gabe is CHY 224 Lecture"
        elif "15:00" <= current_time <= "18:00":
            return "Gabe is on break his next class is in " + str(17 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "18:00" <= current_time <= "21:00":
            return "Gabe is in CHE 217 Lecture"
        else:
            return "Gabe is done for the day"

    if current_date == "Tuesday":
        if "08:00" <= current_time <= "10:00":
            return "Gabe is in EES 512 Tutorial"
        elif "10:00" <= current_time <= "13:00":
            return "Gabe is on break his next class is in " + str(12 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "13:00" <= current_time <= "15:00":
            return "Gabe is in MTH 425 Lab"
        elif "15:00" <= current_time <= "16:00":
            return "Gabe is on break his next class is in " + str(15 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "16:00" <= current_time <= "18:00":
            return "Gabe is in CHE 217 Lab"
        else:
            return "Gabe is done for the day"

    if current_date == "Wednesday":
        if "08:00" <= current_time <= "10:00":
            return "Gabe is in CHE 204 Lecture"
        elif "10:00" <= current_time <= "12:00":
            return "Gabe is on break his next class is in " + str(11 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "12:00" <= current_time <= "14:00":
            return "Gabe is in MTH 425 Lecture"
        else:
            return "Gabe is done for the day"

    if current_date == "Thursday":
        if "09:00" <= current_time <= "12:00":
            return "Gabe is in CHE 224 Lab"
        elif "12:00" <= current_time <= "14:00":
            return "Gabe is on break his next class is in " + str(13 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "14:00" <= current_time <= "15:00":
            return "Gabe is in CHE 204 Tutorial"
        elif "15:00" <= current_time <= "16:00":
            return "Gabe is on break his next class is in " + str(15 - int(current_time[0:2])) + " hours and " + str(
                60 - int(current_time[3:5])) + " minutes"
        elif "16:00" <= current_time <= "18:00":
            return "Gabe is in CHY 224 Lecture"
        else:
            return "Gabe is done for the day"

    if current_date == "Friday":
        if "08:00" <= current_time <= "10:00":
            return "Should be in MTH 425 Lecture but he is probably sleeping"
        else:
            return "Gabe is done for the day"
    else:
        return "Gabe is probably sleeping"


def NameSchedule():
    # Imports

    # Set timezone
    tz = timezone("US/Eastern")
    # Date with timezone
    date = datetime.now(tz)

    # Formatting

    current_time = date.strftime("%H:%M")
    current_date = date.strftime("%A")
    current_time_inhours = int(current_time[0:2])

    if current_date == "Monday":

        if "09:00" <= current_time <= "11:00":
            return "Name is in CMN 423 Lecture"
        elif "11:00" <= current_time <= "12:00":
            return "Name is in AER 318 Lecture"
        elif "12:00" <= current_time <= "13:00":
            return "Name is on a break his next class is in " + str(12 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "13:00" <= current_time <= "15:00":
            return "Name is in AER 309 Lecture"
        else:
            return "Name is done for the day"

    if current_date == "Tuesday":
        if "08:00" <= current_time <= "10:00":
            return "Name is in AER 316 Lecture"
        elif "10:00" <= current_time <= "12:00":
            return "Name is in AER 320 Lecture"
        elif "12:00" <= current_time <= "13:00":
            return "Name is on a break his next class is in " + str(12 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "13:00" <= current_time <= "14:00":
            return "Name is in AER 318 Lab"
        else:
            return "Name is done for the day"

    if current_date == "Wednesday":
        if "08:00" <= current_time <= "10:00":
            return "Name is in MTH 425 Lab"
        elif "10:00" <= current_time <= "12:00":
            return "Name is in AER 316"
        elif "12:00" <= current_time <= "14:00":
            return "Name is in MTH425 Lecture"
        else:
            return "Name is done for the day"

    if current_date == "Thursday":
        if "09:00" <= current_time <= "11:00":
            return "Name is in CMN 423 Lab"
        elif "11:00" <= current_time <= "12:00":
            return "Name is in AER 309 Lecture"
        elif "12:00" <= current_time <= "14:00":
            return "Name is on break his next class is in " + str(13 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "14:00" <= current_time <= "15:00":
            return "Name is in AER 316 Lecture"
        else:
            return "Name is done for the day"

    if current_date == "Friday":
        if "08:00" <= current_time <= "10:00":
            return "Should be in MTH 425 Lecture"
        elif "10:00" <= current_time <= "11:00":
            return "Name is in AER 320 LAB"
        elif "11:00" <= current_time <= "12:00":
            return "Name is on break his next class is in " + str(12 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "12:00" <= current_time <= "14:00":
            return "Name is in AER 320 Lecture"
        elif "14:00" <= current_time <= "16:00":
            return "Name is on break his next class is in " + str(15 - current_time_inhours) + " hours and " + str(
                60 - int(date.strftime("%M"))) + " minutes"
        elif "16:00" <= current_time <= "18:00":
            return "Name is in AER 318 Lecture"
        else:
            return "Name is done for the day"

    else:
        return "Name is probably sleeping"


# keep_alive()
 client.run("YOURBOTTOKEN")
