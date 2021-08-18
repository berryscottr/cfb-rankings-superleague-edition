import pandas as pd


class CFBDataframe:
    def __init__(self):
        # list of dfs values[0] and empty init df values[1]
        self.data_map = {"drives": [[], pd.DataFrame()], "games": [[], pd.DataFrame()], "lines": [[], pd.DataFrame()],
                         "player_game_stats": [[], pd.DataFrame()], "player_season_stats": [[], pd.DataFrame()],
                         "player_usage": [[], pd.DataFrame()], "recruiting_groups": [[], pd.DataFrame()],
                         "recruiting_players": [[], pd.DataFrame()], "recruiting_teams": [[], pd.DataFrame()],
                         "cleaned_games": [[], pd.DataFrame()], 
                         "venues": [[], pd.DataFrame()]}

    @staticmethod
    def append_dfs(df, df_type):
        # append df to list of dfs
        df_type[0].append(df)
        # concat list of dfs
        df_type[1] = pd.concat(df_type[0])

    @staticmethod
    def impute_df(file):
        # import data with Windows encoding
        try:
            df = pd.read_csv(file, encoding='ANSI')  # , na_values='?')
            # df.fillna(pd.Series.mean(df))
        # if not Windows, do Mac encoding
        except LookupError:
            try:
                df = pd.read_csv(file, encoding='ISO-8859-1')  # , na_values='?')
                # df.fillna(pd.Series.mean(df))
            except pd.errors.EmptyDataError:
                print(file, "is empty")
                return
        # if empty data, skip file
        except pd.errors.EmptyDataError:
            print(file, "is empty")
            return
        # set first row as headers
        df.rename(columns=df.iloc[0])
        return df

    def csv_to_df(self, args):
        # not time based
        if len(args) == 1:
            file = "../data/{i}/{i}.csv".format(i=args[0])
        # season based
        elif len(args) == 2:
            file = "../data/{i}/{j}_{i}.csv".format(i=args[0], j=args[1])
        # game based
        else:
            file = "../data/{i}/{k}_week_{j}_{i}.csv".format(i=args[0], j=args[1], k=args[2])
        # import csv to df
        df = self.impute_df(file)
        # append non-empty dfs
        if type(df) is not None:
            self.append_dfs(df, self.data_map[args[0]])