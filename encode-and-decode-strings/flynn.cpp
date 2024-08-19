/**
 * Let's say sum of lengths of given strings N, and the length of the longest string M
 * 
 * Encode
 * - Time complexity: O(N)
 * - Space complexity: O(1)
 * 
 * Decode
 * - Time complexity: O(N)
 * - Space complexity: O(M)
 */

class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res = "";
        for (auto str : strs) {
            res += to_string(str.size());
            res.push_back('.');
            res += str;
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int str_size = 0;
        string tmp = "";

        auto it = s.begin();
        while (it != s.end()) {
            do {
                str_size = str_size * 10 + (*it - '0');
                it++;
            } while (*it != '.');

            it++;

            for (int i = 0; i < str_size; i++) {
                tmp.push_back(*it);
                it++;
            }

            res.push_back(tmp);
            str_size = 0;
            tmp = "";
        }

        return res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
