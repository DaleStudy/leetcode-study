class Solution {
public:
    string minWindow(string s, string t) {
        int m = (int)s.size();
        if (t.empty() || s.empty()) return "";

        int target[128] = {0};
        int cnt[128] = {0};

        int required = 0;
        for (char c : t) {
            unsigned char uc = (unsigned char)c;
            if (target[uc] == 0) required++;
            target[uc]++;
        }

        int formed = 0;
        int l = 0, r = 0;
        int ansl = 0, ansr = 0;
        bool hasAns = false;

        while (l <= r) {
            bool isValid = (formed == required);

            if (isValid) {
                if (!hasAns || (r - l) < (ansr - ansl)) {
                    ansl = l;
                    ansr = r;
                    hasAns = true;
                }

                char cl = s[l];
                cnt[cl]--;
                if (target[cl] > 0 && cnt[cl] == target[cl] - 1) {
                    formed--;
                }
                l++;
            }
            else if (r >= m) {
                char cl = s[l];
                cnt[cl]--;
                if (target[cl] > 0 && cnt[cl] == target[cl] - 1) {
                    formed--;
                }
                l++;
            }
            else {
                char cr = s[r];
                cnt[cr]++;
                if (target[cr] > 0 && cnt[cr] == target[cr]) {
                    formed++;
                }
                r++;
            }
        }

        if (!hasAns) return "";
        return s.substr(ansl, ansr - ansl);
    }
};
