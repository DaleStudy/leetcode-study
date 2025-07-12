"""
문제의도: 이 문제는 트리 순회의 특성을 이해하고 재귀적 분할정복을 연습하는 문제임.
-> preorder로 루트 찾고, inorder로 좌우 나누고, 재귀로 반복
- 전위 순회(preorder): 루트 -> 왼쪽 -> 오른쪽
- 중위 순회(inorder): 왼쪽 -> 루트 -> 오른쪽

해결 방법:
1. preorder의 첫 번째 원소가 현재 트리의 루트임을 이용
2. inorder에서 루트의 위치를 찾아 왼쪽/오른쪽 서브트리 분할
3. preorder에서도 대응하는 부분을 분할
4. 왼쪽/오른쪽 서브트리에 대해 재귀적으로 같은 과정 반복
-> - 루트를 알면 inorder에서 왼쪽/오른쪽을 구분할 수 있음!

시간복잡도: O(n²)
- index() 메서드: 배열에서 값을 찾기 위해 최악의 경우 전체 배열을 순회 → O(n)
- 재귀 호출 횟수: 모든 노드에 대해 한 번씩 호출 → n번
- 전체 시간복잡도: n번의 호출 × 각 호출마다 O(n) = O(n²)

공간복잡도: O(n)
- 재귀 호출 스택의 깊이: O(n) (편향 트리일 때)
- 새로 생성하는 배열들: O(n)

예시 설명 :
예시1의 경우

1단계: preorder의 첫 번째는 항상 루트
[3, 9, 20, 15, 7] → 3이 루트

2단계: inorder에서 루트 위치로 좌우 분할
[9, 3, 15, 20, 7] → 3 기준으로 [9] | [15, 20, 7]
- 왼쪽: [9] (인덱스 0까지)
- 오른쪽: [15, 20, 7] (인덱스 2부터)

3단계: 왼쪽 서브트리 크기로 preorder 분할  
왼쪽 크기가 1이면 preorder에서도 1개만 가져옴
- 루트 제외: [9, 20, 15, 7]
- 왼쪽 크기(1)만큼: [9]
- 나머지: [20, 15, 7]

4단계: 재귀적으로 같은 과정 반복
- 왼쪽: buildTree([9], [9]) → 노드 9
- 오른쪽: buildTree([20, 15, 7], [15, 20, 7]) → 서브트리

최종 결과:
      3
     / \
    9   20
       /  \
      15   7


주의사항:
- 배열 슬라이싱 범위 조심하기
- 빈 배열일 때 None 반환하기
- inorder에서 루트 위치 정확히 찾기

"""


class Solution:
    def buildTree(self, preorder, inorder):
        # 1. 기본 케이스: 빈 배열이면 None 반환
        if not preorder or not inorder:
            return None
        
        # 2. preorder의 첫 번째가 루트
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 3. inorder에서 루트 위치 찾기
        root_index = inorder.index(root_val)
        
        # 4. inorder를 루트 기준으로 분할
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        
        # 5. preorder도 해당 크기만큼 분할
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        
        # 6. 재귀적으로 왼쪽과 오른쪽 서브트리 구성
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root



        