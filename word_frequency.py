import re
from collections import Counter  # count how # times each words appear.
import pickle


# the goal is: analyze the frequency of words in book A Christmas Carol by Charles Dickens stored in 'book_text.txt' file, and excluding words listed in 'stop_words.txt'. I tried to use 'nltk.download('stopwords')' first (guided by ChatGpt), but I found that there are certain words I want to exclude, such as 'said', 'one', 'upon', so I made a txt file to add all stop words source from "sebleier/NLTK's list of english stopwords", and then I added the certain stop words from the orginal frequncy list that I wanted to exclude. The new frequency list is in the new file name: refined_word_frequencies.txt. This way, the words from the list are more meaningful.


def load_book_text(pickle_file_path):
    """
    load book text from pickle file
    """
    with open(pickle_file_path, "rb") as file:
        book_text = pickle.load(file).lower()
    return book_text


def clean_count_words(book_text, stop_words_list):
    """
    remove stop words and count the words frequencies.
    """
    words = re.findall(r"\w+", book_text)  # Extract words
    filtered_words = [word for word in words if word not in stop_words_list]
    return Counter(filtered_words)


def perform_word_frequency_analysis(
    book_pickle_path, frequency_output_path, stop_words_file_path
):
    """Main function to perform word frequency analysis and save the results to a file."""
    # Load stop words directly here
    with open(stop_words_file_path, "r", encoding="utf-8") as file:
        stop_words_list = (
            file.read().strip().split()
        )  # I asked CHATgpt how to split and read through each line in text

    book_text = load_book_text(book_pickle_path)
    word_frequencies = clean_count_words(book_text, stop_words_list)

    # Save/write the word, word frequencies to a file
    with open(
        frequency_output_path, "w", encoding="utf-8"
    ) as output_file:  # 'w' simply means write
        sorted_word_frequencies = sorted(
            word_frequencies.items(), key=lambda item: item[1], reverse=True
        )  # glab we learned lambda
        for word, frequency in sorted_word_frequencies:
            output_file.write(f"{word}: {frequency}\n")


if __name__ == "__main__":
    perform_word_frequency_analysis(
        "book_text.pkl", "refined_word_frequencies.txt", "stop_words.txt"
    )
    print(
        "Word frequency analysis completed and results are saved to refined_word_frequencies.txt."
    )
