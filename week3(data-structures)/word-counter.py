def word_counter(sentence):
    words = sentence.split()# split the sentence into words
    word_freq = {}#dictionary to store the value against each word
    
    # Count the frequency of each word
    for word in words:
        word = word.strip(".,!?;:\"'")#remove puntuation
        if word !="":
            word_freq[word] = word_freq.get(word, 0) + 1#word_freq.get(word, 0) get the count for the word. If the word is not in the dictionary, it returns 0 as the default value
    return word_freq
def main():
    print("Welcome to the Word Counter program!")
    sentence = input("Please enter a sentence: ")
    
    if not sentence:
        print("You didn't enter any sentence.")
        return
    else:
        word_freq = word_counter(sentence)
        print(word_freq)
        total_words = sum(word_freq.values())
        unique_words = len(word_freq)
        print(f"\nTotal words: {total_words}")
        print(f"Unique words: {unique_words}")
main()