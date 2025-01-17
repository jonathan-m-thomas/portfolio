from typing import List

def contains_duplicate(words: List[str]) -> bool:
    for i in range(0, len(words)):
        for j in range(1, len(words)):
            #print(i, j)
            if words[j] == words[i]:
                return True
    return False

    

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))