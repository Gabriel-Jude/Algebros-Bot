# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START calendar_quickstart]
from __future__ import print_function

import datetime
import os.path

# from datetime import datetime
# from pytz import timezone

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dateutil import parser

# Discord Stuff

import discord
from discord.ext import commands

intents = discord.Intents.all()  # or .all() if you ticked all, that is easier
intents.members = False  # If you ticked the SERVER MEMBERS INTENT

client = commands.Bot(command_prefix=".", intents=intents)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    @client.event
    async def on_ready():
        print('Wakey Wakey I am {0.user}'.format(client))

    @client.command(name="listAll")
    async def whereIsWaldo(ctx):
        list = gCalendarDailyEvents(creds)

        for x in list:
            await ctx.channel.send(x)

    client.run("YOURBOTTOKEN")


def gCalendarDailyEvents(creds):
    try:
        service = build('calendar', 'v3', credentials=creds)
        today = datetime.datetime.today()
        start = (datetime.datetime(today.year, today.month, today.day, 00, 00)).isoformat() + 'Z'
        tomorrow = today + datetime.timedelta(days=1)
        end = (datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 00, 00)).isoformat() + 'Z'
        print('Getting todays events')
        events_results = service.events().list(calendarId='primary', timeMin=start, timeMax=end, singleEvents=True,
                                               orderBy='startTime').execute()

        events = events_results.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        print("Daily Events")

        list = []

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))

            start_formatted = parser.isoparse(start)
            end_formatted = parser.isoparse(end)


            string = start_formatted.strftime("%H:%M") + " " + end_formatted.strftime("%H:%M") + " " + event['summary']
            list.append(string)

        return list


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
# [END calendar_quickstart]
