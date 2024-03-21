import re   # learned from Chatgpt, it provide function like 're.findall()' 
import pickle


def load_text(pkl_path):
    """Load book text from pickle"""
    with open(pkl_path, 'rb') as f:  # I debugged with ChatGpt, it told me to add 'rb' b/c it's used for reading when dealing with pickled datas
        return pickle.load(f).lower()


def count_mentions_simple(text, chars):
    """Count mentions of each character"""
    character_counts = {} # dic
    for char in chars:
        count = 0
        lowercases_character = char.lower()  
        # I asked chatgpt how to find all occurrences of names using case-insensitive matching.
        # Chatgpt told me to use re.findall() function, to find all matches of the patterns in the lowercase text
        # and it also imported 're' in lib
        matches = re.findall(r'\b' + re.escape(lowercases_character) + r'\b', text.lower())
        count = len(matches)
        character_counts[char] = count
    return character_counts

# Main characters I found online
chars = ['Scrooge', 'Marley', 'Bob', 'Tim', 'Fred', 'Past', 'Present', 'Future']


if __name__ == "__main__":
    text = load_text('book_text.pkl')  
    counts = count_mentions_simple(text, chars)
    
    # Print character mention counts
    for char, count in counts.items():
        print(f"{char}: {count}")


