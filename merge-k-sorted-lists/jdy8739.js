/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    const arr = [];

    for (let i = 0; i < lists.length; i++) {
        let list = lists[i];

        while (list) {
            arr.push(list.val);
            list = list.next;
        }
    }

    if (!arr.length) {
        return null;
    }

    arr.sort((a, b) => a - b);

    const first = new ListNode(arr[0]);

    let node = first;

    for (let j = 1; j < arr.length; j++) {
        const next = new ListNode(arr[j]);
        node.next = next;
        node = next;
    }

    return first;
};

// 시간복잡도 -> for문 이후 sort 이후 for문을 수행하며 이는 O(n) + O(nlogn) + O(n)이므로 O(nlogn)가 시간복잡도가 된다
// 공간복잡도 -> lists의 노드 수 만큼 길이가 결정되므로 0(n) 
