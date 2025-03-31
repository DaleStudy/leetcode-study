package leetcode_study

/*
* singly linked list를 재정렬하는 문제
* 시간 복잡도: O(n)
* -> 전체 노드를 저장하기 위해 순환하는 과정 O(n)
* -> 리스트의 앞과 뒤에 포인터를 두고 주소값을 변경하는 과정 O(log n)
* 공간 복잡도: O(n)
* -> 노드 전체를 담을 새로운 list 필요 O(n)
* */
fun reorderList(head: ListNode?): Unit {
    val tempNodeList = mutableListOf<ListNode>()
    var currentNode = head

    while (currentNode != null) {
        tempNodeList.add(currentNode)
        currentNode = currentNode.next
    }

    // 양쪽 끝에서부터 교차로 연결
    var i = 0
    var j = tempNodeList.size - 1
    while (i < j) {
        // 먼저 앞쪽 노드의 next가 뒤쪽 노드를 가리키게 함
        tempNodeList[i].next = tempNodeList[j]
        i++  // 다음 앞쪽 노드 선택

        // 만약 앞쪽과 뒤쪽이 만난 경우 (짝수개일 때), 반복 종료
        if (i == j) break

        // 뒤쪽 노드의 next가 새로운 앞쪽 노드를 가리키게 함
        tempNodeList[j].next = tempNodeList[i]
        j--  // 다음 뒤쪽 노드 선택
    }
    tempNodeList[i].next = null
}
