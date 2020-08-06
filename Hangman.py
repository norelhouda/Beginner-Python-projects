import random

word_list = ['javascript', 'java', 'kotlin', 'python']
choice = random.randint(0, 3)
word = word_list[choice]
valid_entries = set('abcdefghijklmnopqrstuvwxyz')
tries = set()
count = 8

# word_hint = word[0:3] + '-' * (len(word)-3)
hint = list('-' * len(word))
print('H A N G M A N\n')
while count > 0:
    cur_answer = ''.join(hint)
    print("\n" + cur_answer)
    guess = input('Input a letter: ')
    if len(guess) != 1:
        print('You should input a single letter') 
        continue
    elif guess not in valid_entries:
        print('It is not an ASCII lowercase letter')
        continue
    elif guess in tries:
        print('You already typed this letter')
        continue
    elif guess not in word:
        print('No such letter in the word')
        count -= 1
        tries.add(guess)
        continue
    elif guess in word:
        for j in range(len(word)):
            if guess == word[j]:
                hint[j] = guess
        tries.add(guess)
    if cur_answer == word:
        print('You guessed the word ' + word)
        print('You survived!')
        break
else:
    print('You are hanged!')
