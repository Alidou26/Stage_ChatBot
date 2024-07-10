import random
import json

import torch

#from spellchecker import SpellChecker

from model import NeuralNet
from nltk_code import sac_de_mot, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)


#spell = SpellChecker(language='fr')

# def correction(phrase):
#     phrase_correcte = []

#     for mot in phrase.split():
        
#         mot_correct = spell.correction(mot)
        
#         phrase_correcte.append(mot_correct if mot_correct is not None else mot)
    
#     return ' '.join(phrase_correcte)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "ChatBot"

def get_response(msg):

    # msg = correction(msg)

    sentence = tokenize(msg)
    X = sac_de_mot(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else: 
        return "Je n'ai pas compris votre question, pouvez-vous reformuler ?\nNotez que je suis conçu pour répondre à des questions liées à l'assurance."


if __name__ == "__main__":
    print(f"{bot_name}: Bienvenue! Posez moi toutes vos questions (taper 'exit' pour quitter)")
    while True:
        
        sentence = input("You: ")
        if sentence == "exit":
            break

        # print(correction(sentence))
        
        resp = get_response(sentence)
        print(f"{bot_name}: {resp}")
