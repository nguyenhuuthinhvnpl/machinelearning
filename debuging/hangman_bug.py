phrase = input("Enter a word or phrase:").lower()
data = '_'.join(phrase) + '_'

wrong = 0
while '_' in data and wrong < 6:
    print('The thing to guess', data[1::2])
    letter = input('What the letter ?').lower()
    while len(letter) != 1:
        letter = input('What letter ?')
    odata = data
    data.replace(letter + '_', letter + letter)
    if odata == data:
        wrong += 1
        print('Sorry, there was no letter', letter, 'in the phrase')
    else:
        print('Good guess')

    run += 1

if '_' in data:
    print('You lose; it was', phrase)
else:
    print('You won in', run, ' steps. The answer was', phrase)
