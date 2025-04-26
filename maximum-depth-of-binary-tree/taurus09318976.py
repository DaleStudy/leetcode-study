# 이진 트리의 노드를 정의하는 클래스
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 노드의 값
        self.left = left # 왼쪽 자식 노드
        self.right = right # 오른쪽 자식 노드


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 초기 조건 확인. 트리가 비어 있는 경우 깊이는 0
        if not root:
            return 0
        
        # 큐에 루트 노드를 추가, 깊이를 0으로 초기화
        queue = [root]
        depth = 0
        
        # 너비우선 탐색(BFS) 실행. 큐가 비어있지 않은 동안 반복
        while queue:
            # 새로운 레벨 시작될 때마다 깊이 증가
            depth += 1
            # 현재 레벨의 노드 수 저장
            level_size = len(queue)
            
            # 현재 레벨의 모든 노드를 순차적으로 처리
            for _ in range(level_size):
                # 큐에서 노드 하나 꺼내기
                node = queue.pop(0)
                
                # 자식 노드 처리. 다음 레벨의 노드들이 됨
                ## 왼쪽 자식이 있으면 큐에 추가
                if node.left:
                    queue.append(node.left)
                ## 오른쪽 자식이 있으면 큐에 추가
                if node.right:
                    queue.append(node.right)
    
        # 최종 깊이 반환
        return depth

    #시간 복잡도 (Time Complexity): O(n)
        #n: 트리의 총 노드 수
        #이유:
            #각 노드를 정확히 한 번씩만 방문
            #각 노드에서의 연산(추가, 제거)은 상수 시간
            #따라서 전체 시간 복잡도는 O(n)
    #공간 복잡도 (Space Complexity): O(n)
        #최악의 경우: O(n)
        #평균적인 경우: O(n/2) ≈ O(n)
        #이유:
            #큐에 저장되는 최대 노드 수는 트리의 최대 너비
            #완전 이진 트리의 경우 마지막 레벨에 약 n/2개의 노드가 있을 수 있음
            #따라서 공간 복잡도는 O(n)
