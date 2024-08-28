/**
 * For length of given strings N,
 * 
 * Time complexity: O(N)
 * - iteration for given strings
 * 
 * Space complexity: O(1)
 * - the size of the container `count` is constant
 */

class Solution {
public:
    bool isAnagram(string s, string t) {
        int count[26] = {0};

        for (auto c : s) count[c - 'a']++;
        for (auto c : t) count[c - 'a']--;

        for (int i = 0; i < 26; i++) if (count[i]) return false;
        return true;
    }
};
