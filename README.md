#aoe2techtree

This is a series of python codes that I wrote (for some reason)
to query the AOE2 tech tree. Everything is written in native python 3.7

To query the tree, simply run tech-tree-query.py. You will be prompted
to enter units or techs that you want a civ to have. Enter them one at 
a time. Once you are done, type "no" and the civs that meet your 
requirements will be printed. 

A few important notes:
Not all the techs have the same name as they do in the tech tree. For 
example, "bracer" keeps the same name, but the other blacksmith upgrades 
have been changed to "melee attack N" (where N is 1,2, or 3), 
"cavalry armor N", "archer armor N", and "infantry armor N". 

Everything is lowercase. I have generally tried to keep the same name 
as the tech tree for non-blacksmith techs and units (e.g., "skirmisher" 
instead of "skirm"). 

If there is confusion, run "print-all-units.py" which will print the 
name of everything listed. 

Because the tech tree I referenced is the readily available one at 
aoe2techtree.net, which is current to the latest DE release, there 
might be some version issues with this and the expansions, and certaintly
with the base HD game.

No civ bonuses are included here; if I get bored again I might put in
a category for that but who knows. 

License: share without profit at will
