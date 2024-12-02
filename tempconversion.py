#coversion of temperature

unit = input("Is this temperature Celcius or fahrenhit?")
temp = float(input("Enter the temperature:"))
if unit == "Celcius":
    temp = round((temp*9)/5+32)
    print(f"the temperature in fahrenhit is: {temp}°F")
elif unit == "fahrenhit":
    temp = round((temp -32)*5/9,1)
    print(f"the temperature in Celcius is:{temp}°C")
else:
    print(f"the {unit} is an invalid measurement")
