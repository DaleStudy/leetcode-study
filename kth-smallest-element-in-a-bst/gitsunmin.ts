/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * time complexity : O(n)
 * space complexity : O(n)
 */

/**
 * * 문제에서 정의된 타입
 */
class TreeNode {
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
 * ! 문제에서의 Input과 실제 정의된, 사용되는 input이 다르기 때문에, 한 번 변환 작업을 거처야함. (실제 제출 시 제외한 함수 입니다.)
 */
const arrayToTreeNode = (arr: Array<number | null>) => (k: number): [TreeNode | null, number] => {
    let root = new TreeNode(arr[0]!);
    let queue: (TreeNode | null)[] = [root];
    let i = 1;

    while (i < arr.length) {
        let current = queue.shift();
        if (current !== null && current !== undefined) {
            if (arr[i] !== null) {
                current.left = new TreeNode(arr[i]!);
                queue.push(current.left);
            }
            i++;
            if (i < arr.length && arr[i] !== null) {
                current.right = new TreeNode(arr[i]!);
                queue.push(current.right);
            }
            i++;
        }
    }

    return [root, k];
}

// const input1 = arrayToTreeNode([3, 1, 4, null, 2]);
// const input2 = arrayToTreeNode([5, 3, 6, 2, 4, null, null, 1]);

// const output1 = kthSmallest(...input1(1))
// const output2 = kthSmallest(...input2(3))

// console.log('output1:', output1);
// console.log('output2:', output2);


function inOrderTraversal(node: TreeNode | null): number[] {
    if (node === null) {
        return [];
    }

    return [
        ...inOrderTraversal(node.left),
        node.val,
        ...inOrderTraversal(node.right)
    ];
}

function kthSmallest(root: TreeNode | null, k: number): number {
    const result = inOrderTraversal(root);
    return result[k - 1]
}