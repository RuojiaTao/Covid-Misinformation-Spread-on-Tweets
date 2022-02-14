# Covid-Misinformation-Spread-on-Tweets
Analyze the misinformation about covid spreading in tweet

Our website: https://ruojiatao.github.io/Covid-Misinformation-Spread-on-Tweets/

The run.py file include our main data and build up by different parts:

 - 'hydrate' for hydartion the data from twitter with API
 - 'EDA' for explore the raw data and try to find interesting points
 - 'misinfo' for check the misinformation inside the test data by compare the link inside tweet with a dataframe contains website provide misinformation
 - 'top_tweets' find out the tweets that are popular based on the public_metrics, and analyze the data of these top tweets
 - 'k_core' build up k-core network and analyze the data near the core
 - 'NLP' is providing emtional analyze on text
 - 'Bot_detection' using the botometer to detect bot users
