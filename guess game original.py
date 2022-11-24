print('                                          ')
print("NOTICE! IT'S OKAY EVEN IF THE ANSWER IS CAPITALIZED OR IN UPPERCASE OR NOT, AND DON’T FORGET WRONG SPELLING IS WRONG")
print('                                          ')
print('********* WORD GUESSING GAME *********')
print('                                          ')
print('*Choose category')
print('                                          ')
print('1. Animals')
print('2. Country')
print('3. Vegetable')
print('                                          ')
print('Number only')
choice = input('what is your choice?: ')
print('                                          ')
score = 0
if choice == '1':
    print('                                          ')
    print('!!!!ANIMALS!!!!')
    print('1. --n-s-or')
    print('2. K-n---o-')
    print('3. -l----nt')
    print('4. gi-r-f-')
    print('5. --k-y')
    print('                                          ')
    w1 = input('Guess the 1st word: ')
    if w1 == 'dinosaur'.capitalize() or w1 == 'dinosaur'.upper() or w1 == 'dinosaur':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score+1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w2 = input('Guess the 2nd word: ')
    if w2 == 'kangaroo'.capitalize() or w2 == 'kangaroo'.upper() or w2 == 'kangaroo':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score+1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w3 = input('Guess the 3rd word: ')
    if w3 == 'elephant'.capitalize() or w3 == 'elephant'.upper() or w3 == 'elephant':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score+1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w4 = input('Guess the 4th word: ')
    if (w4 == 'giraffe'.capitalize()) or (w4 == 'giraffe'.upper()) or (w4 == 'giraffe'):
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score+1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w5 = input('Guess the 5th word: ')
    if w5 == 'monkey'.capitalize() or w5 == 'monkey'.upper() or w5 == 'monkey':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score+1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    print('                                          ')
    print('-----ANSWER----- ')
    print('1. Dinosaur')
    print('2. Kangarooo')
    print('3. Elephant')
    print('4. Giraffe')
    print('5. Monkey')
    print('                                          ')
    pass
elif choice == '2':
    print('!!!!COUNTRY!!!!')
    print('1. -h--i-p-n--')
    print('2. i-d--')
    print('3. -r-z-l')
    print('4. f--n-')
    print('5. -a-b-d-a')
    print('                                          ')
    w1 = input('Guess the 1st word: ')
    if w1 == 'philippines'.capitalize() or w1 == 'philippines'.upper() or w1 == 'philippines':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w2 = input('Guess the 2nd word: ')
    if w2 == 'india'.capitalize() or w2 == 'india'.upper() or w2 == 'india':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w3 = input('Guess the 3rd word: ')
    if w3 == 'brazil'.capitalize() or w3 == 'brazil'.upper() or w3 == 'brazil':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w4 = input('Guess the 4th word: ')
    if w4 == 'france'.capitalize() or w4 == 'france'.upper() or w4 == 'france':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w5 = input('Guess the 5th word: ')
    if w5 == 'cambodia'.capitalize() or w5 == 'cambodia'.upper() or w5 == 'cambodia':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    print('                                          ')
    print('-----ANSWER----- ')
    print('1. Philippines')
    print('2. India')
    print('3. Brazil')
    print('4. France')
    print('5. Cambodia')
    print('                                          ')
    pass
elif choice == '3':
    print('!!!!VEGETABLE!!!!')
    print('1. -o-a-o')
    print('2. --rn')
    print('3. G-ng--')
    print('4. O-i--')
    print('5. C--b-g-')
    print('                                          ')
    w1 = input('Guess the 1st word: ')
    if w1 == 'tomato'.capitalize() or w1 == 'tomato'.upper() or w1 == 'tomato':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w2 = input('Guess the 2nd word: ')
    if w2 == 'corn'.capitalize() or w2 == 'corn'.upper() or w2 == 'corn':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w3 = input('Guess the 3rd word: ')
    if w3 == 'ginger'.capitalize() or w3 == 'ginger'.upper() or w3 == 'ginger':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w4 = input('Guess the 4th word: ')
    if w4 == 'onion'.capitalize() or w4 == 'onion'.upper() or w4 == 'onion':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    w5 = input('Guess the 5th word: ')
    if w5 == 'cabbage'.capitalize() or w5 == 'cabbage'.upper() or w5 == 'cabbage':
        print('                                          ')
        print('----Correct guess----')
        print('                                          ')
        score = score + 1
    else:
        print('                                          ')
        print('***Wrong guess***')
        print('                                          ')
    print('                                          ')
    print('-----ANSWER----- ')
    print('1. tomato')
    print('2. corn')
    print('3. ginger')
    print('4. onion')
    print('5. cabbage')
    print('                                          ')

else:
    print("Please Select only from the selection Thankyou!")
    exit()

if score == 5:
    print('YEHEY! you got', score, 'Perfect score')
elif score >= 3:
    print('Great you got', score, 'score')
else:
    print('So sad you got', score, 'Bawi nextlife thankyou!')
    print('                                          ')
    print('-----Game Over------')
