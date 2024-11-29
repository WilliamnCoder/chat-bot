
name = input("Hello! What is your name? ")  #Name variable and print statement with f-string based on answer
print(f"Nice to meet you, {name}!")

age_input = input("How old are you? ") #Age variables defined and the print statements 
age = int(age_input)
bot_age = 20
age_difference = age - bot_age   #The age difference number that will be printed in the next code line (9)
print(f"You are {age_difference} years older than me. I am only {bot_age} years old!")

color = input("What is your favorite color? ")  #Color variable defined and its print statements
print(f"Oh, {color} is a beautiful color!") 

review = input("Please leave a review about this chat bot. Was it helpful? ") 
while review != "Yes" and review != "No":
    print("Sorry. You have to answer 'Yes' or 'No' ")
    review = input("Please leave a review about this chatbot. Was it helpful? (Yes/No) ")

if review == "Yes":
    print ("Thank you, we will improve it even more. ")
elif review == "No":
    print("Thank you, how can we improve it even more?")
else:
    print("Invalid answer. Please type 'Yes' or 'No' ")


while True:   # The program is running until the user have entered 1-5
    answering_review = input("Thank you for your review. It is very helpful! Now please give a rating from 1-5! ")
    
    if answering_review == "1" or answering_review == "2":
        print (f"We are sorry that you only gave it {answering_review}. ")
        break   #break is for exiting the loop once 1-5 is entered
    elif answering_review == "3":
        print(f"Thank you for a {answering_review}, that is a decent rating!")
        break
    elif answering_review == "4":
        print(f"Wow! Really, a {answering_review}? Almost full rating. ")
        break
    elif answering_review == "5":
        print(f"Amazing! {answering_review} out of {answering_review}! ")
        break
    else:
        print("Invalid answer. It must be a number between 1-5. ")
        answering_review = input("Now please give a rating from 1-5! ")


