# -*- coding: utf-8 -*-
"""Revv_web_scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h5OjTfoT3fvYlNkzHMU29HnzzSbYGDn7
"""

pip install google-play-scraper

from google_play_scraper import app

import pandas as pd

import numpy as np

from google_play_scraper import Sort, reviews_all

us_reviews = reviews_all(
    'com.selfdrive',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='in', # defaults to 'us'
    #sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
)

df2 = pd.DataFrame(np.array(us_reviews),columns=['review'])

df2 = df2.join(pd.DataFrame(df2.pop('review').tolist()))

df2.shape

df2.head()