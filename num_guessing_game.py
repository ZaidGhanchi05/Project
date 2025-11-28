import random
num = random.randint(1,1000)
count=1
print("---------Guess The number Between 1-1000.-------")
while True:
    try:
        user_num = int(input("Guess : "))
        if user_num == num:
            print(f"Congratulations...You've Guessed it right in {count} guesses..🏆")
            break
        elif user_num > num:
            print("Guess Lower..")
            count+=1
        elif user_num < num:
            print("Guess Higher..")
            count+=1
    except:
        print("Give Valid Input.")