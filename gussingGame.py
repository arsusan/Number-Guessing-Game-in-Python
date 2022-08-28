# Declering veriable
secret_number=7
guess_count=0
guess_limit=3
# Priting notice
print("\tNumber guessing Game\n You will have four option to guess (1 to 20) \n")
while guess_count<=guess_limit: #while loop
    guess=int(input('Guess The secret number:') )#taking input from user
    guess_count +=1
    if guess==secret_number:#if condition for output
        print('\nCongratulation,You Won!\n\n')
        break
else:#output fot 
    print("\nYou missed the number,Let's Try Again:\n")    

print("Thank you for playing game!\n\t Have a Nice day!")
#Written by susan aryal