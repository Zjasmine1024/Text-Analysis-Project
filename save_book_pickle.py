import urllib.request
import pickle

# URL of the Project Gutenberg book you want to download
url = 'https://www.gutenberg.org/cache/epub/24022/pg24022.txt'

# Fetching the book text
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')

# Saving the fetched text to a pickle file
with open('book_text.pkl', 'wb') as file:
    pickle.dump(text, file)
