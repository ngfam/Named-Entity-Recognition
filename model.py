import math
import numpy as np
from tagReader import process
from testReader import readData

inf = -100000000
emission, ngram = process()

all = 0
correct = 0

for sentence in readData():
    sentence.append(("</s>", ">"))
    n = len(sentence)

    # tag preparer
    tags = []
    for word in sentence:
        tags.append(emission.query(word[0]))
    beginTag = emission.query("<s>")


    # dynamic programming initialized
    f = [None] * (n + 1)
    trace = [None] * (n + 1)
    f[0] = [[1.0]]
    trace[0] = [[0]]

    for i in range(n):
        tag = tags[i]
        tag1 = None
        tag2 = None

        if i > 0:
            tag1 = tags[i - 1]
        else:
            tag1 = beginTag
        
        if i > 1:
            tag2 = tags[i - 2]
        else:
            tag2 = beginTag
        
        f[i + 1] = inf * np.ones((len(tag1), len(tag)), float)
        trace[i + 1] = np.zeros((len(tag1), len(tag)), int)

        for j in range(len(tag2)):
            for k in range(len(tag1)):
                for h in range(len(tag)):
                    emiProb = tag[h][1]
                    cohProb = ngram.query(tag2[j][0], tag1[k][0], tag[h][0])
                    # because the data set is pretty much weird, so ill *halve* the contribution of cohProb
                    finalProb = math.log2(emiProb * math.pow(emiProb * emiProb * emiProb * emiProb * cohProb, 1/5))
                    # finalProb = math.log2(emiProb)

                    if f[i + 1][k][h] < f[i][j][k] + finalProb:
                        f[i + 1][k][h] = f[i][j][k] + finalProb
                        trace[i + 1][k][h] = j
                    
    
    #Trace the best arg
    bestx = 0
    besty = 0

    for x in range(len(tags[n - 2])):
        for y in range(len(tags[n - 1])):
            if f[n][x][y] > f[n][bestx][besty]:
                bestx = x
                besty = y
    
    tagResult = []
    for i in range(n, 0, -1):
        tagResult.append(tags[i - 1][besty][0])
        temp = trace[i][bestx][besty]
        besty = bestx
        bestx = temp
    
    tagResult.reverse()
    tagResult.pop()

    for i in range(n - 1):
        # if sentence[i][1] == 'O' and tagResult[i] == 'O':
        #     continue
    
        all += 1
        if tagResult[i] == sentence[i][1]:
            correct += 1


print(correct / all)

