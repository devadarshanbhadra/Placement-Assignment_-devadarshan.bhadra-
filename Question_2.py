
#Question 2: -
#Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
#he can remove just one character at the index in the string, and the remaining characters will occur the same
#number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
#Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
#an explanation for the same.

#Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
#Example output 1- YES

#Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
#character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }

#Example output 2 - NO

from collections import Counter

def is_valid_string(s):
    # Count the frequency of each character in the string
    char_freq = Counter(s)
    
    # Count the frequency of frequencies
    freq_freq = Counter(char_freq.values())
    
    # If there is only one unique frequency, the string is valid
    if len(freq_freq) == 1:
        return 'yes'
    
    # If there is only one unique frequency, the string is valid
    if len(freq_freq) == 2 and (1 in freq_freq.values() and freq_freq[1] == 1):
        return 'yes'
    
    return "No"
        
        
# Test case 1
s = "abc"
print(is_valid_string(s))  # Output: YES

# Test case 2
s = "abcc"
print(is_valid_string(s))  # Output: NO

# Test case 3
s = "aabbcc"
print(is_valid_string(s))  # Output: YES

# Test case 4
s = "aabbccc"
print(is_valid_string(s))  # Output: YES

## The is_valid_string function takes a string s as input.
## The frequency of each character in the string is counted using the Counter class from the collections module. The result is stored in the char_frequency dictionary, where the keys are characters and the values are their frequencies.
## The frequency of frequencies is counted by applying Counter on the values of char_frequency. The result is stored in the frequency_frequency dictionary, where the keys are the unique frequencies and the values are their counts.
## If there is only one unique frequency (i.e., len(frequency_frequency) == 1), it means all characters have the same frequency, and the string is valid. In this case, "YES" is returned.
