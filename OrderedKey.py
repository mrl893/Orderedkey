import collections

ship = {
    "Name": "Ahmedabad",
    "HP": 5,
    "Blasters": 13,
    "Thrusters": 18,
    "Price": 250
}

ordered_dict = collections._OrderedDictItemsView(sorted(ship.items()))

# print(ship)
# print(collections.OrderedDict(ship))



list_key = ["Name","HP","Blasters","Thrusters","Price"]
ordered_list = [(key,ship[key]) for key in list_key]
ordered_ship = collections.OrderedDict(ordered_list)

print(ordered_ship)




