import unittest
from ShadowFox.Hangman import HangmanGame

class InternshipProjectsTests(unittest.TestCase):
    def test_hangman_win_scenario(self):
        game = HangmanGame(word="PYTHON")
        self.assertEqual(game.get_masked_word(), "_ _ _ _ _ _")
        for char in "PYTHON":
            game.make_guess(char)
        self.assertTrue(game.is_won())
        self.assertTrue(game.is_game_over())

    def test_hangman_loss_scenario(self):
        game = HangmanGame(word="CAT")
        for wrong_char in "BDEFGHJ":
            game.make_guess(wrong_char)
        self.assertFalse(game.is_won())
        self.assertTrue(game.is_game_over())

if __name__ == '__main__':
    unittest.main()
