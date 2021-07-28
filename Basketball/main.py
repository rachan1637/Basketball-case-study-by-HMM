import os
import pandas as pd
from preoprocessor import GameDataPreprocessor

if __name__ == "__main__":
    mv_data_path = "/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/CHA-TOR.csv"
    event_data_path = "/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/CHA-TOR-events.csv"

    preprocessor = GameDataPreprocessor(mv_data_path, event_data_path)
    df = preprocessor.preprocess_single_event(1)
    df.to_csv("/Users/yhschan/Desktop/sports analytics/Basketball-case-study-by-HMM/basketball/data/event1.csv", 
            float_format = "%.3f")
