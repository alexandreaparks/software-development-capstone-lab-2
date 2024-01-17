# list of tuples
city_state = [("Seattle", "WA"), ("Portland", "OR"), ("San Francisco", "CA")]

print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

# tuple unpacking
print(first_city_state[0])
print(first_city_state[1])

# can be written as:

city, state = first_city_state
print(city, state)


animals = ("lion", "puma", "tiger")

lion, puma, tiger = animals

print(tiger)

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances)

print(distances[0])

# can be written as:

miles, km = get_distance()
print(km)