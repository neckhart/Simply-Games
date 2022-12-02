print("Welcome in my units_converter, use and enjoy it!")
print()

type_of_units = {
    "kilometr" : "km", 
    "meter" : "m",
    "centymeter" : "cm",
    "milimeter" : "mm"}

for keys,value in type_of_units.items():
    print(f"Unit format example: {value}")
print()

number_of_units = float(input("Write number of units: "))
start_unit = str(input("Write symbol of unit which would you like to convert: ")).lower()
finish_unit = str(input("Write symbol of unit which would you like to recive: ")).lower()

print(f"Convert: {number_of_units} {start_unit} to {finish_unit}")

match start_unit:
    case 'km':
        if finish_unit == 'm':
            result = number_of_units * 10**3
        elif finish_unit == 'cm':
            result = number_of_units * 10**5
        else:
            result = number_of_units * 10**6     
    case 'm':
        if finish_unit == 'km':
            result = number_of_units / 10**3
        elif finish_unit == 'cm':
            result = number_of_units * 10**2
        else:
            result = number_of_units * 10**3
    case 'mm':
        if finish_unit == 'km':
            result = number_of_units / 10**6
        elif finish_unit == 'm':
            result = number_of_units / 10**3
        else:
            result = number_of_units / 10
print(f"{number_of_units} {start_unit} is equal: {result:,} {finish_unit}") 