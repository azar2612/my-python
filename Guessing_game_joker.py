secret_word = "joker"
guess  = " "
guess_count =0
guess_limit =3
out_of_guesses = False 

print(not(out_of_guesses))

while guess != secret_word and not(out_of_guesses):
     
     if guess_count<guess_limit:
         guess = input("enter guess: ")
         guess_count +=1
     else:
         out_of_guesses = True

print((out_of_guesses))

if out_of_guesses:
    print("out_of_guesses , you lose")
else:
    print("you win") 