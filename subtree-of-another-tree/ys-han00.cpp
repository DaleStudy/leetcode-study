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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        if (p->val != q->val) return false;

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr) return false;
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
    
    // bool ans = false;
    // void check(TreeNode* root, TreeNode* subRoot) {
    //     if(root == nullptr || subRoot == nullptr || root->val != subRoot->val) {
    //         if(root != nullptr || subRoot != nullptr)
    //             ans = false;
    //         return;
    //     }
    //     check(root->left, subRoot->left);
    //     check(root->right, subRoot->right);
    // }

    // void rec(TreeNode* root, TreeNode* subRoot) {
    //     if(root == nullptr || ans)
    //         return;
    //     if(root->val == subRoot->val) {
    //         ans = true;
    //         check(root, subRoot);
    //         if(ans) return;
    //     }
    //     rec(root->left, subRoot);
    //     rec(root->right, subRoot);
    // }

    // bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    //     rec(root, subRoot);
    //     return ans;
    // }
};
