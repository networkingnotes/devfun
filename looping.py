#looping test
#this program tests if a number is prime or not

testNum = int(input("Enter an integer to for prime: "))
if testNum > 1:
    for i in range (2, testNum):
        if (testNum % i) == 0:
            print(testNum, "is not a prime number")
            print(i,"time",testNum//i,"is",testNum)
            break
    else:
        print(testNum, "is a prime number")
else:
        print("You must enter an integer.")
