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
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
import matplotlib.pyplot as plt


def link_detect(text):
    new_text = []

    for t in text.split(" "):
        if t.startswith('http'):
            return True

    return False

def ml_result():

    df_two=pd.read_pickle("FUll_SAMPLE.pkl")

    df_two['retweet_count']=df_two['public_metrics'].apply(lambda x: x['retweet_count'])
    df_two['reply_count']=df_two['public_metrics'].apply(lambda x: x['reply_count'])
    df_two['like_count']=df_two['public_metrics'].apply(lambda x: x['like_count'])
    df_two['quote_count']=df_two['public_metrics'].apply(lambda x: x['quote_count'])
    df_two['followers_count']=df_two['author'].apply(lambda x: x['public_metrics']['followers_count'])
    df_two['tweet_count']=df_two['author'].apply(lambda x: x['public_metrics']['tweet_count'])
    df_two['contain_link']=df_two['text'].apply(link_detect)
    df_two['length']=df_two['text'].apply(len)
    df_two['core_bot']=((df_two['k_core_degree']>=40).apply(int) + df_two['bot_yes'].apply(int))>1
    df_two['outside_bot']=((df_two['k_core_degree']<=25).apply(int) + df_two['bot_yes'].apply(int))>1



    X = ml_df[['possibly_sensitive', 'k_core_degree', 'retweet_count', 'reply_count','like_count', 'quote_count', 'followers_count', 'tweet_count','contain_link']]
    y = ml_df[['negative']]

    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2.astype(float))
    est2 = est.fit()
    print(est2.summary())
    plt.rc('figure', figsize=(12, 7))
    plt.text(0.01, 0.05, str(est2.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('k_core_only.png')


    X = df_two[['bot_yes','possibly_sensitive', 'k_core_degree', 'retweet_count', 'reply_count','like_count', 'quote_count', 'followers_count', 'tweet_count','contain_link']]
    y = df_two[['negative']]
    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2.astype(float))
    est2 = est.fit()
    print(est2.summary())
    plt.rc('figure', figsize=(12, 7))
    plt.text(0.01, 0.05, str(est2.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('bot_only.png')

    X = df_two[['outside_bot','core_bot','k_core_degree', 'retweet_count', 'reply_count','like_count', 'quote_count', 'followers_count', 'tweet_count','contain_link']]
    y = df_two[['negative']]

    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2.astype(float))
    est2 = est.fit()
    print(est2.summary())
    plt.rc('figure', figsize=(12, 7))
    plt.text(0.01, 0.05, str(est2.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('core_outside_bot.png')
