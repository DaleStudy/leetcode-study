class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode answer = new ListNode();
        ListNode mergePointer = answer;
        // 머지를 수행할 포인터와 정답을 반환할 포인터 총 2개의 포인터가 필요합니다.
        // 초기화에서 정답 포인터와 머지 포인터가 같은 노드 주소를 바라보게 해야 합니다.
        // 머지 포인터가 연산을 계속하더라도 정답 포인터의 next는 정렬된 첫번째 노드를 가리킬 것입니다.
        // 머지 포인터는 연산을 계속하면서 참조 주소가 변경되기 때문에 그 자체로 반환하면 안됩니다.

        while (list1 != null && list2 != null) {
            // list1의 값이 list2의 값보다 작거나 같으면 list1의 노드를 병합
            if (list1.val <= list2.val) { // wrong: 값이 더 작거나, 또는 값이 동일할 경우 list1을 우선시해야 합니다.
                mergePointer.next = list1;
                list1 = list1.next;
            } else {
                // 그렇지 않으면 list2의 노드를 병합
                mergePointer.next = list2;
                list2 = list2.next;
            }
            mergePointer = mergePointer.next;
        }

        // 두 리스트는 오름차순 정렬을 전제로 하기 때문에 한 리스트의 길이 끝에 도달하면 나머지는 그저 통 붙여넣기를 합니다.
        // 두 리스트 중에서 null이 아닌 리스트 노드로 머지 포인터의 next에 연결합니다.
        if (list1 != null) {
            mergePointer.next = list1;
        } else {
            mergePointer.next = list2;
        }
        return answer.next;
    }
}
