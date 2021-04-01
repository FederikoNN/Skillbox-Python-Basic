text_in = input('Сообщение: ')
text_out = []
for word in text_in.split():
    if word.isalpha() is True:
        text_out.append("".join(reversed(word)))
    else:
        text_out.append("".join(reversed(word[:-1])) + word[-1:])

print('\nНовое сообщение:', " ".join(text_out))
