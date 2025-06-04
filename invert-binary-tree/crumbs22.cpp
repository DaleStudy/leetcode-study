/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
	public:
		TreeNode* invertTree(TreeNode* root) {
			// 종료 조건
			if (!root)
				return (nullptr);

			// 노드 반전 (중위순회)
			TreeNode* tmp = root->left;
			root->left = root->right;
			root->right = tmp;

			// 재귀적 호출
			invertTree(root->left);
			invertTree(root->right);
			return (root);
		}
	};
