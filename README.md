# Named Entity Recognition

This model was implemented based on the algorithms described in: https://bit.ly/2Mnmv0F

This time the training data was fairly small, so emplementing Trie does not seem to be needed (especially with the alphabet size of Vietnamese).

## Statistical Review

Although the algorithms described seems fancy, the efficiency in contrast was not impressive. 

I have collected some statistical data of this model, based on two values:

1. The overall probability of tags being correct
2. The probability of tags being correct when at least one of tags (generated by the model and the correct result) is not ```'O'```.

The second factor happened cause it seemed pretty obivous to me that most of the tags are ```'O'```. 

Using the algorithm described:
1. 90.01%
2. 29.36%

Since I notice that most of the tags are ```'O'```, so maybe the transition probability will be very little for other tags. As a result, I made one change to the formula while finding the max arg: ```emission * pow(emission ^ 4 * transition)```

This fortunately gave a better result:
1. 91.02%
2. 37.85%

## Usage

¯\_(ツ)_/¯