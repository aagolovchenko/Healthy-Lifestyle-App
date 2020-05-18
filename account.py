def registration():
    print("\n", "Welcome to the Healthy Lifestyle app", "\n", "Please, fill in the registration form:")
    name = input("Name: ")
    age = int(input("Full age: "))
    weight = int(input("Weight in kilos: "))
    hight = int(input("Hight in santimetres: "))
    type_of_lifestyle = input("Type of lifestyle (active/not active): ")


def start_of_program():
    print("\n", "Would you like to:", "\n", "a) Lose weight", "\n", "b)Gain weight", "\n", "c)Stay the same")
    wish = input("Chose a-c: ")


registration()
start_of_program()
