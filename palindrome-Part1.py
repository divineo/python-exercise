#Python3 code
#checking for palindrome
#using while loop

val = int(input("Enter the number: "))

flip = 0
temp = val

while(temp > 0):
	remainder = temp % 10
	flip = (flip * 10) + remainder
	temp = temp // 10

if(val == flip):
	print("It is a palindrom")

else:
	print("Not a palindrome")
