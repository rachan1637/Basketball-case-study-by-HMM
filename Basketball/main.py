import os
import pandas as pd
from preoprocessor import GameDataPreprocessor

if __name__ == "__main__":
    mv_data_path = "/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/CHA-TOR.csv"
    event_data_path = "/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/CHA-TOR-events.csv"

    preprocessor = GameDataPreprocessor(mv_data_path, event_data_path)
    df = preprocessor.preprocess_single_event(28)
    df.to_csv("/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/event28_3pt.csv", 
            float_format = "%.3f")

    # df = preprocessor.replace_names(28)
    # df.to_csv("/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/event28_3pt_player.csv", 
    #         float_format = "%.3f")
