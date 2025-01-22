﻿﻿        #해석
        # 매개변수 head (ListNode 클래스의 인스턴스)에서 값을 추출하여 temp 리스트에 저장한다.
        # temp 리스트를 역순으로 정렬(reverse)하여 연결 리스트를 뒤집는다.
        # temp 리스트의 각 값을 ListNode 클래스를 사용해 새 연결 리스트(myNode)를 생성하며 순서대로 추가한다.
        # 최종적으로 myNode의 next를 반환한다(이것은 새 연결 리스트의 시작점을 가리킨다).


        #Big O
        #- N: 입력 연결 리스트(head)의 노드 갯수

        #Time Complexity: O(N) 
        #- while head: 연결 리스트의 모든 노드를 순회하며 val을 temp에 저장하므로 O(N).
        #- for value in temp: temp 리스트의 모든 값을 순회하며 새로운 노드를 생성하므로 O(N).

        #Space Complexity: O(N)
        #- temp : 연결 리스트의 모든 val을 저장하므로 O(N).
        #- myNode 인스턴스: for loop 동안 current.next에 ListNode 인스턴스를 생성한다. 이 작업은 O(1) 작업이 N번 반복되므로 O(N).


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp =[]
        while head:
            temp.append(head.val)
            head = head.next

        temp = temp[::-1] #Reverse the temp list 
        
        myNode = ListNode() #Create the Listnode instance 
        current = myNode #Update current to myNode for Initialize
        
        for value in temp:
            current.next = ListNode(value) ## Create new ListNode Instance and assign it to current.next , 
            current = current.next #Move to the current.next(new Instance base on ListNode )
        
        return myNode.next ## Return the head of the newly created linked list



