import gzip
import shutil
import os
import wget
import csv
import linecache
from shutil import copyfile
import ipywidgets as widgets
import numpy as np
import pandas as pd
import tweepy
import json_lines
import re
import json
from urllib.parse import urlparse
import requests
import networkx as nx
from scipy.special import softmax
from matplotlib import pyplot as plt


def merge_bot():

    all_data=list()
    with open('bot_user.json') as fh:
        line = fh.readline()
        while line:
            row=json.loads(line)
            if row:
                all_data.append(row)
            line = fh.readline()

    botometer_result=pd.DataFrame.from_dict(all_data)

    botometer_result['author_id']=botometer_result['user'].apply(lambda x: x['user_data']['id_str'])
    botometer_result['cap_english']=botometer_result['cap'].apply(lambda x: x['english'])
    botometer_result['result_english']=botometer_result['raw_scores'].apply(lambda x: x['english']['overall'])
    botometer_result['bot_yes']=botometer_result['cap_english']<=botometer_result['result_english']

    whole_ds=pd.read_pickle('data/all_data_split/sentiment.pkl')
    df_two = pd.merge(botometer_result, whole_ds,  how='left', left_on=['author_id'], right_on = ['author_id'])

    ax=df_two.groupby('k_core_degree').mean()[['bot_yes']].plot()
    ax.set_xlabel('K Core Degrees')
    ax.set_ylabel('Percentage of Bots')
    fig = ax.get_figure()
    fig.savefig('k_core_bot_plot.jpg', bbox_inches='tight', dpi=150)

    cleaned=df_two.groupby('k_core_degree').mean()[['bot_yes']].reset_index()
    ax=cleaned.plot.scatter(x='k_core_degree',y='bot_yes')
    ax.set_xlabel('K Core Degrees')
    ax.set_ylabel('Percentage of Bots')
    fig = ax.get_figure()
    fig.savefig('k_core_bot_scatter.jpg', bbox_inches='tight', dpi=150)

    df_two.to_pickle("FUll_SAMPLE.pkl")
    df_two.groupby('k_core_degree').mean()[['bot_yes']].to_csv('percentage_bot_degrees.csv')
