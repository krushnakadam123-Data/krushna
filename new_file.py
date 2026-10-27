num = int(input("Enter the number:"))

if num >1:
    for i in range(2,num):
        if num % i==0:
            print("not a prime number")
            break
        else:
            print("its a prime number")
else:
    print("enter the program grater than 1")