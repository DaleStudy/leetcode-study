// Time Complexity: O(n^2)
// Spatial Complexity: O(n)

class Solution {
private:
    int findIndex(int targetVal, vector<int>& inorder) {
        auto pos = find(inorder.begin(), inorder.end(), targetVal);
        if (pos == inorder.end()) {
            return -1;
        }

        return pos - inorder.begin();
    }

    TreeNode* dfs(vector<int>& preorder, vector<int>& inorder, int preorderIndex, int startIndex, int endIndex) {
        if (preorder.size() <= preorderIndex || startIndex > endIndex) {
            return nullptr;
        }

        int targetValue = preorder[preorderIndex];
        int rootIndex = this->findIndex(targetValue, inorder);
        if(rootIndex < 0) {
            return nullptr;
        }

        int leftSubtreeLength = rootIndex - startIndex;

        TreeNode* left = dfs(preorder, inorder, preorderIndex + 1, startIndex, rootIndex - 1); 
        TreeNode* right = dfs(preorder, inorder, preorderIndex + 1 + leftSubtreeLength, rootIndex + 1, endIndex);

        return new TreeNode(targetValue, left, right);
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return this->dfs(preorder, inorder, 0, 0, preorder.size() - 1);
    }
};
