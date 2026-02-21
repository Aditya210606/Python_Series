input_str = str(input("Enter a string :"))

for char in input_str:
    print(char)
    if input_str.count(char) == 1 :
        print("Char is ",char) 
        break # breaks the loop if the solution is found 