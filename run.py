import hydrate_tweets_twarc
import EDA
import K_Core_Degree
import bot_detection
import sample_dataset
import NLP
import NLP_ab_testing
import Bot_merge
import Tests_result

if __name__ == '__main__':
    hydrate_tweets_twarc.hydrate()
    EDA.EDA_data()
    K_Core_Degree.find_k_core()
    K_Core_Degree.assign_k_core()
    K_Core_Degree.k_core_vis()
    sample_dataset.sample_data()
    NLP.sentiment_check()
    NLP_ab_testing.ab_testing()
    bot_detection.bot_detection()
    Bot_merge.merge_bot()
    Tests_result.ml_result()
