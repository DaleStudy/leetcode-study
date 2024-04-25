// https://leetcode.com/problems/valid-palindrome/
// Time Complexity : O(n)
// Space Complexity : O(n)

class Solution {
public:
    bool isPalindrome(string s) {
        string ns;
        for(char c : s){
            if(c >= '0' && c <= '9') ns += c;
            else if(c >= 'A' && c <= 'Z') ns += (c + 32);
            else if(c >= 'a' && c <= 'z') ns += c;
        }

        int n = ns.size();
        for(int i=0; i<n/2; i++) {
            if(ns[i] != ns[n-i-1]) return false;
        }
        return true;
    }
};
