# Season function
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"
    
# create function to convert Tuncertainty to Clecius from Fahrenheit
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0  