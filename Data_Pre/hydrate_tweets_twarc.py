import gzip
import shutil
import os
import wget
import csv
import linecache
from shutil import copyfile
import numpy as np
import pandas as pd
import tweepy
from twarc import Twarc
import json
from datetime import date, timedelta
from twarc import Twarc2, expansions


CONSUMER_KEY = "" #@param {type:"string"}
CONSUMER_SECRET_KEY = "" #@param {type:"string"}
ACCESS_TOKEN_KEY = "" #@param {type:"string"}
ACCESS_TOKEN_SECRET_KEY = "" #@param {type:"string"}
bearer_token=''
client = Twarc2(CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET_KEY,bearer_token)

def read_tweet(tweet_ids):
    # List of Tweet IDs you want to lookup
    # The tweet_lookup function allows
    missing_number=0
    lookup = client.tweet_lookup(tweet_ids=tweet_ids)
    for page in lookup:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        for tweet in result:
            # Here we are printing the full Tweet object JSON to the console
            with open('data/all_data_full.json','a+', encoding='utf-8') as f:
                missing_number+=1
                json_record = json.dumps(tweet)
                f.write(json_record + '\n')
    return missing_number

def hydrate():
    start_date = date(2020, 3, 22)#3/22
    end_date = date(2022, 1, 1)#10/10
    delta = timedelta(days=1)
    problem_list=[]
    missing_each_day={}
    while start_date <= end_date:
        missing_num=0
        try:
            dataset_URL = "https://github.com/thepanacealab/covid19_twitter/blob/master/dailies/"+str(start_date)+"/"+str(start_date)+"-dataset.tsv.gz?raw=true" #@param {type:"string"}

            #Downloads the dataset (compressed in a GZ format)
            #!wget dataset_URL -O clean-dataset.tsv.gz
            wget.download(dataset_URL, out='clean-dataset.tsv.gz')

            #Unzips the dataset and gets the TSV dataset
            with gzip.open('clean-dataset.tsv.gz', 'rb') as f_in:
                with open('clean-dataset.tsv', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            #Deletes the compressed GZ file
            os.unlink("clean-dataset.tsv.gz")

            df = pd.read_csv('clean-dataset.tsv',sep="\t")



            list_ids=df.sample(frac=0.025)['tweet_id'] #frac=0.0025

            tweets_hydrated=0

            tweets_hydrated = read_tweet(list_ids)
            missing_each_day[str(start_date)]=len(list_ids)-tweets_hydrated



            print("S "+str(start_date)+" "+str(tweets_hydrated)+"/"+str(len(list_ids)))
            start_date += delta
        except:
            print("Failed! "+str(start_date))
            problem_list.append(str(start_date))
            pass
    with open('data/error_data.json','a+', encoding='utf-8') as f:
        for line in problem_list:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    with open('data/missing_data.json','a+', encoding='utf-8') as f:
        for line in missing_each_day:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')

    os.system('cmd /c "split -l 350000 all_data_full.json --numeric-suffixes --suffix-length=2 mydata mydata_"')
