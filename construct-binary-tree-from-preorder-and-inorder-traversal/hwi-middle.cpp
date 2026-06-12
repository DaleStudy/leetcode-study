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

 // 전위 순회의 첫 번째로 나오는 노드가 루트라는 성질을 활용
 // 중위 순회에서 루트를 찾아 좌우 구분 가능
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTreeWithSpan(span(preorder), span(inorder));
    }

    TreeNode* buildTreeWithSpan(span<int> preorder, span<int> inorder)
    {
        if (preorder.size() == 0)
        {
            return nullptr;
        }

        int rootVal = preorder[0];
        TreeNode* rootNode = new TreeNode(rootVal);
        if (preorder.size() == 1)
        {
            return rootNode;    
        }
        int leftSubtreeSize = find(inorder.begin(), inorder.end(), rootVal) - inorder.begin();
        int n = inorder.size();
        span<int> leftPreorder = preorder.subspan(1, leftSubtreeSize);
        span<int> leftInorder = inorder.subspan(0, leftSubtreeSize);
        span<int> rightPreorder = preorder.subspan(leftSubtreeSize + 1, n - leftSubtreeSize - 1);
        span<int> rightInorder = inorder.subspan(leftSubtreeSize + 1, n - leftSubtreeSize - 1);
        rootNode->left = buildTreeWithSpan(leftPreorder, leftInorder);
        rootNode->right = buildTreeWithSpan(rightPreorder, rightInorder);
        return rootNode;
    }
};
