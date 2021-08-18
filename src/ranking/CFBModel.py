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
        game_data = self.data['games']

        # Select columns
        x = game_data[['_season', '_week', '_season_type', '_neutral_site', '_conference_game', '_venue_id', '_home_id', '_away_id', '_home_conference', '_away_conference']]
        y = game_data['_home_points'] - game_data['_away_points']

        # Data Transforms
        x.loc[:, '_season_type'] = LabelEncoder().fit_transform(x['_season_type'])
        x.loc[:, '_home_conference'] = LabelEncoder().fit_transform(x['_home_conference'])
        x.loc[:, '_away_conference'] = LabelEncoder().fit_transform(x['_away_conference'])
        x.loc[:, '_venue_id'] = LabelEncoder().fit_transform(x['_venue_id'])
        x.loc[:, '_home_id'] = LabelEncoder().fit_transform(x['_home_id'])
        x.loc[:, '_away_id'] = LabelEncoder().fit_transform(x['_away_id'])

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=0)
        regression_model.fit(x_train, y_train)
        return regression_model.score(x_test, y_test)
