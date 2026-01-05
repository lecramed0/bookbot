# sort helper
def sort_on(items):
    return items["num"]

# functions
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

def character_report(characters):
    character_report = []
    for character, count in characters.items():
        if character.isalpha():
            character_summary = {
                    "char": character,
                    "num": count
                    }
            character_report.append(character_summary)

    # sort helper
    def sort_on(items):
        return items["num"]

    # NOTE: a_list.sort() return None, so you can assign it to
    # a variable or return it. You must sort in place then return.
    character_report.sort(reverse=True, key=sort_on)

    return character_report
