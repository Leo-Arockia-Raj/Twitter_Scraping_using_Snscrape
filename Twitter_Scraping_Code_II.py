import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
from pymongo import MongoClient


def twitter_scraper(limit_fm, query_fm):
    """
    inputs:
        limit_fm - specify the twitter scrape limit
        query_fm - provide query in specified format "(search_word) since: (from_date) until:(to_date)"
        Note: from_date and to_date has to be type cast to string type.
    output: returns twitter scraped dataframe
    """
    tweets_list = []
    for tweet in sntwitter.TwitterSearchScraper(query_fm).get_items():
        if len(tweets_list) > limit_fm:
            break
        else:
            tweets_list.append(
                [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount,
                 tweet.lang, tweet.source, tweet.likeCount])
    cols = ["date", "id", "url", "tweet content", "user", "reply count", "retweet count", "language",
            "source", "like count"]
    tweets_df_tm = pd.DataFrame(tweets_list, columns=cols)
    return tweets_df_tm


def data_upload(search_word_fm, tweets_df_fm):
    """
    Pass parameter to store document in "twitter_search_collection"

    search_word_fm: pass "dictionary key" for storing the passed dataframe as document
                    in "twitter_search_collection" collection using mongoDB.
    tweets_df_fm: pass dataframe that needs to be stored.
    """
    client = MongoClient('localhost', 27017)  # creates a connection with port 27017.
    db = client['twitter_db']  # Creates a database named "twitter_db".
    collection = db['twitter_search_collection']  # Creates a collection "twitter_search_collection" in twitter_db.
    keyword = search_word_fm + str(datetime.datetime.now())
    tweet_dict = tweets_df_fm.to_dict('records')
    collection.insert_one({keyword: tweet_dict})
    st.success("Upload Successful")


st.title(":blue[TWITTER SCRAPER USING SNSCRAPE]")
search_word = st.text_input("**:green[Enter Keyword or Hashtag to be searched: ]**", "python")
from_date = st.date_input("**:green[Select From-Date:]**", max_value=datetime.datetime.now())
to_date = st.date_input("**:green[Select To-Date:]**", max_value=datetime.datetime.now())
limit = st.slider("**:green[Set Tweet Scrape Limit]**", 1, 1000, 100)
query = search_word + ' since:' + str(from_date) + ' until:' + str(to_date)

tweets_df = twitter_scraper(limit, query)
# parameters are passed to ensure that twitter_scraper function can be used in other programs.

st.subheader("**:violet[Scraped Twitter data for '"+search_word+"' from "+str(from_date)+" to "+str(to_date)+".]**")
st.dataframe(tweets_df)
st.write("**:green[Click to Upload Data]**")

if st.button("Upload Data"):
    # Loading Data into MongoDB DataBase
    data_upload(search_word, tweets_df)
    # parameters are passed to ensure that data_upload function can be used in other programs.

st.write("**:green[Click to Save file in .CSV format]**")
st.download_button(label="Download data as CSV", data=tweets_df.to_csv(), file_name='data_csv.csv')
st.write("**:green[Click to Save file in .JSON format]**")
st.download_button(label="Download data as JSON", data=tweets_df.to_json(), file_name='data_json.json')
