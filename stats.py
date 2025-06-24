
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_words_count(filepath):
    with open(filepath) as f:
        count = len(f.read().split())
        return f"{count}"

def get_character_count(filepath):
    res = {}
    text = get_book_text(filepath)
    text = text.lower()
    for znak in text:
        if znak in res:
            res[znak] += 1
        else:
            res[znak] = 1
    return res

def sort_on(item):
    return item["num"]

def get_sorted_dict(counts):
    res = []
    for char, count in counts.items():
        if char.isalpha():
            res.append({"char": char, "num": count})

    res.sort(reverse=True, key=sort_on)
    return res
    
    