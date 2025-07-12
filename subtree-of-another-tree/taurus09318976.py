"""
문제의 본질: "큰 트리 안에 작은 트리와 똑같은 부분이 있나?"

해결 아이디어:
1. 큰 트리의 모든 위치를 하나씩 확인해보기
2. 각 위치에서 "여기서 시작하는 서브트리가 찾는 트리와 완전히 같은가?" 확인하기

해결 방법:
1. 큰 트리의 모든 노드를 순회
2. 각 노드에서 시작하는 서브트리가 찾는 트리와 같은지 확인
3. 같은 트리인지 확인하는 것은 별도 함수로 분리

헤결에 필요한 두 개의 함수:
1. isSubtree 함수 (메인 로직): "어디서 찾을 수 있나?" (탐색 담당)
   - root가 None이면 False 반환 (빈 트리에선 찾을 수 없음)
   - 현재 위치에서 완전히 같은 트리인지 확인
   - 같지 않다면 왼쪽, 오른쪽 자식에서 재귀적으로 찾기

2. isSameTree 함수 (보조 로직): "여기서 완전히 같나?" (비교 담당)
   - 두 트리가 완전히 같은지 확인
   - 구조와 값이 모두 같아야 함
   - 재귀적으로 모든 노드 비교

왜 이렇게 풀까?
- 서브트리는 어느 노드에서든 시작할 수 있음
- 따라서 모든 가능한 시작점을 확인해야 함
- 각 시작점에서 완전히 같은 트리인지 확인하면 됨

기억하기 쉬운 방법:
1. "모든 노드에서 시도해보기" (isSubtree)
2. "완전히 같은지 확인하기" (isSameTree)
이 두 가지 기능을 분리해서 생각하기!

시간복잡도: O(m × n)
- m: root 트리의 노드 개수
- n: subRoot 트리의 노드 개수
- 최악의 경우 root의 모든 노드에서 subRoot와 비교

공간복잡도: O(max(m, n))
- 재귀 호출 스택의 깊이는 트리의 높이와 같음
- 균형 트리라면 O(log n), 편향 트리라면 O(n)
"""


# 1. 먼저 TreeNode 클래스 정의 (이진 트리의 노드를 나타냄)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 노드의 값
        self.left = left    # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드


class Solution:
    # 2. 메인 함수: root 트리에서 subRoot와 같은 서브트리가 있는지 확인
    def isSubtree(self, root, subRoot):
        
        # 기본 케이스 1: 큰 트리가 비어있으면 서브트리를 찾을 수 없음
        if not root:
            return False
        
        # 기본 케이스 2: 현재 노드에서 서브트리와 완전히 일치하는지 확인
        if self.isSameTree(root, subRoot):
            return True
        
        # 재귀 케이스: 왼쪽 서브트리 또는 오른쪽 서브트리에서 찾기
        # 왼쪽 서브트리에서 찾거나 OR 오른쪽 서브트리에서 찾으면 True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    
    # 3. 보조 함수: 두 트리가 완전히 같은지 확인 (구조와 값 모두)
    def isSameTree(self, tree1, tree2):
        
        # 기본 케이스 1: 둘 다 비어있으면 같음
        if not tree1 and not tree2:
            return True
        
        # 기본 케이스 2: 하나만 비어있으면 다름
        if not tree1 or not tree2:
            return False
        
        # 기본 케이스 3: 현재 노드의 값이 다르면 다름
        if tree1.val != tree2.val:
            return False
        
        # 재귀 케이스: 왼쪽 서브트리와 오른쪽 서브트리가 모두 같아야 함
        # 왼쪽끼리 같고 AND 오른쪽끼리 같아야 전체가 같음
        return (self.isSameTree(tree1.left, tree2.left) and 
                self.isSameTree(tree1.right, tree2.right))

