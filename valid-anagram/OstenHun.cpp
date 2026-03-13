/*
    Given two strings s and t, return true
    if t is an anagram of s, and false otherwise.

    An anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase,
    using all the original letters exactly once.

    Input: s = "anagram", t = "nagaram"
    Output: true
*/

#include <string>
#include <unordered_map>
using namespace std;

#pragma region FirstIdea_TwoArrays
namespace first_idea {

class Solution {
public:
    bool isAnagram(const string& s, const string& t) {
        int freq_s[26] = {};
        int freq_t[26] = {};

        if (s.length() != t.length()) {
            return false;
        }

        for (size_t i = 0; i < s.length(); i++) {
            freq_s[s[i] - 'a']++;
        }

        for (size_t i = 0; i < t.length(); i++) {
            freq_t[t[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq_s[i] != freq_t[i]) {
                return false;
            }
        }

        return true;
    }
};

}  // namespace first_idea
#pragma endregion

#pragma region FinalSolution_OneArray
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
#pragma endregion

#pragma region Alternative_UnorderedMap
namespace unordered_map_idea {

class Solution {
public:
    bool isAnagram(const string& s, const string& t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        for (char ch : t) {
            freq[ch]--;
        }

        for (const auto& [ch, count] : freq) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
};

}  // namespace unordered_map_idea
#pragma endregion
