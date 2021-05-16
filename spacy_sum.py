import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Os governos de China e Argentina ampliaram neste domingo (2), em Buenos Aires, a sua associação estratégica com a assinatura de 30 acordos de comércio e investimentos, em uma cerimônia liderada pelos presidentes Xi Jinping e Mauricio Macri.

    “Fortalecemos a cooperação em matéria econômica, agrícola, de infraestrutura e financeira, entre outros campos. O objetivo é promover a longa amizade entre os dois povos”, disse Xi em um evento na residência presidencial argentina em Olivos, na periferia norte.

    Além disso, Macri disse que a assinatura de uma declaração conjunta demonstra “o importante consenso alcançado em termos de desenvolvimento em longo prazo. Foi uma reunião muito produtiva”, detalhou.

    Xi foi o único presidente estrangeiro a concluir uma visita de Estado ao país sul-americano, enquanto era realizada a cúpula do G20, que terminou neste sábado (dia 1º)."""


stopwords = list(STOP_WORDS)
nlp = spacy.load('pt_core_news_sm')
doc = nlp(text)
tokens = [token.text for token in doc]
print(tokens)

punctuation = punctuation = punctuation + '\n'
#print(punctuation)

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] = word_frequencies[word.text] + 1

#print(word_frequencies)


max_frequency = max(word_frequencies.values())
#print(max_frequency)

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
    print(word_frequencies[word])

sentence_tokens = [sent for sent in doc.sents]

#print(sentence_tokens)

sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

#print(sentence_scores)

select_length = int(len(sentence_tokens)*0.3)

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

print(summary)
