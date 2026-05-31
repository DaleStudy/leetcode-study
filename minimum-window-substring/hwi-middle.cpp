class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty())
        {
            return "";
        }

        // t에서 각 문자가 등장한 횟수
        unordered_map<char, int> dictT;
        for (auto& c : t)
        {
            dictT[c]++;
        }

        // t에 들어있는 문자의 종류
        // 즉, 윈도우 안에 있는 문자의 종류는 required개 이상이어야 함
        int required = dictT.size();

        int l = 0;
        int r = 0;

        // t에 있는 문자의 종류 중 현재 윈도우 내에서 필요한 만큼 채워진 문자의 수
        int formed = 0;

        // 윈도우에 각 문자가 등장한 횟수
        unordered_map<char, int> windowCounts;

        // 윈도우 길이, 왼쪽 인덱스, 오른쪽 인덱스
        int ans[3] = { -1, 0, 0 };

        while (r < s.length())
        {
            // 오른쪽 포인터가 가리키는 문자를 윈도우에 추가
            char c = s[r];
            windowCounts[c]++;

            // t에서 등장한 횟수가 같다면 formed 증가
            if (dictT.contains(c) && windowCounts[c] == dictT[c])
            {
                formed++;
            }

            // 윈도우가 조건을 만족하는 동안 루프
            // 즉, 더 이상 조건을 만족하지 않을 때 까지 왼쪽 포인터를 이동하여 윈도우를 축소시켜봄
            while (l <= r && formed == required)
            {
                c = s[l];
                
                // 현재까지 발견한 가장 작은 윈도우 정보를 저장
                if (ans[0] == -1 || r - l + 1 < ans[0])
                {
                    ans[0] = r - l + 1;
                    ans[1] = l;
                    ans[2] = r;
                }

                // 왼쪽 포인터가 가리키는 문자를 윈도우에서 제거
                windowCounts[c]--;

                // 그 결과, 문자가 t에서 등장한 횟수를 충족하지 못하면 formed 감소
                if (dictT.contains(c) && windowCounts[c] < dictT[c])
                {
                    formed--;
                }

                // 왼쪽 포인터 이동
                l++;
            }

            // 축소해가며 탐색이 끝났으면 오른쪽 포인터를 이동
            r++;
        }

        return ans[0] == -1 ? "" : s.substr(ans[1], ans[2] - ans[1] + 1);
    }
};
