
def weather(temperature):

    if temperature > 25 :
        weather_feel = 'Hot'
    elif temperature >= 15 and temperature <= 25 :
        weather_feel = 'Warm'
    else :
        weather_feel = 'Cold'

    return weather_feel

temp_input = float(input("Enter temperature ( centigrade):"))

print(weather(temp_input))
