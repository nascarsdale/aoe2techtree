#aoe2techtree

This is a series of python codes that I wrote (for some reason)
to query the AOE2 tech tree. Everything is written in native python 3.7

To query the tree, simply run tech-tree-query.py. You will be prompted
to enter units, techs, or bonuses that you want a civ to have. Enter 
them one at a time. Once you are done, type "no" and the civs that meet 
your requirements will be printed. 

A few important notes:
Not all the techs have the same name as they do in the tech tree. For 
example, "bracer" keeps the same name, but the other blacksmith upgrades 
have been changed to "melee attack N" (where N is 1,2, or 3), 
"cavalry armor N", "archer armor N", and "infantry armor N". 

I know this is confusing but I never hear anybody talk about missing 
"plate mail armor" or whatever instead of "the last infantry armor" but 
I definitely hear people talk about "missing bracer". 

Everything is lowercase. I have generally tried to keep the same name 
as the tech tree for non-blacksmith techs and units (e.g., "skirmisher" 
instead of "skirm"). 

If there is confusion, run "print-all-units.py" which will print the 
name of everything listed. 

There are likely to be some discrepancies with DE AND HD as I have not 
included the new DE civs, and have not directly referenced the HD tech
tree in-game. Sorry about that. 

NEW! 
"bonus" query: you can say, e.g., 'strong early economy bonus' as one
of your queries and the code will tell you what civs have those. Note
that these are COMPLETELY subjective and VERY wacky (lol that I gave 
Portuguese a "strong" military bonus for their gold discount), being
based on the opinion of somebody who only has a couple hundred hours
of gametime. I will make an effort to make these less absurd, but 
it may take some time so just keep this in mind when querying.  

Coming eventually:
unique techs and unique units 



So I don't forget to include this info if I share this 
thing publicly:
Age of Empires II is copyrighted by Microsoft Corporation. 
This code was created under Microsoft's Game Usage Rules
using assets from Age of Empires II and is not endorsed by 
or affiliated with Microsoft.

License: CC BY-NC-SA
