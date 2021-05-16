import nltk
import re
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import Counter, OrderedDict

text = """Os governos de China e Argentina ampliaram neste domingo (2), em Buenos Aires, a sua associação estratégica com a assinatura de 30 acordos de comércio e investimentos, em uma cerimônia liderada pelos presidentes Xi Jinping e Mauricio Macri. <SENTENÇA 1>

    “Fortalecemos a cooperação em matéria econômica, agrícola, de infraestrutura e financeira, entre outros campos. O objetivo é promover a longa amizade entre os dois povos”, disse Xi em um evento na residência presidencial argentina em Olivos, na periferia norte. <SENTENÇA 2>

    Além disso, Macri disse que a assinatura de uma declaração conjunta demonstra “o importante consenso alcançado em termos de desenvolvimento em longo prazo. Foi uma reunião muito produtiva”, detalhou. <SENTENÇA 3>

    Xi foi o único presidente estrangeiro a concluir uma visita de Estado ao país sul-americano, enquanto era realizada a cúpula do G20, que terminou neste sábado (dia 1º). <SENTENÇA 4>"""

sents = sent_tokenize(text)

words = word_tokenize(text)

stops = stopwords.words('portuguese')

punctuation = list(punctuation)

stops.extend(punctuation)

words = list(filter(lambda word: word not in stops, words))

freq = FreqDist(words)

PATTERN = r"""\w+\-+\w+|\w+|['"]{1}"""

def my_tokenizer(input_string):
    return re.findall(PATTERN, input_string)

def token_counter(input_tokens):
    return Counter(input_tokens)

def ordered_counter(input_tokens):
    tok = OrderedDict(Counter(input_tokens))
    return OrderedDict(sorted(tok.items(), key=lambda x: x[1], reverse=True))

print(ordered_counter(my_tokenizer(text)))
