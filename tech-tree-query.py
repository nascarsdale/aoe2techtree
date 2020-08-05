from aoe2techtree import *

all_units = return_all_units()
all_attributes = civ_attributes()

full_dict = {}

for civ in all_attributes.keys():
    full_dict[civ] = make_civ_dict(all_units, all_attributes[civ])

desired = []
asking_for_units = True

while asking_for_units == True:
    unit = input('What do you want your civ to have? Type \'no\' if you would not like anything else. ')
    if unit == 'no':
        asking_for_units = False
        break
    desired.append(unit)

civs_meeting_reqs = []

i = 0

#if full_dict[civ][thing] == 1 for thing in desired:
#    civs_meeting_reqs.append(civ)

master_runs = {}

for thing in desired:
    temp = []
    
    if i == 0:
        for civ in full_dict.keys():
            if full_dict[civ][thing] == 1:
                temp.append(civ)
            else:
                continue
        master_runs[str(i)] = temp
        
    elif i>0:
        newcivlist = master_runs[str(i-1)]
        for civ in newcivlist:
            if full_dict[civ][thing] == 1:
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