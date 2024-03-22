
import nltk

# Download the punkt tokenizer models. This is used by the sent_tokenize function.
nltk.download('punkt')
nltk.download('vader_lexicon')
 
import pickle

from nltk.sentiment import (SentimentIntensityAnalyzer,)  # Chatgpt told me this is neccesary for generating the sentiment score
from nltk.tokenize import (sent_tokenize,)  # cut into individual sentence, easier to handle.


def load_book_text_from_pickle(pickle_file_path):
    """load book text from pickle file"""
    with open(pickle_file_path, "rb") as file:
        text = pickle.load(file).lower()
    return text


# List of key characters I found online
character_list = [
    "Scrooge",
    "Marley",
    "Bob",
    "Tim",
    "Fred",
    "Past",
    "Present",
    "Future",
]


def analyze_character_sentiment(
    book_text,
    characters=["Scrooge", "Marley", "Bob", "Tim", "Fred", "Past", "Present", "Future"],
):
    """analyze sentiment for sentences mentioning characters"""
    tool = SentimentIntensityAnalyzer()
    sentences = sent_tokenize(
        book_text
    )  # Chatgpt debugged and said I need to split the text into sentences.
    sentiment_counts = {
        "Scrooge": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Marley": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Bob": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Tim": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Fred": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Past": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Present": {"good_person": 0, "neutral": 0, "bad_person": 0},
        "Future": {"good_person": 0, "neutral": 0, "bad_person": 0},
    }

    for sentence in sentences:  # go through each sentences.
        for character in character_list:
            if character.lower() in sentence:
                score = tool.polarity_scores(sentence)["compound"]
                if score >= 0.6:
                    sentiment_counts[character]["good_person"] += 1
                elif score >= 0.3:
                    sentiment_counts[character]["neutral"] += 1
                else:
                    sentiment_counts[character]["bad_person"] += 1

    return sentiment_counts


def calculate_sentiment_percentage(sentiment_counts):
    """calculate percentage of sentiment for each character"""
    sentiment_percentages = {}
    for character in sentiment_counts:
        counts = sentiment_counts[character]
        total_mentions = 0  # initial
        for sentiment in counts:
            total_mentions += counts[sentiment]
        # I think turning into percentage is better to process
        good_percent = (counts["good_person"] / total_mentions) * 100
        neutral_percent = (counts["neutral"] / total_mentions) * 100
        bad_percent = (counts["bad_person"] / total_mentions) * 100
        sentiment_percentages[character] = {
            "good_person": good_percent,
            "neutral": neutral_percent,
            "bad_person": bad_percent,
        }
    return sentiment_percentages


pickle_file_path = "book_text.pkl"


if __name__ == "__main__":
    book_text = load_book_text_from_pickle(pickle_file_path)
    sentiment_counts = analyze_character_sentiment(book_text, character_list)
    sentiment_percentages = calculate_sentiment_percentage(sentiment_counts)

    for character, percentages in sentiment_percentages.items():
        print(f"{character}: {percentages}")
