/*
    풀이 :
        result를 int의 최솟값으로 초기화하고 시작

        두가지 기능을 하는 함수 하나를 생성
            1. left, root->val, right의 합(하나의 path/\를 이룸)을 통해 maxSum을 업데이트
            2. max (left 노드 합, right 노드 합)과 root를 더해서 return 
                -> left, right 둘 중 하나만 포함해야 상위 tree에서 path의 일부로 사용가능
                   /\
                  /  \
                 /   /
                 \
            이 때, 음수 노드의 합은 max(0, value)를 통해 버리고 left + right + root->val을 통해 추가적인 계산 없이 maxSum 업데이트
        
    노드 개수 : N

    TC : O(N)
        모든 노드 순회

    SC : O(N)
        재귀 호출 스택도 노드 개수에 비례
*/


#include <limits.h>
#include <algorithm>

using namespace std;

class Solution {
    public:
        int maxPathSum(TreeNode* root) {
            int result = INT_MIN;
    
            dfs(root, result);
            return result;
        }

        int dfs(TreeNode* root, int& maxSum) {
            if (!root)
                return 0;
    
            int left = max(0, dfs(root->left, maxSum));
            int right = max(0, dfs(root->right, maxSum));
    
            maxSum = max(maxSum, left + right + root->val);
    
            return root->val + max(left, right);
        }
    };

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
