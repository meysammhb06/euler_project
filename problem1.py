def Coefficien3or5(n):
    if n % 5 == 0 or n % 3 == 0:
        return True
    else:
        return False 
sum = 0
for i in range (1, 1000):    #checking i in range
    if Coefficien3or5(i):    #checking coefficien is fine for i or not!
        sum = sum + i

print(sum)

#Mcapo