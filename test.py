
print("welcome to pune,pushing code into feature_dev")
#prime number programe
num = int(input("Enter the number: "))
if num >1:
    for i in range(2,num):
        if num %i ==0:
            print("Not a prime number")
            break
    else:
        print("its prime number")
else:
    print("Enter the number grater then one")