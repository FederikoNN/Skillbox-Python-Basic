text_in = input('Сообщение: ')
text_out = []
for word in text_in.split():
    if word.isalpha() is True:
        text_out.append("".join(reversed(word)))
    else:
        word_tmp = ''
        word_change = ''
        for sym in word:
            if sym.isalpha() is True:
                word_tmp += sym
            else:
                word_change += "".join(reversed(word_tmp)) + sym
                word_tmp = ''
        text_out.append("".join(word_change + word_tmp))

print('\nНовое сообщение:', " ".join(text_out))
