import nltk
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Download tokenizer if not already present
nltk.download('punkt', quiet=True)

# Function to summarize the text
def summarize_text(text, sentence_count=3):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, sentence_count)
        return " ".join(str(sentence) for sentence in summary)
    except Exception as e:
        return f" Error: {str(e)}"

# Function to save the summary to a text file
def save_to_file(summary, filename="summary_output.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(summary)
        print(f"\n Summary saved successfully to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f" Could not save file: {str(e)}")

# Display user instructions
def show_instructions():
  
# Main program
if __name__ == "__main__":
    show_instructions()

    user_text = input(" Paste the text you want summarized:\n\n")

    if len(user_text.strip()) < 50:
        print("\n Text too short. Please enter at least 50 characters.")
    else:
        try:
            sentence_count = int(input("\n How many sentences should the summary contain? "))
            if sentence_count <= 0:
                raise ValueError
        except:
            sentence_count = 3
            print(" Invalid input. Using default: 3 sentences.")

        summary = summarize_text(user_text, sentence_count)
        print("\n SUMMARY:\n")
        print(summary)

        save_to_file(summary)
