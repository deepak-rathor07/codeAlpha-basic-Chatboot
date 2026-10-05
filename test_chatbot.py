"""Tests for InternshipBot's rule-based responses."""

import unittest
from unittest.mock import call, patch

from chatbot import get_response, is_exit_message
from main import main


class ChatbotResponseTests(unittest.TestCase):
    def test_greeting_is_case_insensitive(self) -> None:
        self.assertIn("Namaste!", get_response("HI there"))

    def test_answers_project_and_internship_questions(self) -> None:
        self.assertIn("chhote tasks", get_response("Tell me about my project"))
        self.assertIn("naye skills", get_response("internship tips"))

    def test_blank_and_unknown_messages_have_helpful_responses(self) -> None:
        self.assertIn("Kuch type", get_response("  "))
        self.assertIn("Thoda aur bata", get_response("What is the weather?"))

    def test_exit_detection_uses_words_not_substrings(self) -> None:
        self.assertTrue(is_exit_message("Goodbye!"))
        self.assertFalse(is_exit_message("I like this project"))

    @patch("builtins.input", side_effect=["hello", "bye"])
    @patch("builtins.print")
    def test_chat_ends_after_exit_command(
        self, mock_print: unittest.mock.MagicMock, mock_input: unittest.mock.MagicMock
    ) -> None:
        main()

        self.assertEqual(mock_input.call_count, 2)
        self.assertIn(
            call("InternshipBot: Alvida! Baat karke achha laga. / Goodbye, it was nice chatting!"),
            mock_print.call_args_list,
        )


if __name__ == "__main__":
    unittest.main()
