# Converts Celsius to Fahrenheit.

def to_fahrenheit(c):
    return c * 9 / 5 + 32


def to_kelvin(c):
    return c + 273.15

def to_reamur(c):
    return c* 4/5

def main():
    global celsius
    try:
        celsius = float(input("Enter temperature in Celsius: "))
    except ValueError:
        print("Error: please enter a number.")
        return

    if celsius < -273.15:
        print("Error: below absolute zero.")
        return

main()
print(f"Fahrenheit: {to_fahrenheit(celsius):.1f} F")
print(f"Kelvin: {to_kelvin(celsius):.2f} K")
print(f"Reaumur: {to_reamur(celsius):.1f} Re")