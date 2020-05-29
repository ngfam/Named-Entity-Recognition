# TODO: 
## Rebuild this code with normal map implementation 
### Why not trie :<




class Emission:
    def __init__(self):
        self.tags = dict()
        self.countTag = dict()

    def insert(self, key, tag):
        if key not in self.countTag:
            self.countTag[key] = dict()
        if tag not in self.countTag[key]:
            self.countTag[key][tag] = 0
        self.countTag[key][tag] += 1

        if key != '<unk>':
            self.insert('<unk>', tag)
    
    def process(self):
        for key in self.countTag:
            self.tags[key] = []
            total = 0
            for tag in self.countTag[key]:
                total += self.countTag[key][tag]
            for tag in self.countTag[key]:
                self.tags[key].append((tag, self.countTag[key][tag] / total))
        
    def query(self, word):
        if word not in self.tags:
            word = '<unk>'
        return self.tags[word]

