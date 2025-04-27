/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

type TreeNodeNullable = TreeNode | null;

function maxDepth(root: TreeNode | null): number {
    
    // 방법1: [실패]
    // - 접근법 : depth를 1부터 ++해 감
    //          left right 덮어 씌워가면서 없어질 때까지 보고 마지막 depth return
    // - 실패 이유 : left.left || left.right || null에서 left.left의 Depth가 left.right보다 작을 수 있는데, 이때 끝까지 보질 못함
    // const getMaxDepth1 = () => {
    //     let left: TreeNodeNullable = root?.left ?? null;
    //     let right: TreeNodeNullable = root?.right ?? null;
    //     let depth = (left === null && right === null && (root?.val === undefined || root?.val === null)) ? 0 : 1;        
    //     console.log('debug::', left, right, depth)

    //     while(left || right) {
    //         if(left) {
    //             left = left.left || left.right || null;
    //         };
    //         if (right) {
    //             right = right.left || right.right || null;
    //         };
    //         depth++;
    //     }

    //     return depth;
    // };

    // 방법2: BFS(너비 우선 탐색) 방식
    // - 접근법 : Set객체를 활용해서 left, right 중에 있는 것을 추가한다.
    //          count++하고 Set객체에 있는 것 중에 left,right에 있는 것들을 다시 Set객체에 넣는다. 이걸 반복한다.
    // - 시간 복잡도: O(n) - 모든 노드를 한 번씩 방문
    // - 공간 복잡도: O(w) - w는 트리의 최대 너비(최대 레벨에 있는 노드의 수)
    const getMaxDepth2 = () => {
        let nodeSet = new Set<TreeNode>()
        let count = 0;
    
        const addNodeSetByTreeNode = (node: TreeNode | null, nodeSet: Set<TreeNode>) => {
            if(node?.left) {
                nodeSet.add(node.left);
            };
            if(node?.right){
                nodeSet.add(node.right);
            }
        }

        addNodeSetByTreeNode(root, nodeSet);
        if(nodeSet.size !== 0 || root?.left === null && root?.right === null && root?.val !== null) {
            count++;
        }

        while(nodeSet.size !== 0) {
            let nextNodeSet = new Set<TreeNode>()
            nodeSet.forEach((node) => {
                addNodeSetByTreeNode(node, nextNodeSet);
            });
            nodeSet = nextNodeSet;
            count++;
        }

        return count;
    };

    // 방법3: (with GPT)
    // - 접근법 : DFS(깊이 우선 탐색) 재귀 방식
    // - 시간 복잡도: O(n) - 모든 노드를 한 번씩 방문
    // - 공간 복잡도: O(h) - h는 트리의 높이(재귀 호출 스택의 최대 깊이)
    const getMaxDepth3 = (root: TreeNode | null) => {
        if (root === null) return 0;
        return 1 + Math.max(getMaxDepth3(root.left), getMaxDepth3(root.right));
    };

    // return getMaxDepth1();
    // return getMaxDepth2();
    return getMaxDepth3(root);
    
};
