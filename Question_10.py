import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag
from collections import defaultdict

def count_pos_tags(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)
    
    # Initialize counts dictionary
    counts = defaultdict(int)
    
    # Count the number of verbs, nouns, pronouns, and adjectives
    for word, tag in pos_tags:
        if tag.startswith('VB'):  # Verb
            counts['verbs'] += 1
        elif tag.startswith('NN'):  # Noun
            counts['nouns'] += 1
        elif tag.startswith('PR'):  # Pronoun
            counts['pronouns'] += 1
        elif tag.startswith('JJ'):  # Adjective
            counts['adjectives'] += 1
    
    return counts

# Test the function with a sample sentence
sentence = "The quick brown fox jumps over the lazy dog."
counts = count_pos_tags(sentence)
print(counts)

# Additional test cases
# Test case 1
text1 = "I like to eat pizza."
counts1 = count_pos_tags(text1)
print(counts1)

# Test case 2
text2 = "She is reading an interesting book."
counts2 = count_pos_tags(text2)
print(counts2)