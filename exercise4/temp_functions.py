# create function to classify temperature
def temp_classifier(temp_celsius):
    # classify temperature into four classes according to the given criteria
    if temp_celsius < -2:
        return 0
    elif -2 <= temp_celsius < 2:
        return 1
    elif 2 <= temp_celsius < 15:
        return 2
    else:
        return 3
    
# create function to convert fahrenheit to celsius
def fahr_to_celsius(temp_fahrenheit):
    # Convert Fahrenheit to Celsius
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    return temp_celsius