#!/usr/bin/env python3
#!/usr/bin/env python3
  
round = 0

round = round + 1
print('Finish the movie title, "Monty Python\'s The Life of ------"')

answer = input ("Your guess--> ")

if answer == 'Brian':
    print('Correct!')
    #break
elif round == 3:
    print("sorry, the answer was Brian.")
    #break
else:
    print("Sorry! Try again")
