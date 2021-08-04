import numpy as np
import pandas as pd
import requests
import cfbd

from secrets import api_key

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))


all_games = pd.DataFrame()

for year in range(2010, 2021):  # @will try datetime.datetime.now.year in case hard coding requires maintenance
    games = api_instance.get_games(year=year)

    for game in games:
        print(game.attendance)
    # games.to_csv('{}_games.csv'.format(year))

    # all_games = pd.concat([games, all_games])

# all_games.to_csv('data/allgames.csv')