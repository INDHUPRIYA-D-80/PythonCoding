# sample input : aaabbbbcccdd
# sample output : a3b4c3d2
def count(word):
    count = 1
    new = ""

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1
        else:
            new += word[i - 1] + str(count)
            count = 1
    new += word[-1] + str(count)

    return new
word = "aaaabbbbccc"
output = count(word)
print(output)


# word = input()
# print(count(word))



    