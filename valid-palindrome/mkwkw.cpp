class Solution {
public:
    bool isPalindrome(string s) {
        
        string str = "";

        for(int i=0; i<s.length(); i++)
        {
            if(isalpha(s[i]))
            {
                str += tolower(s[i]);
            }
            else if (s[i]>='0' && s[i]<='9') //alpha"numeric"
            {
                str += s[i];
            }
        }

        //Palindrome
        if(s.length()==0 || s.length()==1)
        {
            return true;
        }

        for(int i=0; i<str.length()/2; i++)
        {
            if(str[i]!=str[str.length()-1-i])
            {
                return false;
            }
        }

        return true;
    }
};
