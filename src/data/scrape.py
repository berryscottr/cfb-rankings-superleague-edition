import numpy as np
import pandas as pd
import cfbd
import datetime
import csv

from secrets import api_key

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))


all_games = pd.DataFrame()

# for year in range(2010, datetime.datetime.now.year):
for year in range(2010, 2021):

    # Pulls games
    games = api_instance.get_games(year=year)

    with open('src/data/games/{}_games.csv'.format(year), 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Writes the headers
        game_headers = games[0].__dict__.keys()
        writer.writerow(game_headers)

        # Writes out the game rows 
        for game in games:
            writer.writerow(game.__dict__.values())
