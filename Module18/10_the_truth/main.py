def string_shift(string, delta):
    delta %= len(string)
    return string[-delta:] + string[:-delta]


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_encrypt = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

for word in text_encrypt.split():
    if word.find('/') != -1:
        text_encrypt = text_encrypt.replace(word + " ", word + "\n ")

text_decrypt = []
shift = 3
for string in text_encrypt.splitlines():
    for word in string.split():
        text_decrypt.append(string_shift(word, shift))
    text_decrypt.append('\n')
    shift += 1

text_decrypt = [(alphabet[(alphabet.index(letter) + 51) % 52] if alphabet.count(letter) != 0 else letter) for letter
                in " ".join(text_decrypt)]

print("".join(text_decrypt).replace('/', '.').replace('..', '').replace('+', '').replace('(', "'"))
