import sys

class Synonym:
    meaningless = {'Anger':0.85,
                'Disgust':0.79,
                'Fear':0.67,
                'Happiness':0.44,
                'Sadness':0.56,
                'Surprise':0.22}
    beautiful = {'Anger':0.05,
                'Disgust':0.1,
                'Fear':0.07,
                'Happiness':0.80,
                'Sadness':0.02,
                'Surprise':0.5}
    running = {'Anger':0.30,
                'Disgust':0.40,
                'Fear':0.40,
                'Happiness':0.30,
                'Sadness':0.35,
                'Surprise':0.1}

    dictionary = {'beautiful':beautiful,'meaningless':meaningless,'running':running}

    
if __name__ == "__main__":
    syn = Synonym()

    word = input("Enter the word: ")
    print ("The emotions of the word "+word+" is")
    emotion = {}
    emotion.update(syn.dictionary[word])
    for key, value in emotion.items():
        print(key, value)
    emotion.clear()
    
