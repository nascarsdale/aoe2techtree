from aoe2techtree import *

everything = return_all_units()

for type_of_thing in everything.keys():
    for unitline in everything[type_of_thing].keys():
        for unit_or_tech in everything[type_of_thing][unitline]:
            print(unit_or_tech)
