/**
 * For the height H of the given BST,
 * 
 * Time complexity: O(max(H, K))
 *   - if H > K, O(H) at worst
 *   - else, O(K)
 * 
 * Space complexity: O(H > K ? H + K : K)
 *   - additional vector to save nums O(K)
 *   - if H > K, call stack O(H)
 *   - else, O(K)
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
    void inorder(TreeNode* node, vector<int>& v, int max_size) {
        if (!node || v.size() == max_size) return;

        if (node->left) inorder(node->left, v, max_size);
        v.push_back(node->val);
        if (node->right) inorder(node->right, v, max_size);
    }

    int kthSmallest(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums, k);

        return nums[k - 1];
    }
};