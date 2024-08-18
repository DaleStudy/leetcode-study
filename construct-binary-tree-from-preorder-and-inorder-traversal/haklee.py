"""TC: O(n), SC: O(n)

아이디어:
- preorder 트리가 주어져 있다면 다음과 같이 분할할 수 있다.
    - [root값, [...left], [...right]]
    - 위의 left, right는 preorder 트리와 같은 방식으로 구성된다.
- inorder 트리가 주어져 있다면 다음과 같이 분할할 수 있다.
    - [[...left], root값, [...right]]
    - 위의 left, right는 inorder 트리와 같은 방식으로 구성된다.
    - 이때, 
        - left의 첫 아이템이 인덱스 inorder_s에 있고,
        - right의 마지막 아이템이 인덱스 inorder_e - 1에 있다고 하자.
        - 즉, inorder_e를 미포함!
- preorder 트리의 맨 앞 값을 통해 root값 val을 찾고, 이 값으로 inorder의 root값의 인덱스를 찾을 수 있다.
    - 모든 node의 val값이 unique한 것이 조건으로 주어져 있으므로 val값의 indices를 전처리해둘 수 있다.
    - 이때, inorder의 root값의 인덱스를 inorder_root이라고 하자.
- inorder의 root값의 위치와 inorder 트리의 시작 위치를 알 수 있다면
    [...left]의 길이 left_len을 알 수 있다.
    - left_len = inorder_root - inorder_start
- preorder 트리의 left의 루트는 [...left]의 첫 아이템, 즉, preorder_root에 1을 더한 값이다.
- preorder 트리의 right의 루트는 [...right]의 첫 아이템, 즉, preorder_root + 1 + left_len이다.
- root값을 구할 수 없으면 노드가 없다.
    - inorder_s >= inorder_e와 같이 판별이 가능하다. 즉, 아이템이 하나도 없는 경우.

위의 아이디어를 종합하면,
- preorder 트리의 루트 인덱스 preorder_root가 주어진, 구간 (inorder_s, inorder_e)에서 정의된 inorder 트리는
    - val값은 preorder[preorder_root]이 된다.
    - left node는 아래와 같이 구해진다.
        - preorder 트리의 루트 인덱스 preorder_root + 1,
        - 구간 (inorder_s, inorder_root)
        - 이때 구간이 유효하지 않으면 노드가 없다.
    - right node는 아래와 같이 구해진다.
        - preorder 트리의 루트 인덱스 preorder_root + 1 + left_len,
        - 구간 (inorder_root + 1, inorder_end)
        - 이때 구간이 유효하지 않으면 노드가 없다.


SC:
- 처음 inorder_indices를 계산할때 O(n).
- 아래의 build함수 호출이 최대 트리의 깊이만큼 재귀를 돌면서 쌓일 수 있다.
    - 트리의 깊이는 최악의 경우 O(n).
    
TC:
- build함수는 O(1). 코드 참조.
- 위의 과정을 n개의 노드에 대해 반복하므로 O(n).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}

        def build(inorder_s, inorder_e, preorder_root):
            if inorder_s >= inorder_e:  # O(1)
                return None
            val = preorder[preorder_root]  # O(1)
            inorder_root = inorder_indices[val]  # O(1)
            left_len = inorder_root - inorder_s  # O(1)
            return TreeNode(
                val,
                left=build(inorder_s, inorder_root, preorder_root + 1),
                right=build(inorder_root + 1, inorder_e, preorder_root + 1 + left_len),
            )

        return build(0, len(inorder), 0)


"""
그런데 위의 아이디어를 다시 생각해보면, 모든 노드들을 preorder 순서로 순회한다!
- `val = preorder[preorder_root]`와 같은 방식으로 val값을 구하지 않고, 주어진 preorder를 순서대로 가져와도 됨.
- 즉, preorder를 iterator로 바꿔서 next를 통해 값을 하나씩 뽑아와서 건네줘도 된다.
- 이렇게 하면 build함수에 preorder_root를 전달하지 않아도 됨.
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def build(inorder_s, inorder_e):
            if inorder_s >= inorder_e:  # O(1)
                return None
            val = next(preorder_iter)  # O(1)
            inorder_root = inorder_indices[val]  # O(1)
            return TreeNode(
                val,
                left=build(inorder_s, inorder_root),
                right=build(inorder_root + 1, inorder_e),
            )

        return build(0, len(inorder))
