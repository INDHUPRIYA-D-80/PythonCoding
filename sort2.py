#PS Arrange them in such a wsy rhyming words are next to each other

words = ["run","maple","bun","apple"]
words.sort(key=lambda x:x [::-1]) #USING A LAMBDA WHICH DOESN'T NEED ANY SPECIFIC DEFINITION
print(words)

#USING A SEPARATE FUNCTION

def reverse_str(x):
    return x[::-1]
print(words)

#PS2: SORT THE WORDS IN THE FOLLOWING SENTENCE BASED ON THEIR LENGTH

string = "this statement gets arranged in the order of increasing length of the words"

result = string.split(" ")
result.sort(key=len)

print(" ".join(result))