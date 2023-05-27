## frequency of each word in a string and returns the length of the highest-frequency word
def find_highest_frequency_word_length(string):
    words = string.split()
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    max_frequency = max(word_frequency.values())
    highest_frequency_words = [word for word, frequency in word_frequency.items() if frequency == max_frequency]

    return len(highest_frequency_words[0])

# Test case 1
string = "write write write all the number from from from 1 to 100"
print(find_highest_frequency_word_length(string))  # Output: 5

# Test case 2
string = "the quick brown fox jumps over the lazy dog"
print(find_highest_frequency_word_length(string))  # Output: 3

# Test case 3
string = "hello world hello world hello world"
print(find_highest_frequency_word_length(string))  # Output: 5

## The find_highest_frequency_word_length function takes a string as input.
## The string is split into individual words using the split() method, and the words are stored in the words list.
## A dictionary word_frequency is initialized to store the frequency of each word.
### We iterate over each word in the words list. If the word is already present in the word_frequency dictionary, we increment its frequency. Otherwise, we add the word to the dictionary with an initial frequency of 1.
## After counting the frequencies, we find the maximum frequency using the max() function on the dictionary values.
## We create a list highest_frequency_words that contains all the words with the maximum frequency.
## Finally, we return the length of the first word in the highest_frequency_words list.
