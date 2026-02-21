number = int(input("Enter a number to check even or not :" ))

even_number = 0 

for i in range (1,number+1):
    if i%2 == 0 :
        even_number +=1 

print("Count of even numbers are :" ,even_number)        