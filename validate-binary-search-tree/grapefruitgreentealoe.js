/*
유효한 BST는 이렇게 정의가 된다.
1. 노드의 좌측 서브 트리에는 노드의 키보다 작은 키를 가진 노드만 있다.
2. 노드의 우측 서브 트리에는 노드의 키보다 큰 키를 가진 노드만 있다.
3. 좌 우측 서브 트리도 모두 이진 탐색 트리여야 한다.

트리의 순회는 재귀로 순회가 가능하다.
또한 BST 의 특성에 맞게, 하위값, 상한값의 개념이 들어간다.
만약 좌측으로 순회하게 될때는
하위값은 부모노드의 하한값.
상한값은 부모노드의 값이 된다.

우측 서브트리로 내려갈 때는,
하위값은 부모노드의 값,
상한값은 부모노드의 상한값이 된다.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    function dfs(node,low,high){
        if(!node) return true; // leaf
        if(
            (low !==null && node.val <= low)||
            (high !== null && node.val >= high)){
            return false
        }
        return dfs(node.left,left,node.val) && dfs(node.right,node.val,high)

    }
    dfs(root,null,null)
};



/*
2. 두번째로는 중위순회로 해결할 수 있다. 
중위순회 : 왼쪽 → 현재 노드 → 오른쪽 순서로 방문하는 방식

이진탐색 트리는 오름차순으로 모든 노드를 방문할 수 있다. 
좌측트리를 먼저 순회하고, 부모노드를 방문하고, 그 다음 우측 트리를 순회하기 때문이다. 

따라서, 중위순회가 오름차순으로 진행되지 않는다면 이것은 유효한 이진 트리가 아니다. 
*/
var isValidBST = function(root) {
  let prev = null;

  function inorder(node) {
    if (!node) return true; //leaf

    if (!inorder(node.left)) return false;

    //좌측 순회
    if (prev !== null && node.val <= prev) return false;
    prev = node.val;

    return inorder(node.right);
  }

  return inorder(root);
};
// 둘다 시간복잡도 O(N)이다.
// 공간복잡도 O(h) (재귀 스택만큼)

