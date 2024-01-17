# can modify a set
# unordered collection
# duplicates not allowed

cats = set()  # creates empty set
cats.add("Lion")
cats.add("Tiger")
print(cats)
cats.add("Cheetah")
print(cats)

birds = {"owl", "robin", "swan"}
print(birds)
birds.add("robin")  # won't work - can't have duplicates
print(birds)
birds.remove("owl")
birds.add("cardinal")
print(birds)

for bird in birds:
    print(bird)

bird_list = ["robin", "swan", "swan", "eagle", "cardinal", "swan", "robin"]
bird_list_no_duplicates = list(set(bird_list))  # change to set, then back to list
print(bird_list_no_duplicates)

