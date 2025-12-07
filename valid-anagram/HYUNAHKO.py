from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict1 = {}
        letter_dict2 = {}
        letter_list1 = list(s)
        letter_list2 = list(t)
        
        for i in letter_list1:
            letter_dict1[i] = letter_dict1.get(i, 0) + 1
            
        for j in letter_list2:
            letter_dict2[j] = letter_dict2.get(j, 0) + 1

        if (letter_dict1 == letter_dict2):
            return True 
        else: 
            return False
                

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
