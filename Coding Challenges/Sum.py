#WAP to sum the two digit indiviually i.e 42 , 4+2= 6
two_digitnum = input("enter two digit number ")
first=two_digitnum[0]
second =two_digitnum[1]
print(first)
print(type(first))
result = int(first) + int(second)
print("Your sum is :" + str(result))
