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


Abstract: 
Spread of misinformation over social media posts challenges to daily information intake and exchange. Especially under current covid 19 pandemic, the disperse of misinformation regarding to covid 19 diseases and vaccination posts threats to individuals' wellbeings and general publich health. This project seeks to invertigate the spread of misinformation over social media (Twitter) under covid 19 pademic. The first topic is the effect of bot users on the spread of misinformation, and the second topic is to examine users' attitude towards misinformation. These two topics are analyze under the social structure (connected social graphs) created through user's interactions on Twitter. This project also seeks to invertigate the change in proportion of bot users and users' attitude towards misinformation as it's approaching to the center of the social network. 
