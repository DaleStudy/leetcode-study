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
    bool ans = true;
    void rec(TreeNode* p, TreeNode* q) {
        if(p == nullptr && q == nullptr)
            return;
        else if(p && q && p->val == q->val) {
            rec(p->left, q->left);
            rec(p->right, q->right);
        }
        else 
            ans = false;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        rec(p, q);
        return ans;
    }
};

