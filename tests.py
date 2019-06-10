import unittest
from unittest.mock import patch

from translate import startwith_vowel, translate_word
from client import send_word

class TestTranslate(unittest.TestCase):

    def test_startwith_vowel_return_false_if_word_start_with_consonant(self):
        word = 'james'
        self.assertFalse(startwith_vowel(word))

    def test_startwith_vowel_return_true_if_word_start_with_vowel(self):
        word = 'ousmane'
        self.assertTrue(startwith_vowel(word))

    def test_translate_word_translate(self):
        word = 'hello'
        translated = translate_word(word)

        self.assertNotEqual(word, translated)

    def test_translate_word_match_capitalization(self):
        word1 = 'Hello'
        word2 = 'hello'
        translated1 = translate_word(word1)
        translated2 = translate_word(word2)

        self.assertTrue(translated1.istitle())
        self.assertFalse(translated2.istitle())


class TestClient(unittest.TestCase):

    @patch('client.requests.post') # mock the api call
    def test_client_return_bad_request_if_status_400(self, mock_request):
        mock_request.return_value.status_code = 400
        response = send_word('Drew')

        self.assertEqual(response, 'Bad Request 400')



if __name__ == '__main__':
    unittest.main()
