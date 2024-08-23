
/**
 * * 문제에서 정의된 타입
 */
export class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

/**
 * ! 문제에서의 Output과 실제 정의된, 사용되는 output이 다르기 때문에, 한 번 변환 작업을 거처야함. (실제 제출 시 제외한 함수 입니다.)
 */
// function treeToArray(root: TreeNode | null): (number | null)[] {
//     if (!root) return [];
//     const result: (number | null)[] = [];
//     const queue: (TreeNode | null)[] = [root];
//     while (queue.length > 0) {
//         const node = queue.shift();
//         if (node) {
//             result.push(node.val);
//             queue.push(node.left);
//             queue.push(node.right);
//         } else {
//             result.push(null);
//         }
//     }
//     while (result[result.length - 1] === null) result.pop();
//     return result;
// }

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (preorder.length === 0 || inorder.length === 0) return null;

    const rootVal = preorder[0];
    const inorderIndex = inorder.indexOf(rootVal);
    const leftInorder = inorder.slice(0, inorderIndex);

    return new TreeNode(
        rootVal,
        buildTree(
            preorder.slice(1, 1 + leftInorder.length),
            leftInorder
        ),
        buildTree(
            preorder.slice(1 + leftInorder.length),
            inorder.slice(inorderIndex + 1)
        ),
    );
}


// const preorder = [3, 9, 20, 15, 7];
// const inorder = [9, 3, 15, 20, 7];
// console.log('output:', treeToArray(buildTree(preorder, inorder))); 
