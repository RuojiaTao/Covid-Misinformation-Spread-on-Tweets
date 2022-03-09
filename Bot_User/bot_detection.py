import pickle
import botometer
import json
import pandas as pd

def bot_detection():
    """
    This function examine the
    """
    # https://github.com/IUNetSci/botometer-python
    whole_ds=pd.read_pickle('data/all_data_split/sentiment.pkl')
    whole_ds.to_csv('small_dataset.csv')
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
