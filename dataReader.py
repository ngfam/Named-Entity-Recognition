import logger

maxChar = 0
alphabet = {'a'}

UD_VIETNAMESE_TRAIN = './Datas/train.conll'
def readData():
    training_file = open(UD_VIETNAMESE_TRAIN, "r")
    
    sentence = []
   
    while True:
        a = training_file.readline()
        # print(a, len(a))
        if len(a) == 0:
            yield sentence
            break
        
        if len(a) == 1:
            yield sentence
            sentence.clear()
            continue

        
        words = a.split()
        if len(words) < 2: 
            continue

        sentence.append((words[0], words[1]))

        for c in words[0]:
            alphabet.add(c)
