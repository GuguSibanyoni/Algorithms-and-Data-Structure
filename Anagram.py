'''
given strings s1 = 'Clint Eastwood' and s2 = 'old west action'
prove that the two strings are anagrams of each other

step 1. Clean up the strings
step 2. Check if the length of both the strings, it needs to be the same if not then they are not anagrams of eachother
step 3. count the frequency of the letters
step 4. we do the reverse on the second string
step 5. check count in the dictionary
step 6. If all are zero we jump out of the loop'''


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for character in s1:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1

    for character in s2:
        if character in count:
            count[character] -= 1
        else:
            count[character] = 1

    for i in count:
        if count[i] != 0:
            return False
    return True


x = is_anagram("clint Eastwood", "old west action")
y = is_anagram("Gugu", "Dudu")

print(x)
print(y)