# -*- coding: utf-8 -*-
import os
import re
from flask import Flask, render_template
from helpers.fun_tweet_scraper import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm.j2")

@app.route('/latest_pauline_tweets')
def latest_tweets():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"}
    search_url = "https://twitter.com/search"
    params = {"q" : query_builder()}
    tweet_objs = get_funny_tweets(search_url, params=params, headers=headers)

    date_matcher = re.compile("\d+-\d+-\d+")
    start_date, end_date = date_matcher.findall(params["q"])

    return render_template("display_tweets.htm.j2", tweets=tweet_objs,
                            start=start_date, end=end_date)

if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True, port=80)
