import pickle

# Loading the text back from the pickle file
with open('book_text.pkl', 'rb') as file:
    reloaded_text = pickle.load(file)

