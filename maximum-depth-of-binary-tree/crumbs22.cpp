#include <algorithm>

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
		int maxDepth(TreeNode* root) {
			if (!root)
				return (0);
			return (getMaxDepth(root));
		}

		int getMaxDepth(TreeNode* node, int depth = 0) {
			if (!node)
				return (depth);
			return std::max(getMaxDepth(node->left, depth + 1), getMaxDepth(node->right, depth + 1));
		}
	};
