/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    const dfs = (a, b) => {
        const isValSame = a?.val === b?.val;
        const isLeftValSame = a?.left?.val === b?.left?.val;
        const isRightValSame = a?.right?.val === b?.right?.val;

        if (!isValSame || !isLeftValSame || !isRightValSame) {
            return true;
        }

        if (a?.left && b?.left) {
            const isLeftDiff = dfs(a.left, b.left);

            if (isLeftDiff) {
                return true;
            }
        }
W

        if (a?.right && b?.right) {
            const isRightDiff = dfs(a.right, b.right);

            if (isRightDiff) {
                return true;
            }
        }
        
    }


    return !dfs(p, q);
};

// 시간복잡도 - O(n) p와 q가 같다면 모든 노드를 방문하므로
// 공간복잡도 - O(h) 깊이우선탐색을 사용하여 트리의 최대 높이만큼 실행환경이 함수호출스택에 저장되므로
