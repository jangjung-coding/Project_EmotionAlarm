# main.py
import random
from response_storage import save_response
from insights import generate_insights


# List of sample questions
questions = [
    "How are you feeling today?",
    "What made you happy recently?",
    "What is something you dislike?",
    "What is one thing you're grateful for today?"
]

def ask_question():
    # Pick a random question
    question = random.choice(questions)
    print("\n" + question)
    response = input("Your response: ")
    return question, response

def main():
    print("Welcome to the Emotion Reflection App!")
    
    while True:
        print("\nMenu:")
        print("1. Answer a question")
        print("2. View insights")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            question, response = ask_question()
            save_response(question, response)
            print(f"\nThank you! Your response has been saved.")
        elif choice == "2":
            print("\n" + generate_insights())
        elif choice == "3":
            print("Goodbye! Keep reflecting on your emotions!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
