class Trie
{
public:
	Trie()
	{
        mRoot = make_unique<Node>();
	}

	void insert(string word)
	{
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

	bool search(string word)
	{
		Node* curNode = mRoot.get();
		for (char c : word)
		{
            auto& child = curNode->children[c - 'a'];
			if (child == nullptr)
			{
				return false;
			}

			curNode = child.get();
		}

		return curNode->isWord;
	}

	bool startsWith(string prefix)
	{
		Node* curNode = mRoot.get();
		for (char c : prefix)
		{
            auto& child = curNode->children[c - 'a'];
			if (child == nullptr)
			{
				return false;
			}

			curNode = child.get();
		}

		return true;
	}

private:
	struct Node
	{
		bool isWord = false;
		unique_ptr<Node> children[26];
	};

	unique_ptr<Node> mRoot;
};
