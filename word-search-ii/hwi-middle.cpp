class Solution {
private:
    // 트라이(Trie)를 활용
	struct Node
	{
		bool isWord = false;
		Node* children[26];
        Node() : isWord(false) 
        {
            fill(children, children + 26, nullptr);
        }

        bool isEmpty()
        {
            for (int i = 0; i < 26; ++i)
            {
                if (children[i] != nullptr)
                {
                    return false;
                }
            }

            return true;
        }
	};

    // 각 노드는 배열로 관리
    static constexpr size_t POOL_SIZE = 300001;
    Node pool[POOL_SIZE];
    int poolIdx = 0;

    Node* newNode()
    {
        pool[poolIdx] = Node();
        return &pool[poolIdx++];
    }

    Node* root;
    vector<string> ans;
    int row;
    int col;

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // 트라이 구성 시작
        poolIdx = 0;
        ans.clear();
        root = newNode();
        for (auto& word : words)
        {
            Node* cur = root;
            for (auto ch : word)
            {
                auto& child = cur->children[ch - 'a'];
                if (child == nullptr)
                {
                    child = newNode();
                }

                cur = child;
            }

            cur->isWord = true;
        }

        // 한 칸씩 탐색 시작
        row = board.size();
        col = board[0].size();
        for (int r = 0; r < row; ++r)
        {
            for (int c = 0; c < col; ++c)
            {
                string s = "";
                solve(board, root, s, r, c);
            }
        }

        return ans;
    }

    void solve(vector<vector<char>>& board, Node*& node, string& s, int r, int c)
    {
        // 경로가 제거된 경우
        if (node == nullptr)
        {
            return;
        }
        
        // 범위를 벗어난 경우
        if (r < 0 || r >= row || c < 0 || c >= col) 
        {
            return;
        }

        // 이미 방문한 경우
        char ch = board[r][c];
        if (ch == '?')
        {
            return;
        }

        // 트라이에 이 문자가 없는 경우 (찾을 단어에 포함되지 않음)
        if (node->children[ch - 'a'] == nullptr)
        {
            return;
        }

        // 이 문자가 하나의 단어를 구성하는 경우
        if (node->children[ch - 'a']->isWord)
        {
            s.push_back(ch);
            ans.push_back(s);
            s.pop_back();
            node->children[ch - 'a']->isWord = false; // 중복 마킹 방지
        }
        
        board[r][c] = '?'; // 이미 방문한 곳으로 돌아오지 않도록 입력으로 들어오지 않는 문자로 치환

        // 상하좌우 탐색
        static int dr[4] = { 1, 0, -1, 0 };
        static int dc[4] = { 0, 1, 0, -1 };

        for (int dir = 0; dir < 4; ++dir)
        {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            s.push_back(ch);
            solve(board, node->children[ch - 'a'], s, nr, nc);
            s.pop_back();
        }
        
        board[r][c] = ch; // 원래 문자로 되돌리기

        // 더 이상 탐색이 필요 없는 곳은 경로 자체를 제거
        // 일단 자식 먼저 판단
        Node*& child = node->children[ch - 'a'];
        if (child != nullptr && !child->isWord && child->isEmpty()) 
        {
            child = nullptr;  
        }

        // 자신도 지울 수 있으면 지움
        if (!node->isWord && node->isEmpty())
        {
            node = nullptr;
        }
    }
};
