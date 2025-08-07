/**
 * 문제 유형: Heap
 *
 * 문제 설명
 * - 가장 빈도수가 많은 K개 Element 추출
 *
 * 아이디어
 * 1) 빈도수 계산하여 index와 함께 Map에 저장, 빈도수를 기준으로 MinHeap 구성
 * 2) 빈도수 Map을 순회하면서 MinHeap에 추가 + MinHeap의 크기가 K를 초과하면 최소값 제거 (미리미리 빈도수가 많은 K개 Element를 만들어나가는 형식)
 * 3) MinHeap에 남아있는 Element들의 index를 반환
 *
 * 시간 복잡도: O(NlogK)
 * 공간 복잡도: O(N)
 */
class MinHeap {
  heap: [number, number][] = [];

  insert(item: [number, number]) {
    this.heap.push(item);
    this.bubbleUp();
  }

  private bubbleUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[index][0] >= this.heap[parentIndex][0]) break;
      [this.heap[index], this.heap[parentIndex]] = [
        this.heap[parentIndex],
        this.heap[index],
      ];
      index = parentIndex;
    }
  }

  extractMin(): [number, number] | undefined {
    if (this.heap.length === 0) return undefined;
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0 && end !== undefined) {
      this.heap[0] = end;
      this.sinkDown(0);
    }
    return min;
  }

  private sinkDown(index: number) {
    const length = this.heap.length;
    while (true) {
      let left = 2 * index + 1;
      let right = 2 * index + 2;
      let smallest = index;

      if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
        smallest = left;
      }
      if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
        smallest = right;
      }
      if (index === smallest) break;

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }

  peek(): [number, number] | undefined {
    return this.heap[0];
  }

  size(): number {
    return this.heap.length;
  }
}
function topKFrequent(nums: number[], k: number): number[] {
  const freqMap = new Map<number, number>();
  for (const num of nums) {
    freqMap.set(num, (freqMap.get(num) ?? 0) + 1);
  }

  const minHeap = new MinHeap();
  for (const [num, count] of freqMap.entries()) {
    minHeap.insert([count, num]);
    if (minHeap.size() > k) {
      minHeap.extractMin();
    }
  }

  return minHeap.heap.map(([_, num]) => num);
}
