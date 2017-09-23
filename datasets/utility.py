import pandas as pd
import datetime


# date input format mm/dd/yyyyy
def num_of_dates_till_end_of_season(game_day):
    last_game_date_of_year = {
        '2013': '04/16/2014',
        '2014': '04/15/2015',
        '2015': '04/13/2016',
        '2016': '04/12/2017'
    }
    # print(game_day)
    date_format = "%m/%d/%Y"
    game_date = datetime.datetime.strptime(game_day, date_format)
    # print(game_date)
    if game_date.month <= 4:
        end_day = last_game_date_of_year.get(str(game_date.year - 1))
    else:
        end_day = last_game_date_of_year.get(str(game_date.year))

    end_date = datetime.datetime.strptime(end_day, date_format)

    difference = end_date - game_date
    return difference.days


df = pd.read_csv('Game_Data.csv')
# df['date_est'][12000]
print(num_of_dates_till_end_of_season('04/10/2015'))

# print(list(df))
#
# for index, row in df.iterrows():
#     print(index,row['Game_id'])
