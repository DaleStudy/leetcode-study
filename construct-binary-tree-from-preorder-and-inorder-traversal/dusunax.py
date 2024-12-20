# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    A. 재귀 풀이
    preorder와 inorder의 각각의 범위를 조정하여 트리를 생성
    '''
    def buildTreeA(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def setTree(pre_left, pre_right, in_left, in_right):
            # 재귀 종료 조건: preorder 범위가 유효하지 않은 경우
            if pre_left > pre_right:
                return None

            val = preorder[pre_left]  # preorder의 현재 루트 노드 값 가져오기
            mid = TreeNode(val)  # 루트 노드를 먼저 생성

            mid_inorder = inorder_idx_map[val]  # 루트 노드의 inorder 인덱스 가져오기
            left_size = mid_inorder - in_left  # 왼쪽 서브트리의 크기 계산

            # 왼쪽 서브트리 생성: preorder와 inorder의 범위를 왼쪽 서브트리로 조정
            mid.left = setTree(
                pre_left + 1, pre_left + left_size, in_left, mid_inorder - 1
            )

            # 오른쪽 서브트리 생성: preorder와 inorder의 범위를 오른쪽 서브트리로 조정
            mid.right = setTree(
                pre_left + left_size + 1, pre_right, mid_inorder + 1, in_right
            )

            return mid # 현재 노드 반환

        # inorder를 값 -> 인덱스 맵핑한 딕셔너리 생성 (O(n))
        inorder_idx_map = {value: idx for idx, value in enumerate(inorder)}

        # 트리 생성 시작 (preorder와 inorder 전체 범위 사용)
        return setTree(0, len(preorder) - 1, 0, len(inorder) - 1)
        

    '''
    # B. 재귀 풀이 + 공간 최적화
    # 레퍼런스 링크의 풀이 2: https://www.algodale.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    # 특징: 순회 시마다 인덱스를 찾는 과정이 있음
    '''
    def buildTreeB(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre: 현재 preorder에서 확인할 인덱스
        # start, end: inorder에서 사용할 시작/종료 범위
        def setTree(pre, start, end):
            # 재귀 종료 조건: 범위가 잘못되었거나 트리를 더 이상 만들 필요가 없는 경우
            if not (pre < len(preorder) and start <= end): # preorder에서 확인할 인덱스가 범위에서 나감, 투 포인터가 만남
                return None
            
            val = preorder[pre] # 현재 노드의 값
            root = inorder.index(val) # 트리/서브트리의 루트 노드 인덱스 찾기 - SC: O(n)
            
            left = setTree(pre + 1, start, root - 1) 
            # inorder에서 root노드의 왼쪽은 왼쪽 서브트리
            # pre의 변화: 왼쪽 서브트리의 루트 노드를 찾기 위해 +1 이동

            right = setTree(pre + 1 + root - start, root + 1, end)
            # inorder에서 root노드의 오른쪽은 오른쪽 서브트리
            # pre의 변화: 오른쪽 서브트리의 루트 노드를 찾기 위해 +1 이동 + (root - start) 👈 왼쪽 서브트리의 크기 만큼 더 이동

            return TreeNode(preorder[pre], left, right) # 트리 노드 생성
        
        # preorder 최초 인덱스 = 루트 노드(0), inorder의 처음(0)과 끝(len(inorder) - 1) 인덱스
        return setTree(0, 0, len(inorder) - 1) 

    '''
    C. 재귀 풀이 + 시간 최적화
    레퍼런스 링크의 풀이 3: https://www.algodale.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    특징: A에서 preorder를 찾는 O(n) 과정을 해시 테이블을 사용하여 O(1)로 최적화
    '''
    def buildTreeC(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # enumerate: 인덱스와 값을 동시에 반환
        # inorder를 val -> idx로 매핑한 딕셔너리 생성
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)} 
        # preorder를 순회하기 위한 iterator 객체 생성
        pre_iter = iter(preorder) 

        def setTree(start, end):
            if start > end: # 재귀 종료 조건: 범위가 잘못되었거나 트리를 더 이상 만들 필요가 없는 경우
                return None

            root_val = next(pre_iter) # 현재 노드의 값, 매 순회마다 다음 preorder 노드(root)의 값을 가져옴
            root = inorder_index_map[root_val] # 트리/서브트리의 루트 노드 인덱스를 O(1) 시간으로 찾기

            left = setTree(start, root - 1) # 왼쪽 서브트리
            right = setTree(root + 1, end) # 오른쪽 서브트리
            return TreeNode(root_val, left, right) # 트리 노드 생성
        
        return setTree(0, len(inorder) - 1) # inorder의 처음(0)과 끝(len(inorder) - 1) 인덱스
