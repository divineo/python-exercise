#code in python3
#checking if a number is a palindrome
#done using str() and sting slicing. Very easy :)

val = input("Enter the number: ")

#checking the number. string slicing is a method which reverses string. 
test = str(val) == str(val)[::-1]

#Output whether true or false
print("Is it a palindrome? : " + str(test))
