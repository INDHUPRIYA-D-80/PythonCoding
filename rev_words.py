# sample input : this is test
sen=input().split(" ")
# sample output : test is this (reverse word by word)
print(" ".join(sen[::-1]))
# sample output :tset si siht (reverse the entire string)
print(" ".join(sen[::-1])[::-1])
