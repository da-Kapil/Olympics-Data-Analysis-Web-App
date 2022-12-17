import pandas as pd
import numpy as np


def preprocess(df, region_df):
    # Filtering for Summer Olympics
    df = df[df['Season'] == 'Summer']
    # Merging with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # Droping duplicates
    df.drop_duplicates(inplace=True)
    # One hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df