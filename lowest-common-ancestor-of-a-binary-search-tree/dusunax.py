'''
# 235. Lowest Common Ancestor of a Binary Search Tree

## 기본적인 LCA 찾기 문제이다.
- LCA는 두 노드의 최저 공통 조상이다.
- 두 노드를 descendants로 가진 노드이며, 두 노드도 포함된다.

### LCA와 이진 탐색 트리 BST, 일반 이진트리 BT
BST는 부모의 정렬 조건이 있고, BT는 부모의 정렬 조건이 없다.
BST는 이진 탐색을 진행하지만, BT는 구조적 단서가 없으므로 모든 경로를 탐색해야 한다.(Post-order DFS)
따라서 BT의 시간 복잡도는 O(N)이다.

- BT의 LCA 찾기 문제: [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Approach
- p, q가 현재 노드보다 작으면, 왼쪽으로 이동
- p, q가 현재 노드보다 크면, 오른쪽으로 이동
- p, q가 현재 노드에서 양쪽으로 분리되어 나간다면, 현재 노드가 LCA이다.

### 재귀와 반복문
재귀는 함수 호출마다 call stack 프레임이 생긴다.(push/pop)
오버헤드가 발생하여 공간 복잡도가 O(H)이다.
인터프리터는 특성상 재귀 성능 호출이 비교적 좋지 않다.
또한 트리가 매우 깊어서 H가 큰 경우, Stack Overflow 발생 가능성이 있다.

## 시간 & 공간 복잡도

```
TC: O(H)
SC: O(1)
```

### TC is O(H):
- 트리의 높이만큼 반복문을 돌리므로, O(H)이다.

### SC is O(1):
- 추가 공간 사용 없음
- 만약 재귀로 풀이한다면, 함수 호출마다 콜스택 공간이 생기므로 O(H)이다.
'''
class Solution:
    '''
    반복문 Top-down
    TC: O(H)
    SC: O(1)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root 
    '''
    재귀 Bottom-up
    TC: O(H)
    SC: O(H)
    '''
    def lowestCommonAncestorBottomUp(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
