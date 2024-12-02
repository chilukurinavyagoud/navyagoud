# weight coverter pgm
weight = float(input("Enter your weight:"))
unit = input("Is this weight kilograms or pounds?(K or L)")

if(unit == "k"):
    weight = weight * 2.205
    print(f"The weight of ponds is: {round(weight,1)} Lbs.")
elif(unit == "L"):
    weight = weight / 2.205 
    print(f"The weight of kilograms is: {round(weight,2)} Kgs.")



