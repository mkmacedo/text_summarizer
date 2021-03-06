from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from sys import stdin

#text = stdin.read()

class Summarizer:
    def __init__(self, text):
        self.text = text
        self.sents = sent_tokenize(text)
        self.words = word_tokenize(self.text)
        self.stops = stopwords.words('portuguese')
        self.punctuation = list(punctuation)
        self.stops.extend(punctuation)
        self.words = list(filter(lambda word: word not in self.stops, self.words))
        for i in range(len(self.words)):
            self.words[i] = self.words[i].lower()
        self.freq = self.normalize_freq(FreqDist(self.words))

    def normalize_freq(self, freq):
        for word in freq.keys():
            freq[word] = freq[word]/max(FreqDist(self.words).values())
        return freq

    def grade_sentence(self):
        sent_scores = {}
        for sentence in self.sents:
     
            split_sentence = sentence.split()
            for word in split_sentence:
                if word.lower() in self.freq.keys():
                    if sentence not in sent_scores.keys():
                        sent_scores[sentence] = self.freq[word.lower()]
                    else:
                        sent_scores[sentence] += self.freq[word.lower()]
      
        return sent_scores

    def summary(self):
        n_sentences = len(self.sents)
        temp = int(n_sentences*0.3)

        selected_length = temp if temp >= 2 else n_sentences
         
        sent_scores = self.grade_sentence()
       
        temp_summary = nlargest(selected_length, sent_scores, key=sent_scores.get)
        
        final_summary = []
        for sentence in self.sents:
            if len(final_summary) < selected_length:
                if sentence in temp_summary:
                    final_summary.append(sentence)
            else:
                break

        final_summary = ''.join(final_summary)

        return final_summary


#x = Summarizer(text)

#print(x.summary())
#print(len(x.summary()))
#print(len(text))
