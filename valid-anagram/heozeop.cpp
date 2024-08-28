// Time Complexity: O(n)
// Spatial Complexity: O(1)

class Solution {
public:
    bool isAnagram(string s, string t) {
        int numberOfAlphabet[26];

        for(char character : s) {
            numberOfAlphabet[character - 'a']++;
        }

        for(char character : t) {
            numberOfAlphabet[character - 'a']--;
        }

        for(int i = 0; i < 26; ++i) {
            if (numberOfAlphabet[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
};

