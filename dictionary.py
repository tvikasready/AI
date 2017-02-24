import sys

class Synonym:
    meaningless = {'anger':0.85,
                'disgust':0.79,
                'fear':0.67,
                'happiness':0.44,
                'sadness':0.56,
                'surprise':0.22}
    beautiful = {'anger':0.05,
                'disgust':0.1,
                'fear':0.07,
                'happiness':0.80,
                'sadness':0.02,
                'surprise':0.5}
    running = {'anger':0.30,
                'disgust':0.40,
                'fear':0.40,
                'happiness':0.30,
                'sadness':0.35,
                'surprise':0.1}

    dictionary = {'beautiful':beautiful,'meaningless':meaningless,'running':running}
    emotions = {}
    def emo(self,word):
        for self.key,self.value in self.dictionary.items():
            self.emotions[self.value[word]] = self.key
            #print(self.key)

        print (self.emotions)

        for key,value in sorted(self.emotions.items(),reverse = True):
            print(value)

         
            

    
if __name__ == "__main__":
    syn = Synonym()

    word = input("Enter the word: ")
    print ("The order for emotions of the word "+word+" is")
    #emotion = {}
    #emotion.update(syn.dictionary[word])
    
   # for key, value in sorted(emotion.items(),key=lambda kv: kv[1], reverse=True):
       # print(key, value)
    #emotion.clear()
    syn.emo(word)
    
