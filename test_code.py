num = int(input("Enter the number"))
if num>1:
    for i range(2,num):
        if num %i ==0:
            print("its  not a prime_number")
            break

    else:
        print("Its prime number")
else:
    print("print enter the number grater than one")