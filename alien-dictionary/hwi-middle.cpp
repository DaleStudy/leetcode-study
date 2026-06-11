class Solution
{
public:
    string alienOrder(vector<string>& words)
    {
        unordered_map<char, unordered_set<char>> graph; // 해당 문자 뒤에 와야하는 문자들
        unordered_map<char, int> state; // DFS 방문 상태: 0(방문 안함), 1(방문 중), 2(방문 완료)

        // 모든 문자를 그래프에 넣음
        for (const auto& word : words)
        {
            for (char c : word)
            {
                graph[c];
            }
        }

        // 인접한 문자 비교
        for (int i = 0; i < words.size() - 1; ++i)
        {
            string& a = words[i];
            string& b = words[i + 1];

            int len = min(a.size(), b.size());

            int j = 0;
            while (j < len && a[j] == b[j])
            {
                ++j;
            }

            // 마지막까지 동일한 경우
            if (j == len)
            {
                // 사전순인데 앞 단어가 더 길면 규칙 위반
                if (a.size() > b.size())
                {
                    return "";
                }

                // 정상이지만 정보가 없음
                continue;
            }

            // 다른 문자를 찾은 경우 (그 부분만 의미있음)
            graph[a[j]].insert(b[j]);
        }

        string result;

        // 이제 위상정렬 -> 후위순회 dfs 후 순서 뒤집기
        function<bool(char)> dfs = [&](char node)
        {
            if (state[node] == 1)
            {
                return false; // 사이클
            }

            if (state[node] == 2)
            {
                return true;
            }

            state[node] = 1;

            for (char next : graph[node])
            {
                if (!dfs(next))
                {
                    return false;
                }
            }

            state[node] = 2;
            result.push_back(node);

            return true;
        };

        for (auto& [node, _] : graph)
        {
            if (state[node] == 0)
            {
                if (!dfs(node))
                {
                    return "";
                }
            }
        }

        reverse(result.begin(), result.end());

        return result;
    }
};
