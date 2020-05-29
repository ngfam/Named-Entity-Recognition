from dataReader import readData
from DataStructures.ngram import ngram
from DataStructures.Emission import Emission

def process():
    a = Emission()
    b = ngram()

    a.insert('<s>', '<')
    a.insert('</s>', '>')

    for sentence in readData():
        previous1 = "<"
        previous2 = "<"
        sentence.append(("</s>", ">"))

        for words in sentence:
            a.insert(words[0], words[1])
            b.insert(previous1, previous2, words[1])
            previous1 = previous2
            previous2 = words[1]

    a.process()
    return (a, b)

process()