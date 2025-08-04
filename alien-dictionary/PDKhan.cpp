class Solution {
public:
    string alienOrder(vector<string> &words) {
        // Write your code here
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> indegree;
        unordered_set<char> all_chars;

        for (const string& word : words) {
            for (char c : word) {
                all_chars.insert(c);
                if (!indegree.count(c))
                    indegree[c] = 0;
            }
        }

        for(int i = 0; i < words.size() - 1; i++){
            string word1 = words[i];
            string word2 = words[i + 1];
            int len = min(word1.size(), word2.size());
            bool found = false;

            for(int j = 0; j < len; j++){
                char ch1 = word1[j];
                char ch2 = word2[j];

                if(ch1 != ch2){
                    if(graph[ch1].count(ch2) == 0){
                        graph[ch1].insert(ch2);
                        indegree[ch2]++;
                    }

                    found = true;
                    break;
                }
            }

            if(!found && word1.size() > word2.size())
                return "";
        }

        queue<char> q;
        for(char c : all_chars){
            if(indegree[c] == 0)
                q.push(c);
        }

        string order;

        while(!q.empty()){
            char cur = q.front();
            q.pop();

            order += cur;

            for(char next : graph[cur]){
                if(--indegree[next] == 0)
                    q.push(next);
            }
        }

        if(order.size() != all_chars.size())
            return "";

        return order;
    }
};
