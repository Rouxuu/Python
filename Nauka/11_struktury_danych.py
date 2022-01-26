names_list = []  # tworzenie pustej listy
names_list.append('Seba')
names_list.append('Maciek')
names_list.append('Łuaksz')  # dodawanie do listy
print(names_list)

# tworzenie listy już z elementami
names_list = ["Kamil", "Rychu", "Piotr", "Kamil"]
print(names_list)
print()


for name in names_list:  # wypisywanie po kolei elementów listy
    print(name)
print()


names_list.reverse()  # odwrócenie listy
# indeks elementu mowi ktory element list ma byc wyswietlony
print(names_list[1])
print()

print(names_list.count("Kamil"))  # liczenie konkretnych elemntów w liście
print(names_list)
print()

names_list.sort()  # sortowanie alfabetyczne
print(names_list[2])
print()


print(len(names_list))  # liczenie wszystkich elementów w liście
print()


print(names_list.pop(0))  # usunięcie z listy ze zwrotem elementu
print()


names_list.remove("Rychu")  # usunięcie czegoś z listy bez zwrotu
print(names_list)
print()

names_list.clear  # czyszczenie listy
print(names_list)
print()

names_list2 = ["Albert", "Marcin"]
names_list3 = ["Monitor", "Marcin"]
names_list4 = names_list + names_list2 + names_list3
print(names_list4)
print()

names_list4.sort()  # sortowanie alfabetyczne
print(names_list4)
print()

names_list4.sort(reverse=True)  # sortowanie alfabetyczne od tyłu
print(names_list4)
print()

# KROTKA
person = ("Sebastian,", "Har", 19)
print(person.count("Sebastian"))
print(person)
print()

# SET
# 1. nie może być powtórzonych wartość
# 2. elementy setu są niemutowalne
# 3. elementy setu nie są uporządkowane
names_set_pusty = set()
names_set_pusty.add("Piotr")
names_set_pusty.add("Adam")
print(names_set_pusty)
names_set_pusty.remove("Piotr")
print(names_set_pusty)
print()

names_set = {"Kamil", "Mariusz", "Kamil", "Łukasz"}
print(names_set)
print()

for name in names_set:
    print(name)
print()

names_set_3 = names_set.union(names_set_pusty)
for name in names_set_3:
    print(name)
print()

names_set_4 = names_set.difference(names_set_3)
for name in names_set_4:
    print(name)
print()

names_set_3.clear
print("hejo")
for name in names_set_3:
    print(name)
print()

# Dictionary
countries_and_capitals = {"Poland": "Warsaw",
                          "Germany": "Berlin", "Russia": "Moscow"}
countries_and_capitals["USA"] = "Washington DC"
print(countries_and_capitals)
print()

for country, capital in countries_and_capitals.items():
    print(country + "-" + capital)
print()
print(countries_and_capitals["Poland"])
print()
print(countries_and_capitals.setdefault("Spain", "Madrit"))  # wypluwa i dodaje
print()
countries_and_capitals.pop("Poland")
print()
print(countries_and_capitals.popitem())  # usuwa ostatnio dodany element
print()
if "Poland" in countries_and_capitals.keys():
    print("Jest!")
else:
    print("Ni mo!")

countries_and_capitals.clear()
print(countries_and_capitals)
