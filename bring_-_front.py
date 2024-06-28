#sample input : pre-defined
#sample output : -predefined

word = input()
if "-" in word:
    new = word.replace("-","")
print("-",new)
