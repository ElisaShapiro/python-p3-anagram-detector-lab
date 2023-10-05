# your code goes here!
class Anagram:
    def __init__(self, word):
        self.letters_in_word = sorted([letter for letter in word])
    def match(self, list_of_words):
        matches = []
        for word in list_of_words:
            if sorted([letter for letter in word]) == self.letters_in_word:
                matches.append(word)
        return matches