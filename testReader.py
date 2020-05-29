import logger

UD_VIETNAMESE_TEST = './Datas/test.conll'
def readData():
    training_file = open(UD_VIETNAMESE_TEST, "r")
    
    sentence = []
   
    while True:
        a = training_file.readline()
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
