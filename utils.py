import re
import pickle
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
import requests
import numpy as np

tweet_id = None
conv_id = None
token = None
id2name = {}


def extract_id(tweet_url):
    pattern = r"^https://twitter.com/[a-zA-z0-9_]*/status/(\d*)"
    match = re.search(pattern, tweet_url)
    if match:
        return match.group(1)
    else:
        return None


def save_token(token):
    try:
        with open('token.pkl', 'wb') as token_file:
            pickle.dump(token, token_file, protocol=pickle.HIGHEST_PROTOCOL)
        return True
    except:
        return False


def load_token(path):
    try:
        with open(path, 'rb') as token_file:
            token = pickle.load(token_file)
        return token
    except:
        return None


def set_token_button(button, options):
    # 0 - normal
    # 1 - success
    # 2 - failed
    if options == 0:
        button.setStyleSheet('border: None; background-color: #1D9BF0; color: white;')
        button.setText('Set Token')
    elif options == 1:
        button.setStyleSheet('border: None; background-color: LimeGreen; color: white;')
        button.setText('Success')
    elif options == 2:
        button.setStyleSheet('border: None; background-color: Red; color: white;')
        button.setText('Failed')


def set_token(token, main_window):
    saved = save_token(token)
    button = main_window.token_submit
    if saved:
        set_token_button(button, 1)
    else:
        set_token_button(button, 2)
    main_window.token_input.setText('')
    QtCore.QTimer.singleShot(2000, lambda: set_token_button(button, 0))


def set_warning(warn_label, text):
    warn_label.setStyleSheet("color: red")
    warn_label.setText(text)
    QtCore.QTimer.singleShot(3000, lambda: warn_label.setText(""))


def read_tweet(link, main_window):
    global tweet_id
    tweet_id = extract_id(link)
    if not tweet_id:
        set_warning(main_window.warn, "Invalid Tweet URL")
        return
    main_window.web.load(QUrl(link))
    main_window.web.show()


def pick_winner(main_window):
    global tweet_id
    global token
    global id2name
    global conv_id
    token = load_token("token.pkl")
    if not token:
        set_warning(main_window.warn, "Token not found")
    if not tweet_id:
        set_warning(main_window.warn, "Invalid Tweet URL")
    link = create_tweet_url(tweet_id)
    response = connect_to_endpoint(link, "v2TweetLookupPython")
    if not response:
        set_warning(main_window.warn, "Invalid Tweet URL or Invalid token")
    author_id = response['data'][0]['author_id']
    conv_id = response['data'][0]['conversation_id']
    status_1, followers = get_followers(author_id, main_window.fo_check.isChecked())
    status_2, likes = get_likes(main_window.like_check.isChecked())
    status_3, comments = get_comments(main_window.co_check.isChecked())
    status_4, retweets = get_retweet(main_window.re_check.isChecked())
    if not status_1 or not status_2 or not status_3 or not status_4:
        set_warning(main_window.warn, "Please check network or your token")
        return
    user_list = []
    if followers:
        user_list.append(followers)
    if likes:
        user_list.append(likes)
    if comments:
        user_list.append(comments)
    if retweets:
        user_list.append(retweets)
    if len(user_list) == 0:
        candidate_list = np.array([]).astype(np.int)
    elif len(user_list) == 1:
        candidate_list = np.array(user_list[0]).astype(np.int)
    else:
        candidate_list = np.array(user_list[0])
        for i in range(1, len(user_list)):
            candidate_list = np.intersect1d(candidate_list, np.array(user_list[i]))
    candidate_num = candidate_list.shape[0]
    win_num = main_window.num_win.value()
    if win_num > candidate_num or win_num == 0:
        set_warning(main_window.warn, "Invalid number of winners")
        return
    np.random.shuffle(candidate_list)
    winner_index = np.random.choice(candidate_num, win_num, replace=False)
    winners_id = candidate_list[winner_index]
    winners = []
    for wid in winners_id:
        winners.append(id2name[wid])
    model = QtGui.QStandardItemModel()
    main_window.win_list.setModel(model)
    for winner in winners:
        item = QtGui.QStandardItem('@' + winner)
        model.appendRow(item)


def connect_to_endpoint(url, method, user_fields=None):
    response = requests.request("GET", url, auth=lambda r: bearer_oauth(r, method), params=user_fields)
    if response.status_code != 200:
        return None
    return response.json()


def create_tweet_url(id):
    tweet_fields = "tweet.fields=author_id,text,conversation_id"
    ids = "ids={}".format(id)
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def bearer_oauth(r, method):
    global token
    r.headers["Authorization"] = f"Bearer {token}"
    r.headers["User-Agent"] = method
    return r


def get_followers(author_id, required):
    global id2name
    if not required:
        return 200, None
    link = "https://api.twitter.com/2/users/{}/followers?max_results=1000".format(author_id)
    method = "v2FollowersLookupPython"
    response = connect_to_endpoint(link, method)
    follower_list = []
    while response:
        if 'data' in response:
            for user in response['data']:
                if int(user['id']) not in id2name:
                    id2name[int(user['id'])] = user['username']
                follower_list.append(int(user['id']))
            if 'next_token' in response['meta']:
                link = "https://api.twitter.com/2/users/{}/followers?max_results=1000&pagination_token={}" \
                    .format(author_id, response['meta']['next_token'])
                response = connect_to_endpoint(link, method)
            else:
                return 200, follower_list
        else:
            return 200, follower_list
    return None, None


def get_likes(required):
    global tweet_id
    if not required:
        return 200, None
    user_fields = "user.fields=id,username"
    link = "https://api.twitter.com/2/tweets/{}/liking_users".format(tweet_id)
    method = "v2LikingUsersPython"
    response = connect_to_endpoint(link, method, user_fields=user_fields)
    likes_list = []
    while response:
        if 'data' in response:
            for user in response['data']:
                if int(user['id']) not in id2name:
                    id2name[int(user['id'])] = user['username']
                likes_list.append(int(user['id']))
            if 'next_token' in response['meta']:
                link = "https://api.twitter.com/2/tweets/{}/liking_users?max_results=100&pagination_token={}" \
                    .format(tweet_id, response['meta']['next_token'])
                response = connect_to_endpoint(link, method)
            else:
                return 200, likes_list
        else:
            return 200, likes_list
    return None, None


def get_comments(required):
    global conv_id
    if not required:
        return 200, None
    link = "https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{}" \
           "&tweet.fields=author_id&max_results=100".format(conv_id)
    method = "v2RecentSearchPython"
    response = connect_to_endpoint(link, method)
    comments_list = []
    while response:
        if 'data' in response:
            for user in response['data']:
                if int(user['author_id']) not in id2name:
                    user_link = "https://api.twitter.com/2/users/{}".format(user['author_id'])
                    user_fields = "user.fields=id,username"
                    user_method = "v2UserLookupPython"
                    user_response = connect_to_endpoint(user_link, user_method, user_fields=user_fields)
                    if user_response:
                        id2name[int(user['author_id'])] = user_response['data']['username']
                comments_list.append(int(user['author_id']))
            if 'next_token' in response['meta']:
                link = "https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{}" \
                       "&tweet.fields=author_id&max_results=100&pagination_token={}".format(conv_id, response['meta'][
                    'next_token'])
                response = connect_to_endpoint(link, method)
            else:
                return 200, comments_list
        else:
            return 200, comments_list
    return None, None


def get_retweet(required):
    global tweet_id
    if not required:
        return 200, None
    user_fields = "user.fields=id,username"
    link = "https://api.twitter.com/2/tweets/{}/retweeted_by".format(tweet_id)
    method = "v2RetweetedByPython"
    response = connect_to_endpoint(link, method, user_fields=user_fields)
    retweets_list = []
    while response:
        if 'data' in response:
            for user in response['data']:
                if int(user['id']) not in id2name:
                    id2name[int(user['id'])] = user['username']
                retweets_list.append(int(user['id']))
            if 'next_token' in response['meta']:
                link = "https://api.twitter.com/2/tweets/{}/retweeted_by?max_results=100&pagination_token={}" \
                    .format(tweet_id, response['meta']['next_token'])
                response = connect_to_endpoint(link, method)
            else:
                return 200, retweets_list
        else:
            return 200, retweets_list
    return None, None
