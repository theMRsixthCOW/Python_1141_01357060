# main
from thelibrary import most_words, most_letter


with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

top_words = most_words(content)
top_letters = most_letter(content)

print(' '.join(top_words))
print(' '.join(top_letters))