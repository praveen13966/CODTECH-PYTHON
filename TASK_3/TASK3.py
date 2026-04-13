import random, nltk, spacy
nltk.download('punkt')
nltk.download('punkt_tab'); nlp = spacy.load("en_core_web_sm")

responses = {
    "greet":["Hi! How can I help?"],
    "bye":["Goodbye!"],
    "default":["Sorry, I didn’t get that."]
}

def intent(text):
    t = nltk.word_tokenize(text.lower())
    if "hi" in t or "hello" in t: return "greet"
    if "bye" in t: return "bye"
    return "default"

print("🤖 Chatbot ready. Type 'bye' to exit.")
while True:
    msg = input("You: ")
    doc = nlp(msg)
    ans = random.choice(responses[intent(msg)])
    for e in doc.ents:
        if e.label_=="GPE": ans=f"Weather info for {e.text}..."
    print("🤖:", ans)
    if intent(msg)=="bye": break
