from aoe2techtree import *

all_units = return_all_units()
all_attributes = civ_attributes()

full_dict = {}

for civ in all_attributes.keys():
    full_dict[civ] = make_civ_dict(all_units, all_attributes[civ])

desired = []
asking_for_units = True

#make list of things for faulty queries
alltechs = []
for build in all_units.keys():
    for unitline in all_units[build].keys():
        for unit in all_units[build][unitline]:
            alltechs.append(unit)

while asking_for_units == True:
    request = input('What do you want your civ to have? Type \'no\' if you would not like anything else. ')
    #enable "not" functionality without breaking the "make sure they're asking for something in the list"
    if 'not' in request:
        unit = request[4:]
    else:
        unit = request

    if unit == 'no':
        asking_for_units = False
        break

    #tell them if they input a unit that my list doesn't have
    if unit not in alltechs:
        print('that unit or tech does not appear on our list! please check the readme for input details')
        continue
    desired.append(request)

civs_meeting_reqs = []

i = 0

#if full_dict[civ][thing] == 1 for thing in desired:
#    civs_meeting_reqs.append(civ)

master_runs = {}

for thing in desired:
    temp = []
    
    #add ability to say "not paladin", for example
    if 'not' in thing:
        target = 0
        thing = thing[4:]
    elif 'not' not in thing:
        target = 1


    if i == 0:
        for civ in full_dict.keys():
            if full_dict[civ][thing] == target:
                temp.append(civ)
            else:
                continue
        master_runs[str(i)] = temp
        
    elif i>0:
        newcivlist = master_runs[str(i-1)]
        for civ in newcivlist:
            if full_dict[civ][thing] == target:
                temp.append(civ)
            else:
                continue
        master_runs[str(i)] = temp
    
    if i < len(desired)-1:
        i += 1
    else:
        continue
    '''
    if i == 0:
        for civ in full_dict.keys():
            if full_dict[civ][thing] == 1:
                temp1.append(civ)
            else:
                continue
    elif i > 0:
        for civ in temp1:
            if full_dict[civ][thing] == 1:
                temp2.append(civ)
    i+=1
    '''

civs_meeting_reqs = master_runs[str(i)]
    
print('The civs that meet your constraints are: ', civs_meeting_reqs)
