#uchta listni birlashtirib dictionary yasaymiz
list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
set_new={}
for i in range(len(list1)):
    set_new[list1[i]]={list2[i], list3[i]}
print(f"SET={set_new}")