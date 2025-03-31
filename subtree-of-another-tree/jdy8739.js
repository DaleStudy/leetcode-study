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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
    const tree = [`'${root?.val}'`];
    const subTree = [`'${subRoot?.val}'`];

    const dfsStringify = (node, arr) => {
        arr.push(`'${node.left?.val}'` ?? 'null');
        if (node?.left) {
            dfsStringify(node.left, arr);
        }

        arr.push(`'${node.right?.val}'` ?? 'null');
        if (node?.right) {
            dfsStringify(node.right, arr);
        }
    }

    dfsStringify(root, tree);
    dfsStringify(subRoot, subTree);

    const treeString = tree.join(',');
    const subTreeString = subTree.join(',');

    return treeString.includes(subTreeString);
};

// 시간복잡도 O(n + m) -> root tree와 subRoot tree의 노드를 모두 방문하기때문에 root의 노드 수인 n과 subRoot의 노드 수인 m을 더한 값
// 공간복잡도 O(n + m) -> 두 트리의 노드 수를 저장하는 배열의 크기가 각각 n과 m이기 때문
