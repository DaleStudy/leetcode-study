package leetcode_study

/*
* 링크드 리스트에서 순환이 발생하는지 체크하는 문제
* Node `val` 값을 주어진 범위 (-10,000 <= `val` <= 10,000) 보다 큰 정수로 변경해 cycle 판별 시도
* 시간 복잡도: O(n)
* -> linked list node 개수만큼 진행
* 공간 복잡도: O(1)
* -> 주어진 node를 가리키는 currentNode 이외에 추가되는 없음
* */
fun hasCycle(head: ListNode?): Boolean {
    var currentNode = head

    while (currentNode?.next != null) {
        if (currentNode.`val` == 10001) return true // 이미 방문한 노드이면 사이클 존재
        currentNode.`val` = 10001 // 방문한 노드 표시
        currentNode = currentNode.next // 다음 노드로 이동
    }

    return false // `null`을 만났다면 사이클 없음
}
