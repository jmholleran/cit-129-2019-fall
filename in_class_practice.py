"""
In-Class Practice

"""

data = {"1": {"A": "100", "B": "200"},
        "2": {"C": "300", "D": "400"},
        "3": {"E": "500", "F": "600"}}

## Display all dictionaries

for key, value in data.items():
    print(key)



## Display dictionaries

for key, value in data.items():
    print(key, value)
    
select = input("Pick a dictionary: ")

for key, value in data[select].items():
    print(key, value)
    
## Add to dictionary key & value
    
sel_dictionary = input("Pick dictionary to ADD: ")

for key, value in data[sel_dictionary].items():
    print(key, value)
    
new_key = input("New Key: ")
new_value = input("New Value: ")

if new_key not in data[sel_dictionary]:
    data[sel_dictionary][new_key] = new_value
else:
    print("That entry already exists.")
    
for key, value in data.items():
    print(key, value)
    
## Add new dictionary
    
ss_dictionary = input("Enter new dictionary: ")

new_key = input("Enter new key: ")
new_value = input("Enter new value: ")

data[ss_dictionary] = {new_key : new_value}

for key, value in data.items():
    print(key, value)
        
## Change dictionary
    
    
se_dictionary = input("Pick dictionary to CHANGE: ")

for key, value in data[se_dictionary].items():
    print(key, value)
    
change_key = input("Change Key: ")
    
if change_key in data[se_dictionary]:
    
    change_value = input("New Value: ")
    data[se_dictionary][change_key] = change_value

else:
    print("That key not found.")

for key, value in data.items():
    print(key, value)

    
## Delete from dictionary
    
s_dictionary = input("Pick dictionary to DELETE: ")  

for key, value in data[s_dictionary].items():
    print(key, value)
    
delete_key = input("Delete Key: ")

if len(data[s_dictionary]) == 1:
    print("Sorry cannot remove last key/value pair")
elif delete_key in data[s_dictionary]:
    
    del data[s_dictionary][delete_key]
    
else:
    print("Key not found")
    
for key, value in data.items():
    print(key, value)   
    

    





