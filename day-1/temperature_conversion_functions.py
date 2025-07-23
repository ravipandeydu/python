def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

print(celcius_to_fahrenheit(0))  # Example usage
print(fahrenheit_to_kelvin(32))  # Example usage
print(round(kelvin_to_celcius(300), 2))  # Example usage