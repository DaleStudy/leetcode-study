// class Solution {
// public:
//     bool isPalindrome(string s) {
//         string new_s;

//         for(char c : s)
//             if(isalpha(c) || isdigit(c))
//                 new_s += tolower(c);
        
//         int left = 0, right = new_s.size() - 1;

//         while(left < right) {
//             if(new_s[left] != new_s[right])
//                 return false;
//             left++;
//             right--;
//         }

//         return true;
//     }
// };

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;

        while(left < right) {
            if(!isalnum(s[left])) {
                left++;
                continue;
            }
            if(!isalnum(s[right])) {
                right--;
                continue;
            }

            if(isdigit(s[left]) && isdigit(s[right])) {
                if(s[left] != s[right]) {
                    return false;
                }
            }
            else if(isalpha(s[left]) && isalpha(s[right])) {
                if(tolower(s[left]) != tolower(s[right]))
                    return false;
            }
            else 
                return false;
            left++;
            right--;
        }

        return true;
    }
};

