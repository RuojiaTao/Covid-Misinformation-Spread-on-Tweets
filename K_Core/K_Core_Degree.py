import os

import gzip
import shutil
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
import matplotlib.pyplot as plt



def cluster_ids(x):
    if 'author_id' in x['referenced_tweets'][0].keys():
        return (x['author_id'],x['referenced_tweets'][0]['author_id'])
    else:
        return False

def find_degree(key_id):
    try:
        return data[key_id]
    except:
        return 0


def find_k_core():
    all_path=[]
    for i in np.arange(64):
        if i<9:
            all_path.append("data/all_data_split/tweet_0"+str(i+1)+".pkl")
        else:
            all_path.append("data/all_data_split/tweet_"+str(i+1)+".pkl")


    G = nx.DiGraph()
    for path in all_path:
        print(path)
        df_s = pd.read_pickle(path)
        df_s=df_s[['author_id','text','id','referenced_tweets']]
        exist_RT=df_s[df_s['referenced_tweets'].notna()]
        edges=exist_RT.apply(lambda x: cluster_ids(x)  , axis=1)
        print('edge')
        G.add_edges_from(edges[edges != False])
        G.remove_edges_from(nx.selfloop_edges(G))
        df_s=0
        edges=0
        exist_RT=0

    core_num=nx.algorithms.core.core_number(G)
    with open('k_core.json', 'w') as fp:
        json.dump(core_num, fp)


def assign_k_core():
    with open('k_core.json', 'r') as fp:
        data = json.load(fp)

    all_path=[]
    for i in np.arange(64):
        if i<9:
            all_path.append("data/all_data_split/tweet_0"+str(i+1)+".pkl")
        else:
            all_path.append("data/all_data_split/tweet_"+str(i+1)+".pkl")


    for path in all_path:
        df_s = pd.read_pickle(path)
        df_s['k_core_degree']=df_s['author_id'].apply(find_degree)
        store_path=path[:-12]+str('k_core_')+path[-12:]
        print(store_path)
        df_s.to_pickle(store_path)



def k_core_vis():
    with open('k_core.json', 'r') as fp:
        data = json.load(fp)
        all_values=np.array(list(data.values()))
    i,j=np.unique(all_values, return_counts=True)
    k_core_count=pd.DataFrame()
    k_core_count['degrees']=i
    k_core_count['counts']=j
    k_core_count.to_csv('k_core_degree_count.csv')
    fig, ax = plt.subplots(figsize =(10, 5))
    ax.hist(all_values, bins=np.arange(62))
    ax.set_title('The Spread of K-Core Degree')
    ax.set_xlabel('K-Core Degree')
    ax.set_ylabel('Number of Users')
    fig.savefig('k core spread plot.jpg')
