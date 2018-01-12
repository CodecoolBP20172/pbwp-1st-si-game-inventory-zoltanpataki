# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
import operator
import sys
import csv
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'daggerjgjdsfjdshkjfhskjdfhjdshf': 1, 'arrow': 12} 


# Displays the inventory.
def display_inventory(inventory):
    print('Inventory:\n')
    for item,value in inventory.items():
        print(value,item)
    print('\nTotal number of items: %d'%sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    unsortedinv = sorted(inventory.items())    
    sortedinv1 = sorted(inventory.items(), key=operator.itemgetter(1))
    sortedinv2 = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    if order is None:
        sorting=unsortedinv
    elif order == 'count,asc':
        sorting=sortedinv1
    elif order == 'count,desc':
        sorting=sortedinv2
    lst=[]
    for tup in sorting:
        lst.append(len(tup[0]))
    k=max(lst)
    j=max(lst)
    print('Inventory: \n')
    print('count'.rjust(k),'   ','item name'.rjust(j))
    for i in range(k+j+5):
        sys.stdout.write('-')
    print('\n')
    for tup in sorting:
        print(str(tup[1]).rjust(k),'   ',str(tup[0]).rjust(j))
    for i in range(k+j+5):
        sys.stdout.write('-')
    print('\nThe total number of items: %d'%sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    file=open(filename,'r')
    reader=csv.reader(file)
    for row in reader:
        importlst=(row)
    for item in importlst:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1
    file.close()
    return (inventory)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    exportlst=[]
    for key in inventory:
        value=0
        while value<inventory[key]:
            exportlst.append(key)
            value+=1
    print(exportlst)
    with open(str(filename),'w',newline='') as outputstream:
        writer=csv.writer(outputstream)
        writer.writerow(exportlst)



import_inventory(inv,'grading_inventory.csv')
display_inventory(inv)