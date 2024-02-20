from random import choice

percent_rain = [32, 95, 94, 78, 30, 49, 10, 30, 90, 40, 67, 80]

resps = []

x = choice(percent_rain)
print(x)

if x > 90:
    resps.append("Bring an umbrella.")
elif x > 80:
    resps.append("Good for the flowers?")
elif x > 50:
    resps.append("Watch out for clouds!")
else:
    resps.append("Nice day!")
print(resps)
