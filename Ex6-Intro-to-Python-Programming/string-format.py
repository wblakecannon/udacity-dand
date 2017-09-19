city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#todo rewrite this line to use the format method rather than string concatenation
#alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)

# print the alert
print(alert)
