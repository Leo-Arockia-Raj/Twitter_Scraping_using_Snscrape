# 🟦Twitter_Scraping_using_Snscrape 🟦

This program is a simple Python script that uses the Snscrape library to scrape tweets from Twitter.

**Requirements :**
•	Python 3.x
•	Snscrape
•	Pymongo
•	Pandas
•	datetime
•	streamlit

**Installation :**
1.	Install Python 3.x on your system.
2.	Install Snscrape by running pip install snscrape.
3.	If you want to save the data to MongoDB, install Pymongo by running pip install pymongo.
4.	Install Pandas library by running pip install pandas.
5.	Install Datetime library by running pip install datetime.
6.	Install Streamlit library by running pip install streamlit.
7.	Clone or download this repository.

**Usage :**
1.	Open the script in a text editor or Python IDE and run the script. It would open an interactive web page in your default browser.
2.	Enter the keyword or Hashtag to be searched, select the date range and slide limit to set the tweet count that need to be scraped from Twitter.
3.	The Scraped data will to be displayed on screen.
4.	If you want to save the data to MongoDB, click the “**Upload Data**” Button.
5.	To download the data into .csv and .json format, kindly click the "**Download data as CSV**"
6.	Button or "**Download data as JSON**" Button respectively.

**Note :**

MongoDB Default Connection Setting:
  •	**host name       :** 'localhost' (function parameter - db_host)
  •	**port number     :**  27017 (function parameter - db_port)
  •	**database name   :** 'twitter_db' (function parameter - user_database)
  •	**collection name :** 'twitter_search_collection'(function parameter - user_collection)

You can set your own connection detail, database name and collection name by providing parameters to data_upload() function or by changing the values of keyword arguments in script.

data_upload(search_word_fm, tweets_df_fm, **db_host**='localhost', **db_port**=27017, **user_database**='twitter_db', **user_collection**='twitter_search_collection')

**Contact :**

If you have any questions or issues, please contact me.
