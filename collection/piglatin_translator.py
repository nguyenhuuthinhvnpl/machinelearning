message = "this is a statement in english"
# a starting consonant sound in your word moves to the end of the word followed by "ay"
# This -> isthay
# If the word starts with a wovel, then we add "way" to the end
# other -> otherway

translation = {}
translation["this"] = "isthay"
translation["statement"] = "atementstay"
translation['english'] = 'englishway'

words = message.split()
print(words)

for word in words:
    if word in translation.keys():
        print(translation[word])
    else:
        print(word)
