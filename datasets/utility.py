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


# df = pd.read_csv('Game_Data.csv')
# # df['date_est'][12000]
# print(num_of_dates_till_end_of_season(df['date_est'][12000]))

########################################################################
# returns 2 list
# list1 = team1{ date, player_id, name, jersey_sale_rank}
# list2 = team2{ date, player_id, name, jersey_sale_rank}
def jersey_sales_on_teams(team1, team2, game_date, game_df, jersey_df, player_df):
    game_id_df = game_df.loc[(game_df['date_est'] == game_date) & (game_df['Team'] == team1)]
    game_id = game_id_df['Game_id'][game_id_df.index.get_values()[0]]
    team1_players_df = player_df.loc[(player_df['Game_id'] == game_id) & (player_df['Team'] == team1)]

    game_id_df = game_df.loc[(game_df['date_est'] == game_date) & (game_df['Team'] == team2)]
    game_id = game_id_df['Game_id'][game_id_df.index.get_values()[0]]
    team2_players_df = player_df.loc[(player_df['Game_id'] == game_id) & (player_df['Team'] == team2)]

    month = game_date.split('/')[0]
    target_year = int(game_date.split('/')[-1])
    if int(month) <= 4:
        target_year = target_year - 1

    # create column names
    column1 = str(target_year) + '-' + str((target_year % 100) + 1)
    column2 = str(target_year - 1) + '-' + str(target_year % 100)
    # print('t', target_year, 'col1', column1, "col2", column2)

    t1_jersey_player = 0
    t1_list = [game_date]
    for index_t1, row_t1 in team1_players_df.iterrows():
        name1 = row_t1['Person_id']
        actual_name1 = row_t1['Name']
        for index_j, row_j in jersey_df.iterrows():
            # print(row_j[column1], name1, row_j[column2])
            if row_j[column1] == name1 or row_j[column2] == name1:
                t1_jersey_player += 1
                t1_list.append((name1, actual_name1, int(index_j) + 1))
    # print(t1_jersey_player)

    t2_jersey_player = 0
    t2_list = [game_date]
    for index_t2, row_t2 in team2_players_df.iterrows():
        name2 = row_t2['Person_id']
        actual_name2 = row_t2['Name']
        for index_j, row_j in jersey_df.iterrows():
            # print(row_j[column1], name2, row_j[column2])
            if row_j[column1] == name1 or row_j[column2] == name2:
                t2_jersey_player += 1
                t2_list.append((name2, actual_name2, int(index_j) + 1))
    # print(t2_jersey_player)
    return (t1_list, t2_list)


# # test case
# player_df = pd.read_csv('Player_Data.csv')
# jersey_df = pd.read_csv('Jersey_Sales_Rankings_Data.csv')
# game_df = pd.read_csv('Game_Data.csv')
# t1_jersery_count, t2_jersey_count = jersey_sales_on_teams('SAS', 'CHA', '3/21/2016', game_df, jersey_df, player_df)
# print(t1_jersery_count,t2_jersey_count)

#######################################################################################################################
#
def all_star_players_in_game(team1, team2, game_date, game_df, player_df):
    game_id_df = game_df.loc[(game_df['date_est'] == game_date) & (game_df['Team'] == team1)]
    game_id = game_id_df['Game_id'][game_id_df.index.get_values()[0]]
    team1_players_df = player_df.loc[(player_df['Game_id'] == game_id) & (player_df['Team'] == team1)]

    game_id_df = game_df.loc[(game_df['date_est'] == game_date) & (game_df['Team'] == team2)]
    game_id = game_id_df['Game_id'][game_id_df.index.get_values()[0]]
    team2_players_df = player_df.loc[(player_df['Game_id'] == game_id) & (player_df['Team'] == team2)]

    month = game_date.split('/')[0]
    target_year = int(game_date.split('/')[-1])
    if int(month) <= 4:
        target_year = target_year - 1
    print(target_year)
    t1_list = [game_id, game_date]
    for index, row in team1_players_df.iterrows():
        if row['ASG_Team'] != 'None':
            t1_list.append((row['Person_id'], row['Name'], row['ASG_Team']))

    t2_list = [game_id, game_date]
    for index, row in team2_players_df.iterrows():
        if row['ASG_Team'] != 'None':
            t2_list.append((row['Person_id'], row['Name'], row['ASG_Team']))

    return (t1_list, t2_list)


# test case
player_df = pd.read_csv('Player_Data.csv')
jersey_df = pd.read_csv('Jersey_Sales_Rankings_Data.csv')
game_df = pd.read_csv('Game_Data.csv')
t1_all_star_count, t2_all_star_count = all_star_players_in_game('SAS', 'CHA', '3/21/2016', game_df, player_df)
print(t1_all_star_count, t2_all_star_count)
