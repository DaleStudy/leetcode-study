// Time Complexity: O(n)
// Spatial Complexity: O(n)

class Codec {
private:
    string genereateRandomString(size_t size) {
        string randomString = "";
        for(size_t i = 0; i < size; ++i) {
            randomString += static_cast<char>(rand() % 256);
        }

        return randomString;
    }

    vector<string> split(string target, string delimiter) {
        vector<string> ans;

        int delimiterLength = delimiter.size();
        size_t pos = target.find(delimiter);
        while(pos != string::npos) {
            ans.push_back(target.substr(0, pos));

            target = target.substr(pos + delimiterLength, target.size());
            pos = target.find(delimiter);
        }
        ans.push_back(target);

        return ans;
    }

    string delimiter = this->genereateRandomString(10);

public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encodedString = strs[0];

        for(int i = 1; i < strs.size(); ++i) {
            encodedString += this->delimiter + strs[i];
        }

        return encodedString;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {

        return split(s, this->delimiter);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
