/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {

    /**
     * 방법1: [실패]
     * - 접근법: for문 사용, list1, list2 중 긴 값을 기준으로 for문 최대 값 설정
     * - 실패 이유: LinkedList를 배열처럼 접근하려 했으나, LinkedList는 .next로 순차 접근해야 함
     *   또한 list1.next.length와 같은 속성이 존재하지 않음
     */
    // const getSortedList1 = () => {
    //     const maxLength = Math.max(list1.next.length, list2.next.length) + 1; // 오류: LinkedList에는 length 속성이 없음
    //     const results = [];
    //     const queue = [];

    //     for(let i = 0; i < maxLength; i++) {
    //         if(i === 0) {
    //             if(list1.val < list2.val) {
    //                 results.push(list1.val);
    //                 results.push(list2.val);
    //             } else {
    //                 results.push(list2.val);
    //                 results.push(list1.val);
    //             }
    //         } else {
    //             const currList1Val = list1.next[i - 1]; // 오류: LinkedList는 인덱스로 접근 불가
    //             const currList2Val = list2.next[i - 2]; // 오류: LinkedList는 인덱스로 접근 불가
    //             const resultsLatestVal = results[reulsts.length - 1]; // 오류: 변수명 오타 (reulsts)
    //             if(currList1Val < currList2Val) {
    //                 if(currList1Val < resultsLatestVal) {
                        
    //                 }
    //             }
    //         }
    //     }
    // };

    /**
     * 방법2: [실패]
     * - 접근법: LinkedList를 배열로 변환 후 정렬
     * - 실패 이유: LinkedList를 배열로 변환하는 과정에서 오류 발생
     *   list1.next와 list2.next는 배열이 아닌 ListNode 객체이므로 스프레드 연산자 사용 불가
     *   또한 결과를 배열로 반환하지만 문제는 ListNode를 요구함
     */
    // const getSortedList2 = () => {
    //     const list1Next = list1.next ?? [];
    //     const list2Next = list2.next ?? [];
    //     console.log('debug1::', list1.val, list2.val, list1Next, list2Next)
    //     const result: number[] = [list1.val, list2.val, ...list1Next, ...list2Next]; // 오류: ListNode 객체는 스프레드 연산자로 펼칠 수 없음

    //     console.log('debug::', result)

    //     return list1; // 오류: 정렬된 결과가 아닌 원본 list1을 반환
    // };

    /**
     * 방법3: [실패]
     * - 접근법: for 문으로 next 없을 때까지 체크해서 배열에 추가한 다음 정렬 후 반환
     * - 실패 이유: 배열에 값을 모으기만 하고 정렬 및 ListNode 생성 로직이 누락됨
     *   또한 for 루프 조건이 잘못됨 (!!isEnd는 항상 false로 루프가 실행되지 않음)
     *   마지막에 return 문이 불완전함
     */
    // const getSortedList3 = () => {
    //     const result = [list1.val, list2.val];
    //     let currList1 = list1.next;
    //     let currList2 = list2.next;

    //     let isEnd = false;
    //     for (let i = 0; !!isEnd; i++) { // 오류: !!isEnd는 항상 false (isEnd가 false로 초기화됨)
    //         if(currList1?.val) {
    //             result.push(currList1.val); 
    //         }
    //         if(currList2?.val) {
    //             result.push(currList2.val);
    //         }

    //         if(currList1?.next) {
    //             currList1 = currList1.next;
    //         } else if (currList2?.next) {
    //             currList2 = currList2.next;
    //         } else {
    //             break;
    //         }
    //     }

    //     return // 오류: 반환값이 없음
    // };

    /**
     * 방법4: [실패]
     * - 접근법: ListNode 인스턴스로 결과 생성, head를 만들고 순차적으로 값 추가
     * - 실패 이유: 구현이 완료되지 않음, 아이디어만 주석으로 남겨둠
     */

    /**
     * 방법5: 
     * - 접근법: 새 ListNode 인스턴스를 생성하여 두 리스트의 값을 순차적으로 비교하며 병합
     * - 시간 복잡도: O(n + m)
     * - 공간 복잡도: O(n + m)
     */
    const getSortedList5 = () => {
        const dummy = new ListNode();
        let current = dummy;

        while (list1 && list2) {
            if (list1.val < list2.val) {
                current.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                current.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            current = current.next;
        }

        while (!!list1) {
            current.next = new ListNode(list1.val);
            list1 = list1?.next;
            current = current.next
        }

        while (!!list2) {
            current.next = new ListNode(list2.val);
            list2 = list2?.next;
            current = current.next
        }

        return dummy.next;
    };

    /**
     * 방법6: with GPT
     * - 접근법: 방법5의 최적화 버전으로, 새 노드를 생성하지 않고 기존 노드를 재사용
     * - 시간 복잡도: O(n + m)
     * - 공간 복잡도: O(1)
     */
    const getSortedList6 = () => {
        const dummy = new ListNode();
        let current = dummy;
    
        while (list1 && list2) {
            if (list1.val < list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
    
        current.next = list1 ?? list2;
    
        return dummy.next;
    };

    // return getSortedList1();
    // return getSortedList2();
    // return getSortedList3();
    // return getSortedList5();
    return getSortedList6();
    
};