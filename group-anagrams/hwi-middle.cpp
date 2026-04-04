class Solution {
private:
    // 단어별로 알파벳 개수를 세는 구조체
    struct chnum
    {
        int cnt[26];

        chnum()
        {
            memset(cnt, 0, sizeof(int) * 26);
        }

        bool operator==(const chnum& other) const
        {
            for (int i = 0; i < 26; ++i)
            {
                if (this->cnt[i] != other.cnt[i]) return false;
            }
            return true;
        }
    };

struct chnumHash
    {
        size_t operator()(const chnum& key) const
        {
            size_t seed = 5381; 
            for (int i = 0; i < 26; ++i)
            {
                seed = ((seed << 5) + seed) + key.cnt[i];
            }
            return seed;
        }
    };

public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<chnum, vector<string>, chnumHash> ns; // 알파벳 개수를 넣으면 알파벳 구성을 갖는 문자열 배열이 나옴
        for (auto& str : strs)
        {
            chnum n;
            for (auto ch : str)
            {
                n.cnt[ch - 'a']++; // 알파벳 개수를 세고...
            }

            ns[n].push_back(str); // 해시맵에 넣음
        }

        vector<vector<string>> v;
        v.reserve(ns.size());

        for (auto& p : ns)
        {
            v.push_back(move(p.second));
        }

        return v;
    }
};
