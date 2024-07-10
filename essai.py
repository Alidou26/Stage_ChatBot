from spellchecker import SpellChecker

spell = SpellChecker(language='fr')

def correction(phrase):
    phrase_correcte = []

    for mot in phrase.split():
        
        mot_correct = spell.correction(mot)
        
        phrase_correcte.append(mot_correct if mot_correct is not None else mot)
    
    return ' '.join(phrase_correcte)


while True:
        
        phrase = input()
        if phrase == "exit":
            break

        resp = correction(phrase)
        print(resp)