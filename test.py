
num = int(input("Enter the number: "))

if num >1:
    for i in range(2,num):
        if num % i ==0:
            print("its not a prime number")
            break
    else:
        print("prime number")
else:
    print("enter the number grater than one")
