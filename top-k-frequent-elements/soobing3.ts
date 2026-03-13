class MyMinPriorityQueue<T> {
  private heap: T[] = [];
  private compare: (a: T, b: T) => number;

  constructor(compare: (a: T, b: T) => number) {
    this.compare = compare;
  }

  public get size() {
    return this.heap.length;
  }

  public get peek() {
    return this.heap[0];
  }

  public toArray() {
    return this.heap;
  }

  public push(value: T) {
    this.heap.push(value);
    this.bubbleUp();
  }

  public pop() {
    if(this.heap.length === 0) {
        return undefined;
    }

    const min = this.heap[0];
    const last = this.heap.pop();
    if(this.heap.length === 0) {
        return min;
    }

    this.heap[0] = last ?? undefined as T;
    this.bubbleDown();

    return min;
  }

  private bubbleDown() {
    let index = 0;

    while(true) {
        let smallestIndex = index;
        let leftIndex = 2 * index + 1;
        let rightIndex = 2 * index + 2;

        if(leftIndex < this.size && this.compare(this.heap[leftIndex], this.heap[smallestIndex]) < 0) {
            smallestIndex = leftIndex;
        }

        if(rightIndex < this.size && this.compare(this.heap[rightIndex], this.heap[smallestIndex]) < 0) {
            smallestIndex = rightIndex;
        }

        if(index === smallestIndex) break;
        [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex],  this.heap[index]];
        index = smallestIndex;
    }
  }

  private bubbleUp() {
    let index = this.size - 1;
    
    while(index > 0) {
        const parentIndex = Math.floor((index - 1) / 2)
        if (this.compare(this.heap[parentIndex], this.heap[index]) > 0) {
            [this.heap[parentIndex], this.heap[index]] = [this.heap[index],  this.heap[parentIndex]]
        }

        index = parentIndex;
    }
  }
}

function topKFrequent(nums: number[], k: number): number[] {
    const map = new Map<number, number>();
    
    for (const n of nums) {
        map.set(n, (map.get(n) ?? 0) + 1);
    }

    const minHeap = new MyMinPriorityQueue((a: number, b: number) => {
         return (map.get(a) ?? 0) - (map.get(b) ?? 0)
    });

    for(const [key, count] of map) {
        if(minHeap.size < k) {
            minHeap.push(key)
        } else if((map.get(minHeap.peek) ?? 0) < (map.get(key) ?? 0)) {
            minHeap.pop()
            minHeap.push(key)
        }
    }
    return minHeap.toArray()
}
