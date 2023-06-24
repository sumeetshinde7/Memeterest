# -*- coding: utf-8 -*-
"""

@author: Sumeet
"""

from reddit_scrape import get_reddit_data
from chive_scrape import get_chive_data
from memedroid_scrape import get_memedroid_data
import pandas as pd
import numpy as np


### get data from r/memes (subreddit)
reddit_df_1 = get_reddit_data(limit=100,
                            post_type='hot',
                            subreddit='memes')

### get data from r/MemeEconomy (subreddit)
reddit_df_2 = get_reddit_data(limit=100,
                            post_type='hot',
                            subreddit='MemeEconomy')

### get data from chive.com
chive_df = get_chive_data()

### get data from memedroid.com
memedroid_df = get_memedroid_data()

### get data from memegenerator.net using CSV file
memegenerator_df = pd.read_csv('memegenerator.csv')
memegenerator_df['score'] = memegenerator_df['upvotes'] - memegenerator_df['downvotes']
print(memegenerator_df.head())


### integrate data from all websites
df_all = pd.concat([reddit_df_1,
                   reddit_df_2,
                   # chive_df,
                   memegenerator_df,
                   memedroid_df],ignore_index=True)


### get memes with highest score
df_sorted = df_all.sort_values(by=['score'],ascending=False)

### print top 5 memes
print(df_sorted.head())
