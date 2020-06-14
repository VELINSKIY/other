#Python math & time modules
import math
import time

#intro
print("Temperature Converter.  Type C for Celsuis, F for Fahreinheit and K for Kelvin")

def again():
    try_again = print()
    # Letting the user choose the temperature and convert it to another temperature else
    user_temperature = input("Your temperature | C | F | K | ")
    convert_temperature = input("The temperature you want to convert to | C | F | K | ")

    if user_temperature == "C":
        if convert_temperature == "F":
            degree = float(input("enter the degree: "))
            result = (degree * 9/5) + 32
            print(result, "°F.", "The equation is: (", degree, "× 9/5 ) + 32 =", result)
        elif convert_temperature == "K":
            degree = float(input("enter the degree: "))
            result = degree + 273.15
            print(result, "°K.", "The equation is: ", degree, "+ 273.15 =", result)
        elif convert_temperature == "C":
            print("This is the same type of temperature")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()

    elif user_temperature == "F":
        if convert_temperature == "C":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5/9
            print(result, "°F.", "The equation is: (", degree, "- 32 ) × 5/9 =", result)
        elif convert_temperature == "K":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5/9 + 273.15
            print(result, "K°.", "The equation is: (", degree, "- 32 ) × 5/9 + 273.15 =", result)
        elif convert_temperature == "F":
            degree = float(input("This is the same type of temperature"))
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()

    elif user_temperature == "K":
        if convert_temperature == "C":
            degree = float(input("enter the degree: "))
            result = degree - 273.15
            print(result, "°F.", "The equation is: ", degree, "- 273.15 =", result)
        elif convert_temperature == "F":
            degree = float(input("enter the degree: "))
            result = (degree - 273.15) * 9/5 + 32
            print(result, "°K.", "The equation is: (", degree, "- 273.15 ) × 9/5 + 32 =", result)
        elif convert_temperature == "K":
            print("This is the same type of temperature")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()
    else:
        print("Type a temperature")
        time.sleep(1)
        again()

    #asking if the user wants to convert again
    while try_again != "Yes" and try_again != "No":
        print("Do you want to try again?")
        try_again = input("| Yes | No | ")
        if try_again == "Yes":
            again()
            break
        elif try_again == "No":
            print("Goodbye")
            break
        
again()