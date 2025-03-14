/**
 * 이진 트리 노드의 정의입니다.
 * class TreeNode {
 *     val: number;
 *     left: TreeNode | null;
 *     right: TreeNode | null;
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val === undefined ? 0 : val);
 *         this.left = (left === undefined ? null : left);
 *         this.right = (right === undefined ? null : right);
 *     }
 * }
 */

/**
 * 이진트리 깊이별 노드 값들을 배열로 저장하는 함수.
 * 
 * @param {TreeNode | null} root - 이진 트리의 루트 노드
 * @returns {number[][]} - 각 레벨별 노드 값들이 담긴 2차원 배열 반환
 * 
 * 시간 복잡도: O(n) 
 *   - 모든 노드를 한 번씩 방문
 * 공간 복잡도: O(n) 
 *   - 재귀 호출 스택 및 결과 배열 사용
 */
function levelOrder(root: TreeNode | null): number[][] {
    // idx -> 각 깊이별 노드 값들을 저장
    const result: number[][] = [];

    const dfs = (node: TreeNode | null, depth: number): void => {
        // 노드가 null이면 재귀 종료
        if (node === null) return;
        
        // 현재 depth를 처음 방문되는 경우, 결과 배열에 새로운 depth 배열을 추가
        if (result.length === depth) {
            result.push([]);
        }
        
        // 현재 노드의 값을 해당 레벨 배열에 추가
        result[depth].push(node.val);
        
        // 왼쪽 자식 노드를 방문 (depth 1 증가시킴)
        dfs(node.left, depth + 1);
        // 오른쪽 자식 노드를 방문 (depth 1 증가시킴)
        dfs(node.right, depth + 1);
    }

    // depth 0부터 탐색 시작
    dfs(root, 0);
    return result;
};

