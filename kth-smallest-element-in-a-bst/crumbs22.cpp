/*
    dfs로 트리 탐색하며 k번째로 작은 값을 찾음
    왼쪽서브트리-> 루트 -> 오른쪽 서브트리 순으로 탐색 (중위순회)    
    왼쪽 서브트리를 먼저 탐색함 (값이 작은 순으로 탐색하기 위함)
    - 왼쪽이 없으면 return -1
    - 현재 노드 방문 -> k를 1 감소
    - 오른쪽도 같은 방식으로 탐색
    - 자식에서 -1을 반환 받았을 때에는 k번째 작은 값을 찾지 못한 상태로, k값을 줄이며 계속 탐색
    - 자식에서 -1이 아닌 값을 반환 받았을 때에는 k번째 작은 값을 찾은 상태로, 해당 값을 계속적으로 반환
*/
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        return (dfs(root, k));
    }

    int dfs(TreeNode* root, int &k) {
        if (!root)
            return -1;

        int l = dfs(root->left, k);
        if (l != -1) 
            return l; 
        k--;
        if (k == 0) // 현재 노드가 k번째로 작은 값일 때
            return root->val;
        return dfs(root->right, k);
    }
};
