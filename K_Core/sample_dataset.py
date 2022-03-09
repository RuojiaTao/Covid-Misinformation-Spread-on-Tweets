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

def sample_data():
    all_path=[]
    for i in np.arange(64):
        if i<9:
            all_path.append("data/all_data_split/k_core_tweet_0"+str(i+1)+".pkl")
        else:
            all_path.append("data/all_data_split/k_core_tweet_"+str(i+1)+".pkl")

    df_sample=pd.DataFrame()
    df_sample

    for path in all_path:
        df_s = pd.read_pickle(path)
        df_sample=df_sample.append(df_s.sample(n=1000))
        df_s=0
        print(path)


    df_sample.to_pickle('data/all_data_split/sample.pkl')
