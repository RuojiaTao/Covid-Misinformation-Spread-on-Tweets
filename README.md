# Covid-Misinformation-Spread-on-Tweets
Analyze the misinformation about covid spreading in tweet

Our website: https://ruojiatao.github.io/Covid-Misinformation-Spread-on-Tweets/

Abstract: 
Spread of misinformation over social media posts challenges to daily information intake and exchange. Especially under current covid 19 pandemic, the disperse of misinformation regarding to covid 19 diseases and vaccination posts threats to individuals' wellbeings and general publich health. This project seeks to invertigate the spread of misinformation over social media (Twitter) under covid 19 pademic. The first topic is the effect of bot users on the spread of misinformation, and the second topic is to examine users' attitude towards misinformation. These two topics are analyze under the social structure (connected social graphs) created through user's interactions on Twitter. This project also seeks to invertigate the change in proportion of bot users and users' attitude towards misinformation as it's approaching to the center of the social network. 



 - The `run.py` file run all part of code
 - `Data_Pre` folder contains: 
     - `hydrate_tweets_twarc.py` : hydrating the data
     - `EDA.py`: explore the raw data and try to find interesting points
 - `K_Core` folder contains:
     - `K_Core_Degree.py`: set up a graph and calculate the K-Core degree , assign K Core degree back to all data, and plot out the spread of K-Core.
     - `sample_dataset.py` : sample a small dataset for analzye
     - `Tests_result.py` : run a linear machine learning model to predict the negative sentiment based on different parapmeters. Base on the coefficient of ML model to find the relstionship between parpameters and negative sentiment.
 - `NLP` folder contains:
     - `NLP.py`: get the sentiment scores of each tweets, and plot out overall trends
     - `NLP_ab_testing`: run a 2 sample t-test to see if there is an sigificant difference between negative sentiments in different pair of groups that has different K-Core degrees
 - `data` folder contains:
     - `iffy.csv` used for checking misinformation links


