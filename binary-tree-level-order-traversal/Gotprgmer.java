/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// preorder에서 맨 왼쪽을 root
// root값을 기반으로 inorder에서 인덱스를 찾는다 그리고 왼쪽 오른쪽 길이를 구한다.
// 다시 buildTree 함수를 재귀하는데 이때 위에서 구한 왼쪽 길이와 오른쪽길이를 참고해서
// 왼쪽 buildTree
// value를 갱신
// 오른쪽 buildTree를 갱신한다.

// 시간복잡도 : O(N^2) -> 한쪽으로 치우친 트리일 경우 O(N)(index of) + T(N-1)이 될 수 있다.
// 위 식을 전개해보면 N + N-1 + N-2 + ... + 1 = N(N+1)/2 = O(N^2)
// 공간복잡도 : O(N) ->리트코드 but N길이의 리스트 크기*N번의 재귀호출이 일어날 수 있다. 따라서 O(N^2)가 아닌가...?
class SolutionGotprgmer {
    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if(preorder.length == 0 || indexOf(inorder,preorder[0]) == -1){
            return null;
        }
        TreeNode node = new TreeNode();

        int root = preorder[0];
        int indexOfRoot = indexOf(inorder,root);
        int leftCnt = indexOfRoot;
        // 찾으면
        node.val = root;
        node.left = buildTree(Arrays.copyOfRange(preorder,1,1+leftCnt),Arrays.copyOfRange(inorder,0,leftCnt));
        node.right = buildTree(Arrays.copyOfRange(preorder,1+leftCnt,preorder.length),Arrays.copyOfRange(inorder,1+leftCnt,inorder.length));
        return node;
    }
    public int indexOf(int[] intArray,int findNum){
        for(int i=0;i<intArray.length;i++){
            if(findNum==intArray[i]){
                return i;
            }
        }
        return -1;
    }

}
