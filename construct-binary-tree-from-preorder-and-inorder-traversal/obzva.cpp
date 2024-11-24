/**
 * For the number of given nodes N,
 * 
 * Time complexity: O(N)
 * 
 * Space complexity: O(N) at worst
 */

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inorder_index_map;
        stack<TreeNode*> tree_stack;

        for (int i = 0; i < inorder.size(); i++) inorder_index_map[inorder[i]] = i;

        TreeNode* root = new TreeNode(preorder[0]);
        tree_stack.push(root);

        for (int i = 1; i < preorder.size(); i++) {
            TreeNode* curr = new TreeNode(preorder[i]);

            if (inorder_index_map[curr->val] < inorder_index_map[tree_stack.top()->val]) {
                tree_stack.top()->left = curr;
            } else {
                TreeNode* parent;
                while (!tree_stack.empty() && inorder_index_map[curr->val] > inorder_index_map[tree_stack.top()->val]) {
                    parent = tree_stack.top();
                    tree_stack.pop();
                }
                parent->right = curr;
            }
            tree_stack.push(curr);
        }

        return root;
    }
};
