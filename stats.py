
def wordcount(filepath):
    with open(filepath) as f:
        words = f.read().split()
        return len(words)

def charactercount(filepath):
    with open(filepath) as f:
        characters = {}
        for c in f.read():
            c = c.lower()
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1
        return characters

