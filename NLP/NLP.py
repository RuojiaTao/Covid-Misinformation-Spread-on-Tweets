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


from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")


def preprocess(text):
    new_text = []

    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def NLP_sentiment(processed_text):

    try:
        encoded_input = tokenizer(processed_text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        return scores
    except:
        return np.array([0, 0, 0])

def sentiment_check():
    df_sample = pd.read_pickle('data/all_data_split/sample.pkl')
    all_text=df_sample['text'].apply(preprocess)
    all_scores=[]
    for processed_text in all_text:
        try:
            all_scores.append(NLP_sentiment(processed_text))
        except:
            all_scores.append(np.array([0, 0, 0]))

    negative=[]
    neutral=[]
    postive=[]


    for each in all_scores:
        negative.append(each[0])
        neutral.append(each[1])
        postive.append(each[2])

    df_sample['all_sentiment']=all_scores
    df_sample['postive']=postive
    df_sample['neutral']=neutral
    df_sample['negative']=negative

    df_sample.to_pickle('data/all_data_split/sentiment.pkl')

    fig, ax = plt.subplots(figsize =(10, 5))
    ax=df_sample['postive'].hist()
    ax.set_title('The Sampled Postive Score of Tweets')
    ax.set_xlabel('How Postive the Tweet is')
    ax.set_ylabel('Number of Users')
    fig.savefig('Sampled Postive Score.jpg')

    fig, ax = plt.subplots(figsize =(10, 5))
    ax=df_sample['negative'].hist()
    ax.set_title('The Sampled Negative Score of Tweets')
    ax.set_xlabel('How Negative the Tweet is')
    ax.set_ylabel('Number of Users')
    fig.savefig('Sampled Negative Score.jpg')

    fig, ax = plt.subplots(figsize =(10, 5))
    ax=df_sample['neutral'].hist()
    ax.set_title('The Sampled Neutral Score of Tweets')
    ax.set_xlabel('How Neutral the Tweet is')
    ax.set_ylabel('Number of Users')
    fig.savefig('Sampled Neutral Score.jpg')

    ax=df_sample.groupby('k_core_degree').mean()[['postive','negative','neutral']].plot(figsize =(12, 7), color=['orange','blue','green'])
    ax.set_title('The Change of User Sentiment with K Core Degree')
    ax.set_xlabel('K Core Degrees')
    ax.set_ylabel('Scores')
    fig = ax.get_figure()
    fig.savefig('Sentiment change with K Core Degree.jpg')

    df_sample.groupby('k_core_degree').mean()[['postive','negative','neutral']].to_csv('data/all_data_split/mean_sentiment.csv')
