import string


class Anagram:
    def __init__(self, _sentence):
        self.sentence = _sentence
        self.length = len(_sentence)
        self.letters = self.process_sentence(_sentence)

    def remove_punctuation_marks(self, original_sentence):
        return original_sentence.translate(string.maketrans("", ""), string.punctuation)

    def remove_duplicated_letters(self, original_sentence):
        return "".join(set(original_sentence.lower()))

    def process_sentence(self, original_sentence):
        original_sentence = self.remove_duplicated_letters(original_sentence)
        original_sentence = self.remove_punctuation_marks(original_sentence)
        return original_sentence.strip()
