print("pushing code into feature_dev , feature_dev")


num = int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if num %i==0:
            print("Its not a prime numner")
            break
        else:
            print("Its a prime number")
else:
    print("Enter the number grater than one")