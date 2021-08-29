import csv
import ast
import json
import pandas as pd

for year in range(2010,2021):
    for week in range (1, 17):

        new_stats_file = []
        outframe = pd.DataFrame()
        try:
            with open('src/data/team_stats/{}_week_{}_team_stats.csv'.format(year, week), newline='') as csvfile:
                reader = csv.reader(csvfile)
                counter = 0
                for row in reader:
                    counter += 1

                    if counter == 1:
                        new_stats_file.append(['game_id','team','category','stat'])
                        continue

                    stats_row = row[1]
                    json_stats_row = ast.literal_eval(stats_row)

                    for cat in json_stats_row[0]['stats']:
                        new_stats_file.append([row[0], json_stats_row[0]['school'], cat['category'], cat['stat']])
        except FileNotFoundError:
            print('File not found')

        with open('src/data/team_stats/{}_week_{}_team_stats_fixed.csv'.format(year, week),'w+', newline='') as outfile:
            writer = csv.writer(outfile)
            if(len(new_stats_file) == 0):
                continue
            writer.writerows(new_stats_file)