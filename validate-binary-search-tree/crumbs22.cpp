#include <iostream>
#include <climits>

using namespace std;

/*
	TC: O(n)
		중복되는 방문 없이 모든 노드를 한번씩 방문하므로 O(n)
	SC: O(h)
		재귀 호출의 깊이는 트리의 높이와 같다
		최악의 경우 O(N)이고 최선의 경우엔 O(logn)이다

	풀이 방법: 
		전위순회를 하면서 왼쪽 자식노드와 오른쪽 자식노드에 대한 깊이탐색을 수행한다
		INT_MIN 혹은 INT_MAX에 대한 값을 처리하기 위해 초기 min과 max값을 long형으로 둔다
*/

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
		return (dfs(root, LONG_MIN, LONG_MAX));
    }
	bool dfs(TreeNode *node, long min, long max)
	{
		if (!node)
			return (true);
		if (node->val <= min || node->val >= max)
			return (false);
		if (dfs(node->left, min, node->val) && dfs(node->right, node->val, max))
			return (true);
		else
			return (false);
	}
};
