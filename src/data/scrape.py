import cfbd
import csv
import time

from secrets import api_key
from cfbd.models import play

from cfbd.rest import ApiException

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

games_api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
drives_api_instance = cfbd.DrivesApi(cfbd.ApiClient(configuration))
players_api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
betting_api_instance = cfbd.BettingApi(cfbd.ApiClient(configuration))
recruiting_api_instance = cfbd.RecruitingApi(cfbd.ApiClient(configuration))
venues_api_instance = cfbd.VenuesApi(cfbd.ApiClient(configuration))

class ScrapeWriter():
    def __init__(self, data, data_string, year=None, week=None):
        self.data = data
        self.data_string = data_string
        self.year = year
        self.week = week
    
    def write_scraped_data(self):
        with open(self.file_string(), 'w', newline='') as outfile:
            writer = csv.writer(outfile)

            # Slices from 1 to avoid the configuration columns
            # Writes the headers
            data_headers = list(self.data[0].__dict__.keys())
            writer.writerow(data_headers[1:])

            # Writes out the game rows 
            for data_row in self.data:
                writer.writerow(list(data_row.__dict__.values())[1:])

    def file_string(self):
        if self.week:
            return 'src/data/{}/{}_week_{}_{}.csv'.format(self.data_string,self.year,self.week,self.data_string)
        if self.year:
            return 'src/data/{}/{}_{}.csv'.format(self.data_string,self.year,self.data_string)
        else:
            return 'src/data/{}/{}.csv'.format(self.data_string,self.data_string)


# for year in range(2010, datetime.datetime.now.year):
for year in range(2019, 2021):
    print('Starting year: {}'.format(year))

    # Pulls games
    games = games_api_instance.get_games(year=year, season_type='both')
    games_writer = ScrapeWriter(games, 'games', year)
    games_writer.write_scraped_data()

    # Pulls player individual game stats
    for week in range(1,20):
        try:
            player_game_stats = games_api_instance.get_player_game_stats(year=year, season_type='both', week=week)
            player_game_stats_writer = ScrapeWriter(player_game_stats, 'player_game_stats', year, week)
            player_game_stats_writer.write_scraped_data()
        except ApiException:
            print('API Exception for year {} and week {}'.format(year, week))
        except IndexError:
            print('No weeks left')
        except ValueError:
            print('No weeks left')

    # Pulls team drive stats
    drives = drives_api_instance.get_drives(year=year, season_type='both')
    drives_writer = ScrapeWriter(drives, 'drives', year)
    drives_writer.write_scraped_data() 

    if year >= 2013:
        lines = betting_api_instance.get_lines(year=year, season_type='both')
        lines_writer = ScrapeWriter(lines, 'lines', year)
        lines_writer.write_scraped_data()
    
        player_usage = players_api_instance.get_player_usage(year=year)
        player_usage_writer = ScrapeWriter(player_usage, 'player_usage', year)
        player_usage_writer.write_scraped_data()

    player_season_stats = players_api_instance.get_player_season_stats(year=year, season_type='both')
    player_season_stats_writer = ScrapeWriter(player_season_stats, 'player_season_stats', year)
    player_season_stats_writer.write_scraped_data()
    
    recruiting_players = recruiting_api_instance.get_recruiting_players(year=year)
    recruiting_players_writer = ScrapeWriter(recruiting_players, 'recruiting_players', year)
    recruiting_players_writer.write_scraped_data()

venues = venues_api_instance.get_venues()
venues_writer = ScrapeWriter(venues, 'venues')
venues_writer.write_scraped_data()

recruiting_groups = recruiting_api_instance.get_recruiting_groups()
recruiting_groups_writer = ScrapeWriter(recruiting_groups, 'recruiting_groups')
recruiting_groups_writer.write_scraped_data()

recruiting_teams = recruiting_api_instance.get_recruiting_teams()
recruiting_teams_writer = ScrapeWriter(recruiting_teams, 'recruiting_teams')
recruiting_teams_writer.write_scraped_data()