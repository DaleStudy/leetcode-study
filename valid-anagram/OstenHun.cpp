/*
    Given two strings s and t, return true
    if t is an anagram of s, and false otherwise.

    An anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase,
    using all the original letters exactly once.
*/

#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(const string& s, const string& t) {
        if (s.length() != t.length()) {
            return false;
        }

        int freq[26] = {};

        for (size_t i = 0; i < s.length(); i++) {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }

        for (int count : freq) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
};
