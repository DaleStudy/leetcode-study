"""TC: O(n^2), SC: O(1)

n은 주어진 리스트의 노드 개수.

아이디어:
아래의 절차를 반복한다.
- 리스트가 주어져있다. 여기에 head가 존재한다. (*로 표시)
    - 1 -> 2 -> 3 -> 4 -> 5
      *
- 리스트의 끝 노드를 떼어낸다.
    - 1 -> 2 -> 3 -> 4    5
      *
- head의 next를 떼어낸 노드로 바꾼다.
    - 1    2 -> 3 -> 4
      *└─> 5
- head의 next의 next를 원래 head의 next였던 노드로 바꾼다.
    - 1    ┌─> 2 -> 3 -> 4
      *└─> 5
- head를 새로 만들어진 head의 next의 next로 바꾼다.
    - 1    ┌─> 2 -> 3 -> 4
       └─> 5   *

코드에서는 위의 아이디어를 cur_head, cur_next, end 같은 변수를 써서 구현했다. 이때 end 노드를
구하기 위한 함수를 따로 구현했는데, 자세한 내용은 코드를 참조하면 된다.

SC:
- 마지막 노드를 가져오는 `pop_end` 함수에서 end, result 변수 관리에 O(1).
- cur_head, cur_next, end 등의 변수 관리에 O(1).
- 종합하면 O(1).

TC:
- 한 번 끝 노드를 떼어서 head에 붙이고 head의 next였던 노드를 끝 노드에 붙이는 시행에 O(1)
- ... 인 것처럼 보이지만 끝 노드를 구하는 데에 head 뒤에 달린 노드 개수 만큼을 순회해야 한다.
- 처음 리스트의 길이가 n에서 시작해서 한 번의 작업 시행에 탐색해야 하는 리스트 길이가 2씩 줄어든다.
- n + (n-2) + ... = O(n^2). 자세한 식 유도는 생략하겠다.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def pop_end(node: Optional[ListNode]) -> Optional[ListNode]:
            end = node
            while end.next and end.next.next:
                # end의 next의 next가 없으면, 즉, end의 next가 리스트의 끝이면 멈춘다.
                # 이름을 end라고 지어놓아서 헷갈릴 수 있는데, 여기서 구하고자 하는 end는
                # 뒤에서 두 번째 노드다...
                end = end.next

            # 찐 마지막 노드를 result에 넣어놓는다.
            result = end.next

            # 찐 마지막 노드를 리스트에서 제거한다. 마지막에서 두 번째 노드의 next를
            # None으로 바꾸면 연결이 끊어짐.
            end.next = None

            # 찐 마지막 노드를 리턴.
            return result

        cur_head = head
        while cur_head and cur_head.next and cur_head.next.next:
            cur_next = cur_head.next
            end = pop_end(cur_head)
            cur_head.next = end
            end.next = cur_next
            cur_head = end.next


"""TC: O(n), SC: O(n)

n은 주어진 리스트의 노드 개수.

아이디어:
- 앞의 아이디어는 다 좋은데 끝 노드를 찾기 위해 리스트 전체를 순회해야 해서 TC가 너무 커진다.
- 리스트 순회를 안 하고 싶으면 리스트에 있는 노드 값을 한 번 순회하면서 죄다 파이썬의 리스트에
  넣어놓고 필요한 값을 꺼내서 결과 리스트를 만들면 되는 것이 아닐까?
- 파이썬 리스트는 주어진 singly-linked list와는 달리 인덱스로 접근이 가능하므로, 투포인터를 써서
  새로 결과 리스트를 만들어서 리턴하자.
  
SC:
- 주어진 singly-linked list를 순회하면서 값을 뽑아서 파이썬 리스트에 넣음. O(n).

TC:
- 투포인터를 써서 모든 아이템에 한 번씩만 접근하여 새로 노드 만듦. O(n).
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        nums = []
        cur_head = head
        while cur_head:
            nums.append(cur_head.val)
            cur_head = cur_head.next

        head.val = nums[0]
        cur_head = head
        ptr = [1, len(nums) - 1]
        i = 1
        while ptr[0] <= ptr[1]:
            cur_head.next = ListNode(nums[ptr[i]])
            cur_head = cur_head.next
            if i == 0:
                ptr[i] += 1
            else:
                ptr[i] -= 1
            i = (i + 1) % 2
