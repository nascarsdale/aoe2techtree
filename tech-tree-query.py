from aoe2techtree import *

all_units = return_all_units()
all_attributes = civ_attributes()
bonuses = civ_bonuses()

full_dict = {}

for civ in all_attributes.keys():
    full_dict[civ] = make_civ_dict(all_units, all_attributes[civ])

#make list of things for faulty queries
alltechs = []
for build in all_units.keys():
    for unitline in all_units[build].keys():
        for unit in all_units[build][unitline]:
            alltechs.append(unit)

print('This script will ask you for units & techs that you would like a civ to have. You can enter as many as you like. Please refer to the readme for information about how the techs are described. They do not all match the tech tree exactly (e.g. instead of \"ring archer armor\", the entry in this script is \"archer armor 3\", but \"bracer\" is unchanged). NOTE: currently, you must enter desired bonuses LAST in your query.')

run = True

while run:
    
    #initialize 
    desired = []
    asking_for_units = True

    while asking_for_units == True:
        request = input('What unit/tech do you want your civ to have? Type \'no\' if you would not like anything else. ')
        #enable "not" functionality without breaking the "make sure they're asking for something in the list"
        #note that this only works because there aren't any units with "not" in their name, lol
        if 'not' in request:
            unit = request[4:]
        else:
            unit = request

        if unit == 'no':
            asking_for_units = False
            break

        #tell them if they input a unit that my list doesn't have
        if unit not in alltechs and 'bonus' not in unit:
            print('that unit or tech does not appear on our list! please check the readme for input details')
            continue
        desired.append(request)


#==================BEGIN ACTUALLY QUERYING=======================


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
        
        #run number 1, when you're drawing from the full list of civs
        if i == 0:
            if 'bonus' not in thing:
                for civ in full_dict.keys():
                    if full_dict[civ][thing] == target:
                        temp.append(civ)
                    else:
                        continue
            elif 'bonus' in thing:
                bonustraits = thing.split(' ')
                bonustraits.remove('bonus')
                for civ in full_dict.keys():
                    for civbonus in bonuses[civ]:

                        #if all of the traits of your desired bonus are in the civ's bonus...
                        if all(trait in civbonus for trait in bonustraits):
                            
                            #making it so if you search "siege bonus", and ethiopians come up, 
                            #you know they have some siege-related advantage, but that it's a 
                            #tech, not a true free bonus.
                            
                            if 'tech' in civbonus:
                                temp.append(civ+'*')
                            else:
                                temp.append(civ)
            
            #hacky way to make i the dictionary key,  
            master_runs[str(i)] = temp
        
        #subsequent runs, where you want to pull from the shorter list you've already made
        elif i>0:
            newcivlist = master_runs[str(i-1)]
            if 'bonus' not in thing:
                    for civ in newcivlist:
                        if full_dict[civ][thing] == target:
                            temp.append(civ)
                        else:
                            continue
            elif 'bonus' in thing:
                bonustraits = thing.split(' ')
                bonustraits.remove('bonus')
                for civ in newcivlist:
                    #get rid of starred civs (i.e. unique tech bonuses)
                    if '*' in civ:
                        civ = civ[:-1]
                    for civbonus in bonuses[civ]:
                        if all(trait in civbonus for trait in bonustraits):
                            if 'tech' in civbonus:
                                temp.append(civ+'*')
                            else:
                                temp.append(civ)

            #don't accidentally indent this lol 
            master_runs[str(i)] = temp
        
        #pre-bonus code
        #elif i>0:
        #    newcivlist = master_runs[str(i-1)]
        #    for civ in newcivlist:
        #        if full_dict[civ][thing] == target:
        #            temp.append(civ)
        #        else:
        #            continue
        #    master_runs[str(i)] = temp
    
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
    
    #quick hack because my bonus code introduces duplicates 
    civlist_final = []
    [civlist_final.append(x) for x in civs_meeting_reqs if x not in civlist_final]

    print('The civs that meet your constraints are: ', civlist_final)

    again = input('Would you like to run another search? Type y or n')

    if again=='y':
        continue
    elif again=='n':
        run = False
        break

