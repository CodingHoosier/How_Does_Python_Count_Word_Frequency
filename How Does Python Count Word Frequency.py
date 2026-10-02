# https://www.youtube.com/watch?v=9VCrK62CgJc
# How Does Python Count Word Frequency?
print("First test:")
text = "cat cat cat dog dog mouse"
word_frequency = {w: text.split().count(w) for w in set(text.split())}
print(f"word_frequency is a {type(word_frequency)}")
print(word_frequency)   
print("Second test:")
text = "This is a sample string. \
This text is for testing word frequency counting in Python. \
Python is great for text processing."
word_frequency = {w: text.split().count(w) for w in set(text.split())}
print(word_frequency)   
