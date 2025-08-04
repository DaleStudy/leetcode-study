class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder cleaned = new StringBuilder(); 

        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.append(Character.toLowerCase(c)); 
            }
        }

        int left = 0; 
        int right = cleaned.length() - 1; 
        while (left < right) {
            // Fail fast: return false as soon as a mismatch is found
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false; 
            }
            left++;
            right--; 
        }

        return true; 
    }
}

/**
converting all uppercase letters into lowercase letters
removing all non-alphanumeric char

1. cleaning 
    0. str -> char with for-each loop  
    1. check char if isLetterOrDigit
    2. make char to LowerCase 
    * Character Class static method 
2. two ptrs comparison while left < right 
    s[i] == s[n - 1 - i] 

- Time: O(n) 

 /** REMEMBER 
1. length vs length() 

arr.length => field 
String(Builder).length() => method 

2. “fail fast” approach: 
As soon as we detect something wrong, we exit early.
  */
