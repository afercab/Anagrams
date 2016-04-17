from unittest import TestCase
from anagram import Anagram


class TestAnagram(TestCase):
    def test_initializer_must_initialize_with_correct_sentence_size_and_letters(self):
        test_sentence = "Testing"
        expected_test_sequence_letters = "eginst"
        anagram = Anagram(test_sentence)

        self.assertEqual(anagram.sentence, test_sentence)
        self.assertEqual(anagram.length, len(test_sentence))
        self.assertEqual(anagram.letters, expected_test_sequence_letters)

    def test_initializer_with_blank_spaces_must_initialize_with_correct_sentence_size_and_letters(self):
        test_sentence = "Testing two"
        expected_test_sequence_letters = "egionstw"
        anagram = Anagram(test_sentence)

        self.assertEqual(test_sentence, anagram.sentence)
        self.assertEqual(len(test_sentence), anagram.length)
        self.assertEqual(expected_test_sequence_letters, anagram.letters)

    def test_initializer_with_punctuation_marks_must_initialize_with_correct_sentence_size_and_letters(self):
        test_sentence = "Testing, two!!"
        expected_test_sequence_letters = "egionstw"
        anagram = Anagram(test_sentence)

        self.assertEqual(test_sentence, anagram.sentence)
        self.assertEqual(len(test_sentence), anagram.length)
        self.assertEqual(expected_test_sequence_letters, anagram.letters)
