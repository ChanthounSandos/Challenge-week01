sct = input("Filename: ")
#split the string by dot(.)
a = sct.split(".")
a = a[1]
#create a dic which contain keys and values
dic = {"txt": "Text File", "py": "Python File", "json": "JSON File"}
#match the key and value
if a in dic.keys():
    print(dic[a])
else:
    print("Invalid Filename")