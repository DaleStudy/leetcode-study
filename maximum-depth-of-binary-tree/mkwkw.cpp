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
    int maxDepth(TreeNode* root) {
        
        //root가 비어있는 경우
        if(root == nullptr)
        {
            return 0;
        }

        stack<TreeNode*> nodeStack;
        stack<int> depthStack;
        int maxDepth = 0;

        nodeStack.push(root);
        depthStack.push(1);

        while(!nodeStack.empty())
        {
            TreeNode* rootNode = nodeStack.top(); //change root pointer
            int rootDepth = depthStack.top();
            maxDepth = max(maxDepth, rootDepth);
            nodeStack.pop();
            depthStack.pop();

            //making max depth binary tree
            if(rootNode->left != nullptr)
            {
                nodeStack.push(rootNode->left);
                depthStack.push(rootDepth+1);
            }

            if(rootNode->right != nullptr)
            {
                nodeStack.push(rootNode->right);
                depthStack.push(rootDepth+1);
            }
            
        }
        return maxDepth;
    }
};
