class Solution {
    public:
        /*
         * @param strs: a list of strings
         * @return: encodes a list of strings to a single string.
         */
        string encode(vector<string> &strs) {
            // write your code here
            string code;
    
            for(const string& s : strs){
                code += to_string(s.size()) + ":" + s;
            }
    
            return code;
        }
    
        /*
         * @param str: A string
         * @return: decodes a single string to a list of strings
         */
        vector<string> decode(string &str) {
            // write your code here
            vector<string> result;
            int i;
    
            while(i < str.size()){
                int j = i;
    
                while(str[j] != ':') 
                    j++;
    
                int len = stoi(str.substr(i, j - i);
                string word = str.substr(j + 1, len);
    
                result.push_back(word);
    
                i = j + 1 + len;
            }
    
            return result;
        }
    };
