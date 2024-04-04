import requests
import pandas as pd
import re
from langdetect import detect


class TwitterAPI:
    def __init__(self):
        self.url = "https://twitter154.p.rapidapi.com/hashtag/hashtag"
        self.headers = {
            "X-RapidAPI-Key": "17f22a1354msh519ee6dd37bee98p13a068jsndb5c88696b21",
            "X-RapidAPI-Host": "twitter154.p.rapidapi.com",
        }

    def get_user_input(self, prompt):
        return input(prompt).strip()

    def validate_hashtags(self, hashtags):
        for hashtag in hashtags:
            if not hashtag.startswith("#"):
                return False
        return True

    def validate_section_choice(self, section_choice):
        return section_choice in ["1", "2"]

    def clean_text(self, text):
        cleaned_text = re.sub(r"#[^\s]+", "", text)
        cleaned_text = re.sub(r"http[s]?://\S+", "", cleaned_text)
        return cleaned_text.strip()

    def retrieve_tweets(self):
        print(
            "Please enter the hashtags of the tweets you want to retrieve, separated by spaces."
        )
        print(
            "Hashtags help filter tweets based on a specific topic or keyword."
        )

        while True:
            hashtag_input = self.get_user_input(
                "Enter the hashtag(s), separated by spaces (e.g., #moviereview #latestmovies): "
            )
            hashtags = hashtag_input.split()
            if self.validate_hashtags(hashtags):
                break
            else:
                print("Error: Hashtags must start with '#' character.")

        print("\nChoose the section:")
        print(
            "1. Top Tweets - Retrieves the top tweets based on relevance or engagement."
        )
        print("2. Latest Tweets - Retrieves the most recent tweets.")

        while True:
            section_choice = self.get_user_input(
                "Enter the section number (1 or 2): "
            )
            if self.validate_section_choice(section_choice):
                break
            else:
                print(
                    "Error: Invalid section choice. Please enter '1' or '2'."
                )

        section = "top" if section_choice == "1" else "latest"

        hashtag_query = " ".join(hashtags)

        querystring = {
            "hashtag": hashtag_query,
            "limit": "20",
            "section": section,
            "language": "en",
        }

        response = requests.get(
            self.url, headers=self.headers, params=querystring
        )

        if response.ok:
            data = response.json()
            results = data.get("results", [])

            if results:
                tweets_data = []

                for tweet in results:
                    tweet_id = tweet.get("tweet_id")
                    user_id = tweet["user"]["user_id"]
                    text = tweet.get("text")
                    text = " ".join(text.split())
                    cleaned_text = self.clean_text(text)

                    try:
                        if detect(cleaned_text) == "en":
                            tweets_data.append(
                                {
                                    "Tweet ID": tweet_id,
                                    "User ID": user_id,
                                    "Text": cleaned_text,
                                }
                            )
                    except:
                        pass

                tweets_df = pd.DataFrame(tweets_data)
                return tweets_df

            else:
                print("No tweets found in the response.")
        else:
            print("Failed to retrieve data. Error:", response.text)
