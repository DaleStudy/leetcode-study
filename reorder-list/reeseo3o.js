// Time Complexity: O(n)
// Space Complexity: O(1)

const reorderList = (head) => {
    if (!head || !head.next || !head.next.next) return;
  
    // 1. 가운데 찾기 (slow는 앞쪽 리스트의 끝)
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
  
    // 2. 뒷부분 뒤집기 (slow.next ~ 끝)
    let prev = null;
    let curr = slow.next;
    slow.next = null; // 앞부분과 뒷부분 분리
  
    while (curr) {
      const next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    // prev: 뒤집힌 두 번째 리스트의 head
  
    // 3. 교차 머지 (head: 첫 번째, prev: 두 번째)
    let first = head;
    let second = prev;
  
    while (second) {
      const nextFirst = first.next;
      const nextSecond = second.next;
  
      first.next = second;
      second.next = nextFirst;
  
      first = nextFirst;
      second = nextSecond;
    }
  };
