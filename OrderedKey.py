import collections

ship = {
    "Name": "Ahmedabad",
    "HP": 5,
    "Blasters": 13,
    "Thrusters": 18,
    "Price": 250
}

print(ship)
print(collections.OrderedDict(ship))

ordered_dict = collections._OrderedDictItemsView(sorted(ship.items()))

list_key = ["Name","HP","Blasters","Thrusters","Price"]
ordered_list = [(key,ship[key]) for key in list_key]
ordered_ship = collections.OrderedDict(ordered_list)

print(ordered_ship)




