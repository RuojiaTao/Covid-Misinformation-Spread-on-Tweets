import gzip
import shutil
import os
import wget
import csv
from shutil import copyfile
import numpy as np
import pandas as pd
import tweepy
from twarc import Twarc
from datetime import date, timedelta
from twarc import Twarc2, expansions
import re
import json
from urllib.parse import urlparse
import requests
import sys
import networkx as nx

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import pickle
import botometer


CONSUMER_KEY = "" #@param {type:"string"}
CONSUMER_SECRET_KEY = "" #@param {type:"string"}
ACCESS_TOKEN_KEY = "" #@param {type:"string"}
ACCESS_TOKEN_SECRET_KEY = "" #@param {type:"string"}
bearer_token=''
client = Twarc2(CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET_KEY,bearer_token)


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

    def cluster_ids(x):
        if 'author_id' in x['referenced_tweets'][0].keys():
            return (x['author_id'],x['referenced_tweets'][0]['author_id'])
        else:
            return False

def main(targets):


    if 'hydrate' in targets:

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

        start_date = date(2020, 3, 22)
        end_date = date(2021, 4, 1)
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



                list_ids=df.sample(frac=0.0025)['tweet_id'] #frac=0.0025

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


        os.system('cmd /c "split -l 350000 huge_json_file.jl"')

        with open('data/all_data_split/xaa') as f:
            df_xaa = pd.DataFrame(json.loads(line) for line in f)
        df_xaa.to_pickle("data/all_data_split/xaa.pkl")
        df_xaa=0
        with open('data/all_data_split/xab') as f:
            df_xab = pd.DataFrame(json.loads(line) for line in f)
        df_xab.to_pickle("data/all_data_split/xab.pkl")
        df_xab=0
        with open('data/all_data_split/xac') as f:
            df_xac = pd.DataFrame(json.loads(line) for line in f)
        df_xac.to_pickle("data/all_data_split/xac.pkl")
        df_xac=0
        with open('data/all_data_split/xad') as f:
            df_xad = pd.DataFrame(json.loads(line) for line in f)
        df_xad.to_pickle("data/all_data_split/xad.pkl")
        df_xad=0
        with open('data/all_data_split/xae') as f:
            df_xae = pd.DataFrame(json.loads(line) for line in f)
        df_xae.to_pickle("data/all_data_split/xae.pkl")
        df_xae=0
        with open('data/all_data_split/xaf') as f:
            df_xaf = pd.DataFrame(json.loads(line) for line in f)
        df_xaf.to_pickle("data/all_data_split/xaf.pkl")
        df_xaf=0
        #Load Data:
        all_values=pd.DataFrame()
        for path in all_path:
            print(path)
            df = pd.read_pickle(path)
            all_values=all_values.append(df[['author_id','text','id']])
            df=0
        df=all_values
        all_values=0

    if 'test' in targets:
        targets=["EDA",'misinfo','top_tweets','k_core','NLP','Bot_detection']
        df=pd.read_pickle('test/testdata/test.pkl')
        all_path = ['all_path']
    #EDA: find link/RT/ check number of unqiue author
    if 'EDA' in targets:
        print('EDA Start')
        pattern_link='.*http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.*'
        pattern_re='RT @.*'
        series_a=df['text'].str.contains(pattern_re)
        series_b=df['text'].str.contains(pattern_link)
        P_re=series_a.mean()
        P_url=series_b.mean()
        unqiue_author=len(df['author_id'].unique())

        with open('result.txt', 'w') as f:
            f.write('EDA:'+'\n')
            f.write('- the proportion of tweets that contain a URL is '+str(P_url)+'\n')
            f.write('- the number of unique users is '+str(unqiue_author)+'\n')
            f.write('- the proportion of the data that are retweets '+str(P_re)+'\n')
            f.write('\n')
        ax=df.groupby('author_id').count().groupby('text').count()['id'].plot(title='Tweets by Same Author')
        ax.set_ylabel('number of authors')
        ax.set_xlabel('counts of tweets')
        ax.figure.savefig('same_author.jpg')

    #checked misinformation
    if 'misinfo' in targets:
        print('misinfo Start')
        # request and extra link
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

    #find the top popular tweets
    if 'top_tweets' in targets:
        print('top_tweets Start')
        all_values=pd.DataFrame()
        for path in all_path:
            print(path)
            df = pd.read_pickle(path)
            all_values=all_values.append(df[['author_id','text','id','public_metrics']])
            df=0
        df=all_values
        df['retweet']=df['public_metrics'].apply(lambda x: x['retweet_count'])
        most_popular=df.sort_values('retweet').head(10000)
        most_popular.to_csv('most_popular.csv')
        #most popular tweets:
        top_pro=len(top_links[top_links.apply(lambda x: x !='')])/len(top_links)
        misinfor_tweets=top_links.apply(lambda x: x in list(domains))
        proportion_top_mis=misinfor_tweets.mean()

        fact=['politifact.com', 'factcheck.org', 'washingtonpost.com', 'snopes.com', 'reporterslab.org', 'factcheck.org', 'flackcheck.org', 'mediabiasfactcheck.com', 'npr.org']
        proportion_top_fact=top_links.apply(lambda x: x in fact).mean()
        with open('result.txt', 'a') as f:
            f.write('Misinformation:'+'\n')
            f.write('- for top 10000 popular tweets the proportion of tweets that have a link can be requested is '+str(top_pro)+'\n')
            f.write('- for top 10000 popular tweets the proportion of misinformation is '+str(proportion_top_mis)+'\n')
            f.write('- for top 10000 popular tweets the proportion of fact check is '+str(proportion_top_fact)+'\n')
            f.write('\n')
    return

    #find the k core tweets
    if 'k_core' in targets:
        G = nx.DiGraph()
        for path in all_path:
            print(path)
            df_s = pd.read_pickle(path)
            df_s=df_s[['author_id','text','id','referenced_tweets']]
            df_s=pd.merge(link_df,df_s)
            print('merge')
            exist_RT=df_s[df_s['referenced_tweets'].notna()]
            edges=exist_RT.apply(lambda x: cluster_ids(x)  , axis=1)
            print('edge')
            G.add_edges_from(edges[edges != False])
            #df_s=0
            edges=0
            exist_RT=0



        G.remove_edges_from(nx.selfloop_edges(G))
        core_num=nx.algorithms.core.core_number(G)
        max_core=max(list(core_num.values()))
        num_edge=G.number_of_edges()

        df_s['degree']=df_s['author_id'].apply(lambda x: core_num[x] if x in core_num.keys() else 0)
        df_s['misinfor_tweets']=df_s['domain'].apply(lambda x: x in list(domains))

        fact=['politifact.com', 'factcheck.org', 'washingtonpost.com', 'snopes.com', 'reporterslab.org', 'factcheck.org', 'flackcheck.org', 'mediabiasfactcheck.com', 'npr.org']
        df_s['fact_tweets']=df_s['domain'].apply(lambda x: x in fact)
        ax=df_s.groupby('degree').mean()['misinfor_tweets'].plot()
        ax.figure.savefig('spead_mis.jpg')
        ax=df_s.groupby('degree').mean()['fact_tweets'].plot()
        ax.figure.savefig('spead_fact.jpg')


        average_tweet.append(df_s[df_s['degree']==0].groupby('author_id').count()['text'].mean())
        average_tweet.append(df_s[df_s['degree']==1].groupby('author_id').count()['text'].mean())
        average_tweet.append(df_s[df_s['degree']==2].groupby('author_id').count()['text'].mean())
        average_tweet.append(df_s[df_s['degree']==3].groupby('author_id').count()['text'].mean())
        average_tweet.append(df_s[df_s['degree']==4].groupby('author_id').count()['text'].mean())
        average_tweet.append(df_s[df_s['degree']==5].groupby('author_id').count()['text'].mean())
        ax=pd.DataFrame(average_tweet).plot.bar()
        ax.figure.savefig('average_tweets.jpg')
        with open('result.txt', 'a') as f:
            f.write('Misinformation:'+'\n')
            f.write('- the maximum degree of all the nodes is '+str(max_core)+'\n')
            f.write('- the number of edges in this graph is '+str(num_edge)+'\n')
            f.write('\n')

    if 'NLP' in targets:
        print('NLP Start')
        def preprocess(text):
            new_text = []

            for t in text.split(" "):
                t = '@user' if t.startswith('@') and len(t) > 1 else t
                t = 'http' if t.startswith('http') else t
                new_text.append(t)
            return " ".join(new_text)
        all_values=pd.DataFrame()
        tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        for path in all_path:
            print(path)
            df = pd.read_pickle(path)
            all_values=all_values.append(df[['text','id']])
            df=0
        all_text=all_values['text'].apply(preprocess)
        all_scores=[]
        for processed_text in all_text:
            try:
                all_scores.append(nlp_text(processed_text))
            except:
                all_scores.append(np.array([0, 0, 0]))
        np.savetxt("array_all.txt", all_scores)
        f = open('array.txt', 'r+')
        all_scores=[]
        for line in inf.readlines():
            all_scores.append(line)
        f.close()
        positive=[]
        for i in all_scores:
            datas=i.split(" ")
            positive.append(float(datas[0])-float(datas[2]))
        ax=pd.Series(positive).hist()
        ax.set_title('The Overall Postive Score of Tweets')
        ax.set_xlabel('How Postive the Tweet is')
        ax.set_ylabel('Number of Users')
        ax.figure.savefig('NLP_emotion_spread.jpg')


    if 'Bot_detection' in targets:
        print('Bot_detection Start')
        def bot_detection():
            """
            This function examine the
            """
            # https://github.com/IUNetSci/botometer-python

            data = pd.read_csv('small_dataset.csv')

            rapidapi_key = ""
            twitter_app_auth = {
                'consumer_key': '',
                'consumer_secret': '',
                'access_token': '',
                'access_token_secret': '',

              }

            bom = botometer.Botometer(wait_on_ratelimit=True,
                                      rapidapi_key=rapidapi_key,
                                      **twitter_app_auth)

            bot_user = 0
            total_user = 0
            missing_user = 0
            error_message = {}
            error_count = {}

            for user in data['author_id']:
                total_user += 1
                result = None
                # Check a single account by id
                try:
                    result = bom.check_account(user)
                    if (result['raw_scores']['english']['overall'] >= result['cap']['english']
                        or result['raw_scores']['universal']['overall'] >= result['cap']['universal']):
                        bot_user += 1
                except Exception as e:
                    missing_user += 1
                    print(e)

                with open('bot_user.json', 'a+', encoding='utf-8') as f:
                    json_record = json.dumps(result)
                    f.write(json_record+'\n')

                print('bot user ' + str(bot_user))
                print('total_user ' + str(total_user))
                print('missing_user ' + str(missing_user))
            return error_message, error_count

        def save_error(error_message, error_count):
            message_file = open("error_message.pkl", "wb")
            pickle.dump(error_message, message_file)
            message_file.close()

            count_file = open("error_count.pkl", "wb")
            pickle.dump(error_count, count_file)
            count_file.close()

        error_message, error_count = bot_detection()
        save_error(error_message, error_count)


if __name__ == '__main__':
    # run via:
    # python run.py EDA misinfo top_tweets
    targets = sys.argv[1:]
    main(targets)
