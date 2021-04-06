# Find out whether 2 words are anagram or not


# #Sort and compare solution using built in sort() method
# def anagramSolution(s1,s2):
#     # seeing if both strings are of same length; if yes assigning them to lists
#     if len(s1) == len(s2):    
        # alist1 = list(s1)
#         alist2 = list(s2)
#     else:
#         return False
    
#     #sorting the lists 
#     alist1.sort()
#     alist2.sort()

#     # seeing if the values in the sorted lists are same.
#     pos = 0
#     matches = True
#     while pos < len(s1) and matches:
#         if alist1[pos]==alist2[pos]:
#             pos = pos + 1
#         else:
#             matches = False
#     return matches

# print(anagramSolution('abcd','edcba'))



# Count and compare solution; Time complexity: O(n)
def anagramSolution2(s1, s2):
    l1 = [0] * 26
    l2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        l1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        l2[pos] += 1

    if l1 == l2:
        return True
    else:
        return False

print(anagramSolution2('abcdf','edcba'))