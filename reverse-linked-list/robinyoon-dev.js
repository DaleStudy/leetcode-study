/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {

    /**정리
     ListNode { 
        val: number;
        next: ListNode | null; //
    }
    */

    /**
     설명에 나와 있는 head=[1, 2, 3, 4, 5]는 실제로 다음과 같음.
        const head =
            new ListNode(
                1,
                new ListNode(
                2,
                new ListNode(
                    3,
                    new ListNode(
                    4,
                    new ListNode(5, null)
                    )
                )
                )
            );
     */

    /**
     계획
     1. ListNode -> Array로 바꾸는 함수 생성
     2. const headArray는 head를 Array로 바꾼 값
     3. const reversedArray는 headArray를 reverse한 배열
     4. const result는 reversedArray를 ListNode로 바꾼 값
     5. return result
     */

    // ListNode를 Array로 바꿔주는 함수
    const getToArray = (listNode) => {
        const tempArray = [];
        let cur = listNode; // 객체 참조 복사! 

        while (cur !== null) {
            tempArray.push(cur.val);
            cur = cur.next;
        }
        return tempArray;
    }

    const getReversedArray = (arr) => {

        const reversedArray = [...arr].reverse();

        return reversedArray;
    }

    const getToListNode = (arr) => {
        const dummy = new ListNode(undefined, undefined);
        let tail = dummy; // 객체 참조 복사! 즉, dummy가 가리키는 객체를 tail도 가리키게 (참조 복사) 됨!

        for (const item of arr) {
            tail.next = new ListNode(item, null);
            tail = tail.next;
        }

        return dummy.next;
    }

    const headArray = getToArray(head);
    const reversedArray = getReversedArray(headArray);
    const result = getToListNode(reversedArray);

    return result;

};
