# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, candidates):
        matches = []

        sortWord = sorted(self.word.lower())

        for candidate in candidates:
            sortCandidate = sorted(candidate.lower())
            if candidate.lower() != self.word.lower() and sortCandidate == sortWord:
                matches.append(candidate)
        return matches