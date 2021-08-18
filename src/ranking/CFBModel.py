import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class CFBModel:
    def __init__(self, df):
        # dict of dfs
        self.data = {k: df[k][1] for k in df}

    def home_favored(self):
        mean_home_points = pd.Series.mean(self.data["games"]["_home_points"])
        mean_away_points = pd.Series.mean(self.data["games"]["_away_points"])
        return mean_home_points - mean_away_points

    def regression_predict(self, predictors):
        regression_model = LinearRegression()
        indep_vars = [self.data['games']['_home_post_win_prob'], self.data['games']['_home_points']]
        dep_vars = self.data['games']['_home_points'] - self.data['games']['_away_points']
        regression_model.fit(indep_vars, dep_vars)
        prediction = regression_model.predict(predictors)
        return prediction

    def spread_prediction(self):
        regression_model = LinearRegression()
        game_data = self.data['cleaned_games']

        # Select columns
        x = game_data.loc[:,['season', 'week', 'season_type', 'neutral_site', 'conference_game', 'venue_id', 'team_id',  'team_conference', 'team_wins','team_loses','games_played','season_point_total','team_line_score_q1_total','team_line_score_q2_total','team_line_score_q3_total','team_line_score_q4_total','opp_team_id', 'opp_team_conference','opp_team_wins','opp_team_loses','opp_games_played','opp_season_point_total','opp_team_line_score_q1_total','opp_team_line_score_q2_total','opp_team_line_score_q3_total','opp_team_line_score_q4_total']]
        y = game_data['team_points'] - game_data['opp_team_points']

        # Data Transforms
        x.loc[:, 'season_type'] = LabelEncoder().fit_transform(x['season_type'])
        x.loc[:, 'team_conference'] = LabelEncoder().fit_transform(x['team_conference'])
        x.loc[:, 'opp_team_conference'] = LabelEncoder().fit_transform(x['opp_team_conference'])
        x.loc[:, 'venue_id'] = LabelEncoder().fit_transform(x['venue_id'])
        x.loc[:, 'team_id'] = LabelEncoder().fit_transform(x['team_id'])
        x.loc[:, 'opp_team_id'] = LabelEncoder().fit_transform(x['opp_team_id'])

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=0)
        regression_model.fit(x_train, y_train)
        return regression_model.score(x_test, y_test)
