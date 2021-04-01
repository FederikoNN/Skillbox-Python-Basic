def string_shift(string, delta):
    delta %= len(string)
    return string[-delta:] + string[:-delta]


# def decrypt_cesar_eng(text, shift):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     return [(alphabet[(alphabet.index(letter) + shift) % 26] if alphabet.count(letter) != 0 else letter) for letter in
#             text]

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_encrypt = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
# text_encrypt = [letter for letter in text_encrypt if letter.isalpha()]
# a=text_encrypt.split('/*')
text_decrypt = []
string_out = []
shift = 3
for string in text_encrypt.split('/'):
    for word in string:
        string_out.append(string_shift(word, shift))
    print(string_out[-1])
    print(string_out[-2])
# print(text_decrypt)
    shift += 1
text_decrypt = [(alphabet[(alphabet.index(letter) + 51) % 52] if alphabet.count(letter) != 0 else letter) for letter
                in " ".join(string_out)]

print("".join(text_decrypt))
# shift = 3
# word = 'vujgvmCfb'
# shift %= len(word)
# print(word[-shift:] + word[:-shift])
