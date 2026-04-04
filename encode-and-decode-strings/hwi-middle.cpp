class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string str;
        for(auto& s : strs)
        {
            str += s;
            str.push_back(3); // 문제의 입력으로 오지 않는 값(ETX, End of Text)을 구분자로 사용
        }

        return str;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> v;
        v.reserve(200);
        string str_buf;
        istringstream iss(s);
        while (getline(iss, str_buf, (char)3)) 
        {
            v.push_back(str_buf);
        }

        return v;
    }
};
