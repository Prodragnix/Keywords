def find():
    word=input('Please enter your word:  ')
    for i in word:
        if i=='a':
            print('The letter A is found!')
            break
        else:
            print('A is not found!')
find()