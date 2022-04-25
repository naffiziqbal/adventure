# Welcome note
name = input("Enter Your Name Please ")
print("Welcome To The Adventure", name)

answer = input("Your Adventure life has just started, Do you Want to "
               "Continue? Write 'Yes' Or 'No'  ").lower()
if answer == "yes":
    answer = input("Ok You have a River Ahed. What do you Want to Do?  Go "
                   "back or Swim?  Write 'Swim' to Swim and Write 'back' if "
                   "you want to go back and Check whether there's any "
                   "alternative way or not!").lower()
    if answer == "swim":
        print("Swimming")
        print("Enough Swamed")
        answer = input("You, Swam Across the River. You Have Two Choices "
                       "now, Go to 'Straight' and Go to 'Right'").lower()
        if answer == "straight":
            print("Walking......")
            answer = input("Do You see a Guy Standing next to that "
                           "building? Write 'Yes' If you saw him and 'No' if "
                           "You Didn't ").lower()
            if answer == "yes":
                print("Hurrah! You won")
            elif answer == "no":
                print("Keep Walking......")
        elif answer == "right":
             quit("Danger Ahed Run.........")

    elif answer == "back":
        quit("There is no way Back! You Lost")

elif answer == "no":
     quit("Okay! we'll Play again")
else:
    print("Not A valid Option")

print("To be Continue ......")
