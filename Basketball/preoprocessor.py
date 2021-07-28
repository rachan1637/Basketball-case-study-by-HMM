import pandas as pd
import math

class GameDataPreprocessor():
    def __init__(self, mv_data_path, event_data_path):
        self.store_information(mv_data_path, event_data_path)

    def replace_names(self, event_id):
        data = self.data

        event_data = data[data['event_id'] == event_id]
        event_data = event_data.replace({"player_id": self.player_dict,
                                        "team_id": self.team_dict})
        event_data = event_data.sort_values(by = 'game_clock', ascending = False)
        event_data.index = pd.RangeIndex(len(event_data.index))
        event_data.index = range(len(event_data.index))

        return event_data
    
    def calculate_speed(self, event_data):
        inital_speed = [0.0 for i in range(len(event_data))]
        event_data['speed'] = inital_speed

        time_step = event_data['game_clock'].value_counts().index

        for index, row in event_data.iterrows():
            time = row['game_clock']
            player = row['player_id']
            curr_loc_x, curr_loc_y = row['x_loc_original'], row['y_loc_original']
            
            if round(time + 0.04, 2) in time_step:
                    prev_row = event_data.loc[(event_data['game_clock'] == round(time + 0.04, 2)) & (event_data['player_id'] == player)]
                    prev_loc_x, prev_loc_y = prev_row['x_loc_original'], prev_row['y_loc_original']
                    speed = math.sqrt(
                                    (curr_loc_x - prev_loc_x)**2 + 
                                    (curr_loc_y - prev_loc_y)**2
                                    ) / 0.04
                    event_data.at[index, 'speed'] = speed
        return event_data          

    def preprocess_events(self):
        for event_id in self.event_ids:
            # This is team-based, which means each time step has 2 rows in total (1 row for each team), containing 5 players and ball for each row.
            single_event_data = self.preprocess_single_event(event_id)

        return

    def preprocess_single_event(self, event_id):
        event_data = self.replace_names(event_id)
        event_data = self.calculate_speed(event_data)
        return event_data
        
        # data = self.data
        # event_data = data[data['event_id'] == event_id]
    #     cleaned_event_data = None
    #     time_step = event_data['game_clock'].value_counts().index
    #     for time in time_step:
    #         # The dataframe here is row based, i.e. 5 players are on each row
    #         time_t_data = event_data[event_data['game_clock'] == time]
    #         time_t_team1_data_sep = time_t_data[time_t_data['team_id'] == self.team1]
    #         time_t_team2_data_sep = time_t_data[time_t_data['team_id'] == self.team2]

    #         # Get the information of ball
    #         time_t_ball_data = time_t_data[time_t_data['team_id'] == self.ball]
    #         ball_x_loc = float(time_t_ball_data['x_loc_original'])
    #         ball_y_loc = float(time_t_ball_data['y_loc_original'])

    #         # The dataframe here combine all players' data at time t into one row
    #         time_t_data = self.create_team_data_at_time_t(time_t_team1_data_sep, time_t_team2_data_sep, event_id, self.team1, self.team2, time, ball_x_loc, ball_y_loc)

    #         if cleaned_event_data is None:
    #             cleaned_event_data = time_t_data
    #         else:
    #             cleaned_event_data = pd.concat([cleaned_event_data, time_t_data], ignore_index = True)
        
    #     cleaned_event_data = cleaned_event_data.replace({'team1_player1': self.player_dict, 
    #                                                     'team1_player2': self.player_dict, 
    #                                                     'team1_player3': self.player_dict, 
    #                                                     'team1_player4': self.player_dict, 
    #                                                     'team1_player5': self.player_dict,
    #                                                     'team2_player1': self.player_dict, 
    #                                                     'team2_player2': self.player_dict, 
    #                                                     'team2_player3': self.player_dict, 
    #                                                     'team2_player4': self.player_dict, 
    #                                                     'team2_player5': self.player_dict,
    #                                                     'team1_id': self.team_dict,
    #                                                     'team2_id': self.team_dict})
        
    #     cleaned_event_data = cleaned_event_data.sort_values(by = 'game_clock', ascending = False)
    #     cleaned_event_data.index = pd.RangeIndex(len(cleaned_event_data.index))
    #     cleaned_event_data.index = range(len(cleaned_event_data.index))

    #     cleaned_event_data = self.preoprocess_speed(cleaned_event_data)

    #     return cleaned_event_data

    # def preoprocess_speed(self, cleaned_event_data):
    #     # Divide by two because each time step gets 2 team data, so it should be an even number
    #     n_timestep = len(cleaned_event_data)

    #     ball_speed_list = []
    #     player_speed_list_nested = [[], [], [], [], [], [], [], [], [], []]

    #     for index in range(n_timestep):
    #         # Set value to 0 if it is the beginning of the event
    #         if index == 0:
    #             ball_speed_list += [0]
    #             for j in range(1, 11):
    #                 player_speed_list_nested[j-1] += [0] 
    #             continue
    #         # Prepare previous time step and current time step data
    #         pre_time_step_data = cleaned_event_data.iloc[index-1]
    #         cur_time_step_data = cleaned_event_data.iloc[index]

    #         time_diff = pre_time_step_data['game_clock'] - cur_time_step_data['game_clock']

    #         # Calculate ball speed
    #         ball_speed = math.sqrt(
    #                                 (pre_time_step_data['ball_x_loc'] - cur_time_step_data['ball_x_loc'])**2 + 
    #                                 (pre_time_step_data['ball_y_loc'] - cur_time_step_data['ball_y_loc'])**2
    #                                 ) / time_diff
    #         ball_speed_list += [ball_speed]
    #         assert ball_speed >= 0

    #         # Calculate player speed
    #         for i in range(1, 3):
    #             for j in range(1, 6):
    #                 x_name, y_name = f"team{i}_player{j}_x_loc", f"team{i}_player{j}_y_loc"
    #                 player_speed = math.sqrt(
    #                                     (pre_time_step_data[x_name] - cur_time_step_data[x_name])**2 + 
    #                                     (pre_time_step_data[y_name] - cur_time_step_data[y_name])**2
    #                                     ) / time_diff

    #                 assert player_speed >= 0
    #                 player_speed_list_nested[(i-1)*5 + j-1] += [player_speed] 

    #     # Add all speed data to the original cleaned dataset
    #     # cleaned_event_data['ball_speed'] = ball_speed_list
    #     # for i in range(1, 3):
    #     #     for j in range(1, 6):
    #     #         speed_name = f"team{i}_player{j}_speed"
    #     #         cleaned_event_data[speed_name] = player_speed_list_nested[(i-1)*5 + j-1]
    #     cleaned_event_data['speed'] = ball_speed_list

    #     return cleaned_event_data        

    # def create_team_data_at_time_t(self, time_t1_team_data, time_t2_team_data, event_id, team1_id, team2_id, time, ball_x_loc, ball_y_loc):
    #     column_names = ['event_id', 'team1_id', 'team2_id', 'game_clock', 'ball_x_loc', 'ball_y_loc']
    #     row_data = [event_id, team1_id, team2_id, time, ball_x_loc, ball_y_loc]
    #     time_t_team_data_list = [time_t1_team_data, time_t2_team_data]
    #     for j in range(1, 3):
    #         time_t_team_data = time_t_team_data_list[j-1]
    #         player_ids = list(time_t_team_data['player_id'].value_counts().index)
    #         for i in range(1, len(player_ids) + 1):
    #             player_id = int(player_ids[i-1])
    #             x_loc = float(time_t_team_data[time_t_team_data['player_id'] == player_id]['x_loc_original'])
    #             y_loc = float(time_t_team_data[time_t_team_data['player_id'] == player_id]['y_loc_original'])
                
    #             column_player = f"team{j}_player{i}"
    #             column_x = f"team{j}_player{i}_x_loc"
    #             column_y = f"team{j}_player{i}_y_loc"
                
    #             column_names += [column_player, column_x, column_y]
    #             row_data += [player_id, x_loc, y_loc]
    
    #     new_t_data = pd.DataFrame(columns = column_names)
    #     new_t_data.loc[0] = row_data

    #     return new_t_data
            

    def store_information(self, mv_data_path, event_data_path):
        # Store the pandas DataFrame
        self.data = pd.read_csv(mv_data_path)
        self.data_q1 = self.data[self.data['quarter'] == 1]
        self.data_q2 = self.data[self.data['quarter'] == 2]
        self.data_q3 = self.data[self.data['quarter'] == 3]
        self.data_q4 = self.data[self.data['quarter'] == 4]

        # Store the information of player_id and name
        self.event_data = pd.read_csv(event_data_path)
        player1 = set(self.event_data[['PLAYER1_ID', 'PLAYER1_NAME']].value_counts().index)
        player2 = set(self.event_data[['PLAYER2_ID', 'PLAYER2_NAME']].value_counts().index)
        player3 = set(self.event_data[['PLAYER3_ID', 'PLAYER3_NAME']].value_counts().index)
        player1.update(player2)
        player1.update(player3)
        players = list(player1)

        self.player_dict = {}
        for i in range(len(player1)):
            player_id, player_name = players[i]
            self.player_dict[player_id] = player_name
        self.player_dict[-1] = 'ball'

        # Store the information of team_id and name
        team_id_list = list(self.data['team_id'].value_counts().index)
        team_id_list.remove(-1)

        self.team1 = team_id_list[0]
        self.team2 = team_id_list[1]
        self.ball = -1

        team = list(self.event_data[['PLAYER1_TEAM_ID', 'PLAYER1_TEAM_ABBREVIATION']].value_counts().index)
        self.team_dict = {}
        self.team_dict[team[0][0]] = team[0][1]
        self.team_dict[team[1][0]] = team[1][1]
        self.team_dict[-1] = 'ball'

        #Store the information of event_id
        self.event_ids = list(self.data['event_id'].value_counts().index)