"""
This code is about going to the giutar center, you are either shopping or repairing your guitar
you will get a guitar model of your color of choice, or repair your guitar strings or main body
"""
welcome=str(input("Welcome to Guitar Center! Are you here for shopping or repairing? "))
# please say exactly "repairing" or "shopping", no caps and correct spelling
if welcome=="shopping":
    brand=str(input("What guitar brand would you like? "))
    # Say either "Fender" or "Gibson", exact spelling

if brand=="Fender":
    model=str(input("What model? "))
    color=str(input("What color? "))
    # Say either "Stratocaster" for model and "Red" for color or "Jaguar" and "Blue"
else:
    model2=str(input("What Gibson model? "))
    color2=str(input("What color? "))
    # Say either "SG" for model and "Red" for color or "Les Paul" and "Sunset"

# This will either give you a red Strat, a blue Jaguar, or nothing
if model=="Stratocaster" and color=="Red":
    print("Here's your red Stratocaster!")
elif model=="Jaguar" and color=="Blue":
    print("Here's your blue Jaguar!")
elif model2=="SG" and color2=="Red":
    print("Here's your Red SG!")
elif model2=="Les Paul" and color2=="Sunset":
     print("Here's your Les Paul!")
else:
    print("Sorry, that is not available.")

# Say either "yes" or "no"
repairing=str(input("Do you need any repairing? "))
if repairing=="yes":
    print("Of course! We'll call our best workers! ")
else:
    print("Ok")

# This code asks if you need a distortion pedal and will either give you one or not
pedal=str(input("Do you need a distortion pedal? "))
if pedal=="yes":
    print("Here are our best pedals and pedalboards?")
else:
    print("Ok, thanks!")

    
