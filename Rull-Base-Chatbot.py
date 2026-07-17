# ============================================
# MENU MODULE - FULL BACKGROUND COLOR
# ============================================

import os
import random
import string

# Color codes for Windows terminal (ANSI)
COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bg_blue": "\033[44m",
    "bg_cyan": "\033[46m",
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_full_line(color_bg, text="", text_color="white", bold=False):
    # Print a full-width line with background color and optional centered text.
    term_width = 80
    style = COLORS["bold"] if bold else ""
    padded = text.center(term_width)
    print(f"{style}{COLORS[color_bg]}{COLORS[text_color]}{padded}{COLORS['reset']}")

def display_menu():
    clear_screen()
    
    print_full_line("bg_blue", "")
    print_full_line("bg_blue", "RULL-BASE CHATBOT", "white", bold=True)
    print_full_line("bg_blue", "")
    print_full_line("bg_cyan", "- Accepts natural language text input from the user.", "white")
    print_full_line("bg_blue", "")
    print_full_line("bg_blue", "Enter your message below (type 'exit' to quit):", "yellow", bold=True)
    print_full_line("bg_blue", "")
    print('')
    
    print(COLORS["reset"], end="")

# ============================================
# INPUT ACQUISITION
# ============================================

def get_user_input():
    user_input = input(COLORS["cyan"] + ">>> " + COLORS["reset"])
    return user_input

# ============================================
# TEXT PROCESSING FUNCTION
# ============================================

def tokenize_clean_text(raw_text):
    """
    Converts text to lowercase, removes punctuation, tokenizes into list.
    Returns: list of tokens (strings)
    """
    lower_text = raw_text.lower()
    translator = str.maketrans("", "", string.punctuation)
    no_punct = lower_text.translate(translator)
    tokens = no_punct.split()
    return tokens

# ============================================
# INTENT DETECTION - RULE BASE
# ============================================

# Intent dictionary: key = trigger word, value = response sentence
INTENT_RESPONSES = {
    "hello": [
        "Greetings. How may I assist you today?",
        "Hello. State your query.",
        "Good day. What is your request?"
    ],
    "hi": [
        "Hello. State your query.",
        "Hi. Proceed with your input.",
        "Greetings. Awaiting your command."
    ],
    "hey": [
        "Acknowledged. Proceed with your request.",
        "Hey. What do you need?",
        "Received. Continue."
    ],
    "help": [
        "I can process text, tokenize input, and respond to basic intents.",
        "Help available. State your issue clearly.",
        "Function: text processing and intent matching."
    ],
    "weather": [
        "I do not have live data. Check a meteorological service.",
        "Weather data unavailable. Use external sources.",
        "No weather function. Consult a weather API."
    ],
    "time": [
        "Refer to your system clock. I am not a timekeeper.",
        "Time queries not supported. Check your device.",
        "I lack temporal functions. Use system time."
    ],
    "date": [
        "Consult your calendar. I lack temporal functions.",
        "Date unavailable. Refer to external calendar.",
        "No date function. System clock provides this."
    ],
    "name": [
        "I am Rull-Base Chatbot. I have no other designation.",
        "Designation: Rull-Base Chatbot.",
        "My name is Rull-Base. No alternative."
    ],
    "who": [
        "I am a rule-based processing system. No identity beyond function.",
        "Who? I am Rull-Base, a text processor.",
        "Identity: rule-based chatbot. Function only."
    ],
    "what": [
        "I perform text tokenization and intent matching.",
        "What: I process your input and respond.",
        "Core function: tokenization and rule-based replies."
    ],
    "how": [
        "I operate via dictionary lookup and conditional logic.",
        "How: token matching against predefined intents.",
        "Mechanism: dictionary lookup with random response selection."
    ],
    "why": [
        "Purpose: demonstrate rule-based natural language processing.",
        "Why: to illustrate basic intent detection.",
        "Exists to show rule-based NLP in action."
    ],
    "bye": [
        "Terminating session. Goodbye.",
        "Bye. Session ended.",
        "Farewell. Disconnecting."
    ],
    "exit": [
        "Exit command received. Shutting down.",
        "Exiting. Process terminated.",
        "Shutdown initiated."
    ],
    "quit": [
        "Quit acknowledged. Ending process.",
        "Quit received. Terminating.",
        "Process ending."
    ],
    "thanks": [
        "Acknowledged. No further action required.",
        "Thanks noted. Continue or exit.",
        "Acknowledgment received."
    ],
    "thank": [
        "You are welcome. Continue or terminate.",
        "Welcome. Proceed.",
        "Acknowledged."
    ],
    "sorry": [
        "Apology noted. Irrelevant to processing.",
        "No apology needed. State your query.",
        "Irrelevant. Continue."
    ],
    "error": [
        "No error detected. State your problem clearly.",
        "Error function unavailable. Clarify your input.",
        "No error. Rephrase."
    ],
    "test": [
        "Test input received. System operational.",
        "Test acknowledged. All functions normal.",
        "System responding to test."
    ]
}

def detect_intent(tokens):
    """
    Checks tokens against INTENT_RESPONSES keys.
    Returns: (matched_key, response) or (None, None)
    Response is randomly selected from the list.
    """
    for token in tokens:
        if token in INTENT_RESPONSES:
            return token, random.choice(INTENT_RESPONSES[token])
    return None, None

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    display_menu()
    
    while True:
        raw = get_user_input()
        if raw.strip().lower() == "exit":
            print(COLORS["red"] + "Terminating." + COLORS["reset"])
            break
        
        tokens = tokenize_clean_text(raw)
        
        # Intent detection
        matched_key, response = detect_intent(tokens)
        
        if matched_key:
            print(COLORS["green"] + response + COLORS["reset"])
        else:
            print(COLORS["yellow"] + "No matching intent found. Rephrase your input." + COLORS["reset"])