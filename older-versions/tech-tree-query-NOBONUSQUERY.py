??? from here until ???END lines may have been inserted/deleted
from aoe2techtree import *

all_units = return_all_units()
all_attributes = civ_attributes()

full_dict = {}

for civ in all_attributes.keys():
    full_dict[civ] = make_civ_dict(all_units, all_attributes[civ])

#make list of things for faulty queries
alltechs = []
for build in all_units.keys():
    for unitline in all_units[build].keys():
        for unit in all_units[build][unitline]:
            alltechs.append(unit)

print('This script will ask you for units & techs that you would like a civ to have. You can enter as many as you like. Please refer to the readme for information about how the techs are described (e.g. instead of \"ring archer armor\", the entry in this script is \"archer armor 3\", but \"bracer\" is unchanged)')

run = True

while run:
    
    #initialize 
    desired = []
    asking_for_units = True

    while asking_for_units == True:
        request = input('What unit/tech do you want your civ to have? Type \'no\' if you would not like anything else. ')
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

#===============START THE QUERY NOW THAT THE LIST IS IN HAND=================================

    #initialize list
    civs_meeting_reqs = []

    i = 0

    #if full_dict[civ][thing] == 1 for thing in desired:
    #    civs_meeting_reqs.append(civ)

    master_runs = {}

    for thing in desired:
        temp = []
        
        

        #add ability to say "not paladin", for example
        #if they add a tech that has "not" in it this will break tho lol 
        if 'not' in thing:
            target = 0
            thing = thing[4:]
        elif 'not' not in thing:
            target = 1

        #first run; need to initialize a list of civs that meet at least 1 requirement
        if i == 0:
            for civ in full_dict.keys():
                if full_dict[civ][thing] == target:
                    temp.append(civ)
                else:
                    continue
            #hacky way to make dict keys w/ i
            master_runs[str(i)] = temp
        
        #subsequent runs; pull from civs that already meet one of them
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

    again = input('Would you like to run another search? Type y or n')

    if again=='y':
        continue
    elif again=='n':
        run = False
        break
???END
