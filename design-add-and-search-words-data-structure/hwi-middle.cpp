// 풀이 접근: Trie로 해결

class WordDictionary {
public:
    WordDictionary() {
        mRoot = make_unique<Node>(); // RAII를 위해 스마트 포인터 사용
    }
    
    void addWord(string word) {
        Node* curNode = mRoot.get();
		for (char c : word)
		{
            auto& child = curNode->children[c - 'a'];
    		if (child == nullptr)
			{
				child = make_unique<Node>();
			}

			curNode = child.get();
		}

		curNode->isWord = true;
    }
    
    bool search(string word) {
        return search_impl(word, mRoot.get());
    }

private:
	struct Node
	{
		bool isWord = false;
		unique_ptr<Node> children[26];
	};

	unique_ptr<Node> mRoot;

    // 복사 없는 substr을 위해 std::string_view 활용
    bool search_impl(string_view word, Node* root)
    {
        Node* curNode = root;
		for (int i = 0; i < word.size(); ++i)
		{
            char c = word[i];
            if (c == '.') // '.'은 와일드 카드이므로 자식 노드를 모두 순회하며 시도
            {
                for (auto& p : curNode->children)
                {
                    if (p != nullptr && search_impl(word.substr(i + 1), p.get()))
                    {
                        return true;
                    }
                }

                return false;
            }
            else
            {
                auto& child = curNode->children[c - 'a'];
                if (child == nullptr)
                {
                    return false;
                }

                curNode = child.get();
            }
		}

		return curNode->isWord;
    }
};
