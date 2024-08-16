// Time Complexity: O(nlogn)
// Spatial Complexity O(n)

#include <vector>
#include <queue>
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
    int kthSmallest(TreeNode* root, int k) {
        queue<TreeNode*> q;
        q.push(root);

        vector<int> numbers;
        TreeNode *curNode, *nextNode;
        while(!q.empty()) {
            curNode = q.front();
            q.pop();

            numbers.push_back(curNode->val);

            nextNode = curNode->left;
            if(nextNode != nullptr) {
                q.push(nextNode);
            }

            nextNode = curNode->right;
            if(nextNode != nullptr) {
                q.push(nextNode);
            }
        }

        sort(numbers.begin(), numbers.end());
        return numbers[k - 1];
    }
};

