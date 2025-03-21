#dictionaryda qiymatlarni alishtirish 
dict1={1:"ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO"}
list_keys=list(dict1.keys())
list_values=list(dict1.values())
print(list_keys)
print(list_values)

dict_new={}
for i in range(0,len(list_keys)-1, 2):
    dict_new[list_keys[i]]=list_values[i+1]
    dict_new[list_keys[i+1]]=list_values[i]
if len(list_keys)%2!=0:
    dict_new[list_keys[-1]]=list_values[-1]
print(dict_new)