speed = int(input('Enter speed: '))
time = int(input('Enter time: '))
distance = speed * time
number_of_laps = distance // 100
destination = (-(100 * number_of_laps - distance))
print(destination)

