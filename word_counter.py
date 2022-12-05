import re

TEXT = "Hello there Mike mike"


def word_counter(text):
    words_counted = {}
    cleaned_txt = re.sub(r'[^\w]', ' ', text)
    for word in cleaned_txt.lower().split():
        if word in words_counted:
            words_counted[word] += 1
        else:
            words_counted[word] = 1
    return words_counted


print(word_counter(TEXT))
