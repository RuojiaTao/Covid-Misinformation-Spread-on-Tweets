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

def EDA_data():
    all_path=[]
    for i in np.arange(64):
        if i<10:
            all_path.append("data/all_data_split/mydata_0"+str(i+1)+".pkl")
        else:
            all_path.append("data/all_data_split/mydata_"+str(i+1)+".pkl")
    all_path_in=[]
    for i in np.arange(64):
        if i<10:
            all_path_in.append("data/all_data_split/mydata_0"+str(i+1))
        else:
            all_path_in.append("data/all_data_split/mydata_"+str(i+1))


    for link in all_path_in:
        with open(link) as f:
            df = pd.DataFrame(json.loads(line) for line in f)
        df.to_pickle(link+".pkl")


    pattern_link='.*http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.*'
    pattern_re='RT @.*'


    all_values=pd.DataFrame()
    for path in all_path:
        df = pd.read_pickle(path)

        med=df[['author_id']]
        df=0
        med['count']=med['author_id'].apply(lambda x: 1)
        med['count_2']=med['author_id'].apply(lambda x: 1)
        all_values[path]=med.groupby('author_id').sum().groupby('count').count()['count_2']
        print(path)


    all_values.fillna(0).apply(sum,axis=1).to_csv('same_author.csv')
    total_amount=all_values.fillna(0).apply(sum,axis=1).sum()

    P_re=0
    P_url=0
    authors=[]
    for path in all_path:
        print(path)
        all_values=pd.DataFrame()
        df = pd.read_pickle(path)
        all_values=all_values.append(df[['author_id','text','id']])
        series_a=df['text'].str.contains(pattern_re)
        series_b=df['text'].str.contains(pattern_link)
        P_re+=series_a.sum()
        P_url+=series_b.sum()
        authors.append(list(df['author_id']))
        df=0
    P_re=P_re/total_amount
    P_url=P_url/total_amount
    unqiue_author=len(np.unique(authors))

    all_values=pd.DataFrame()
    for path in all_path:
        df = pd.read_pickle(path)
        all_values=all_values.append(df[['author_id','text','id']])
        df=0
    df=all_values
    all_values=0
    ax=df.groupby('author_id').count().groupby('text').count()['id'].plot(title='Tweets by Same Author')
    ax.set_ylabel('number of authors')
    ax.set_xlabel('counts of tweets')
    ax.figure.savefig('same_author.jpg')

    with open('result.txt', 'w') as f:
        f.write('EDA:'+'\n')
        f.write('- the proportion of tweets that contain a URL is '+str(P_url)+'\n')
        f.write('- the number of unique users is '+str(unqiue_author)+'\n')
        f.write('- the proportion of the data that are retweets '+str(P_re)+'\n')
        f.write('\n')


    def extra_link(text):
        pattern='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.findall(pattern,text)

    def check_domain(url_list):
        if url_list:
            try:
                r=requests.head(url_list[0])
                link=r.headers['location']
                domain=urlparse(link).netloc
                return domain
            except:
                try:
                    link=requests.get(url_list[0]).url
                    domain=urlparse(link).netlocA
                    return domain
                except:
                    return ''
        return ''

    count=0
    with open(full_path) as f:
        for line in f:
            load_line=json.loads(line)
            count=count+1
        #    if count<=470315:
        #        continue
            json_record=dict()
            json_record['id']=load_line['id']
            link_list=extra_link(load_line['text'])
            json_record['domain']=check_domain(link_list)
            with open('data/link_data.json','a+', encoding='utf-8') as f:
                json_record = json.dumps(json_record, ensure_ascii=False)
                f.write(json_record + '\n')

    with open(full_path) as f:
        for line in f:
            load_line=json.loads(line)
            json_record=dict()
            json_record['id']=load_line['id']
            link_list=extra_link(load_line['text'])
            json_record['domain']=check_domain(link_list)
            with open('data/link_data.json','a+', encoding='utf-8') as f:
                json_record = json.dumps(json_record, ensure_ascii=False)
                f.write(json_record + '\n')


    misinfo=pd.read_csv('data/iffy.csv')
    domains=misinfo['Domain']

    misinfor_tweets=link_df['domain'].apply(lambda x: x in list(domains))
    proportion_mis=misinfor_tweets.mean()

    fact=['politifact.com', 'factcheck.org', 'washingtonpost.com', 'snopes.com', 'reporterslab.org', 'factcheck.org', 'flackcheck.org', 'mediabiasfactcheck.com', 'npr.org']
    proportion_fact=link_df['domain'].apply(lambda x: x in fact).mean()
    proportion_request=len(link_df[link_df['domain'].apply(lambda x: x !='')])/len(link_df)
    with open('result.txt', 'a') as f:
        f.write('Misinformation:'+'\n')
        f.write('- the proportion of tweets that have a link can be requested is '+str(proportion_request)+'\n')
        f.write('- the proportion of misinformation is '+str(proportion_mis)+'\n')
        f.write('- the proportion of fact check is '+str(proportion_fact)+'\n')
        f.write('\n')
