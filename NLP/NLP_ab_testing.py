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
import scipy.stats as stats
import statsmodels.stats.api as sms
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

def ab_testing():
    df_sample=pd.read_pickle('data/all_data_split/sentiment.pkl')
    df_sample.to_csv('small_dataset.csv')
    ab_result=dict()

    for i in np.arange(60):
        i=int(i)
        ab_result[i]=dict()
        for j in np.arange(60):
            j=int(j)
            ab_result[i][j]=dict()
            zero=df_sample[df_sample['k_core_degree']==i]['negative']
            other=df_sample[df_sample['k_core_degree']==j]['negative']
            result=stats.ttest_ind(zero, other, equal_var=False)
            ab_result[i][j]['statistic']=result[0]
            ab_result[i][j]['pvalue']=result[1]
            ab_result[i][j]['result_005']=int(result[1]<0.005)
            ab_result[i][j]['result_001']=int(result[1]<0.001)

    with open('ab_testing.json', 'a+', encoding='utf-8') as f:
                json_record = json.dumps(ab_result)
                f.write(json_record+'\n')

    x=[]
    y=[]
    value=[]
    for i in np.arange(60):
        for j in np.arange(60):
            x.append(i)
            y.append(j)
            value.append(ab_result[i][j]['result_005'])

    tf_df=pd.DataFrame()
    tf_df['k_core_degree_1']=np.array(x)
    tf_df['k_core_degree_2']=np.array(y)
    tf_df['result']=np.array(value)

    fig, ax = plt.subplots()
    tf_df.plot(kind='scatter',x='k_core_degree_1',y='k_core_degree_2',c='result',colormap='Blues',ax=ax)
    ax.set_xlabel('K Core Degrees for Group 1')
    ax.set_ylabel('K Core Degrees for Group 2')
    plt.savefig('ab plot.jpg', bbox_inches='tight', dpi=150)
