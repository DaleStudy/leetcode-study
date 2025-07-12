"""
문제 설명:
There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Conditions:
- You may assume all letters are in lowercase
- At first different letter, if the letter in s precedes the letter in t in the given list order, then the dictionary order of s is less than t
- The dictionary is invalid, if string a is prefix of string b and b is appear before a
- If the order is invalid, return an empty string
- There may be multiple valid order of letters, return the smallest in normal lexicographical order
- The letters in one string are of the same rank by default and are sorted in Human dictionary order

Time Complexity: 
 - 

Space Complexity: 
 - 
"""
