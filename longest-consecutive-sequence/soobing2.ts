/**
 * 문제 유형: 그래프(Union Find)
 *
 * 문제 설명
 * - 주어진 배열에서 가장 긴 연속된 수열의 길이를 구하는 문제
 *
 * 아이디어
 * 1) 중복된 수 제거 후 순회하며 값이 1차이 나는 항목끼리 합집합 만들기
 *
 * 미션
 * - 더 빠른 풀이: HashSet 기반 Greedy로 풀어보기.
 *
 */
class UnionFind {
  parent: Map<number, number> = new Map();
  size: Map<number, number> = new Map();

  constructor(nums: number[]) {
    for (const num of nums) {
      this.parent.set(num, num);
      this.size.set(num, 1);
    }
  }

  find(x: number): number {
    if (this.parent.get(x) !== x) {
      this.parent.set(x, this.find(this.parent.get(x)!));
    }

    return this.parent.get(x)!;
  }

  union(x: number, y: number): void {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX === rootY) return;

    const sizeX = this.size.get(rootX);
    const sizeY = this.size.get(rootY);
    if (sizeX < sizeY) {
      this.parent.set(rootX, rootY);
      this.size.set(rootY, sizeX + sizeY);
    } else {
      this.parent.set(rootY, rootX);
      this.size.set(rootX, sizeX + sizeY);
    }
  }

  getMaxSize(): number {
    let max = 0;
    for (const size of this.size.values()) {
      max = Math.max(max, size);
    }
    return max;
  }
}
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;

  const uniqueNums = Array.from(new Set(nums));
  const uf = new UnionFind(uniqueNums);

  for (const num of uniqueNums) {
    if (uf.parent.has(num + 1)) {
      uf.union(num, num + 1);
    }
  }

  return uf.getMaxSize();
}
