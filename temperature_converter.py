def convert_temperature(value, scale):
    if scale.lower() == "c":
        return (value * 9/5) + 32, value + 273.15
    elif scale.lower() == "f":
        celsius = (value - 32) * 5/9
        return celsius, celsius + 273.15
    elif scale.lower() == "k":
        celsius = value - 273.15
        return celsius, (celsius * 9/5) + 32
    else:
        return None

value = float(input("Enter temperature value: "))
scale = input("Enter scale (C/F/K): ")

result = convert_temperature(value, scale)

if result:
    print(f"Converted values: {result}")
else:
    print("Invalid scale.")
