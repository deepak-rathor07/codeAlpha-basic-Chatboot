"""Command-line entry point for InternshipBot."""

from chatbot import get_response, is_exit_message


def main() -> None:
    """Run the chat until the user enters an exit command."""
    print("InternshipBot: Namaste! Chat shuru karne ke liye message likhiye.")
    print("InternshipBot: Type 'bye' to end the chat.")

    while True:
        message = input("You: ")
        print(f"InternshipBot: {get_response(message)}")
        if is_exit_message(message):
            break


if __name__ == "__main__":
    main()
