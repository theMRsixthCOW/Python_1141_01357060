import re

def most_words(context):
    words = re.findall(r'[a-zA-Z]+', context.lower())
    
    count = {}
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    return [f"{word} {cnt}" for word, cnt in sorted_items[:3]]


def most_letter(context):
    # 轉小寫
    letters = [c.lower() for c in context if c.isalpha()]
    
    count = {}
    for c in letters:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    
    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    # 前三名
    return [f"{char} {cnt}" for char, cnt in sorted_items[:3]]