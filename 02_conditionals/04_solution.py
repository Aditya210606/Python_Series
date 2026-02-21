pet = input("Enter pet (dog/cat): ").lower()
age = int(input("Enter pet age: "))

if pet == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif pet == "cat":
    if age < 5:
        print("Cat food")
    else:
        print("Senior cat food")


