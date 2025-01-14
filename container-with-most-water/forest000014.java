/*
solution 1. brute force
Time Complexity: O(n^2)
Space Complexity: O(1)
모든 선분 i에 대해, 가장 많은 물을 담을 수 있는 반대쪽 선분 j를 찾는다.


solution 2. PQ
Time Complexity: O(nlogn)
- 정렬 : O(nlogn)
- i번째 선분에 대해 (자신보다 크거나 같은) 가장 멀리있는 선분 탐색(O(logn)) * n = O(nlogn)
Space Complexity: O(n)

(사고의 흐름을 적기 위해 편의상 반말로 적었습니다... ^^)
brute force 에서 불필요한 탐색을 줄여보자.
일단 어떤 선분 i가 주어졌다고 가정하자. i를 한쪽 벽으로 해서 가장 많은 물을 담는 방법을 찾으려면, 반드시 나머지 모든 선분을 탐색해야만 할까?

(1) 자신보다 작은 선분은 탐색하지 않는다.

자신보다 큰 선분만을 탐색해도 충분하다.
왜냐하면, 설령 자신보다 더 작은 선분 중에 정답이 있었다고 하더라도, 그 선분을 기준으로 탐색할 때 정답에 해당하는 쌍을 확인하게 될 것이기 때문이다.

(2) 자신보다 크거나 같은 선분만을 탐색 대상으로 삼는다면, 가장 멀리있는 선분만 확인하면 된다.

탐색 대상이 자신보다 크거나 같은 선분들이라면, 어차피 담을 수 있는 물의 높이는 자신의 높이로 일정하다.
따라서, 멀리있는 선분일수록 더 많은 물을 담게 된다.
즉, "자신보다 크거나 같으면서", "가장 멀리 있는(오른쪽이든 왼쪽이든)" 선분만을 후보로 삼아 확인하면 충분하다.
(그 외의 나머지, 즉 자신보다 크거나 같으면서, 가장 멀리있지 않은 나머지 선분들은, 자연스럽게 탐색하지 않을 수 있다.)

정리하자면, 주어진 선분 i에 대해서, 단 2번(오른쪽, 왼쪽)의 탐색만 하면 충분하다.

(3) 내림차순 정렬과 2개의 PQ를 아래처럼 활용하면, 위 탐색을 O(logn) 시간에 수행할 수 있다.
PQ는 각각 x 좌표 기준 max heap(가장 오른쪽의 선분을 찾기 위함), x 좌표 기준 min heap(가장 왼쪽의 선분을 찾기 위함)을 사용한다.
선분들을 길이 내림차순으로 정렬해놓고, 하나씩 순회하면서 (say, i번째 선분), 아래 과정을 반복한다.
- 자신보다 크거나 같으면서 가장 오른쪽으로 멀리 있는 선분의 위치를 찾아서(= 현재 PQ(max heap)의 root), 최대 물의 양을 계산한다.
- 자신보다 크거나 같으면서 가장 왼쪽으로 멀리 있는 선분의 위치를 찾아서(= 현재 PQ(min heap)의 root), 최대 물의 양을 계산한다.
- i번째 선분을 PQ 2개에 각각 넣는다.


solution 3. two pointers
(AlgoDale 풀이를 참고함)

Time Complexity: O(n)
Space Complexity: O(1)

2 포인터를 활용하면, PQ도 없이 시간 복잡도를 O(n)으로 줄일 수 있었다.
단순히 "큰 쪽을 줄이기보다는, 작은 쪽을 줄이는 게 유리하겠지" 정도의 greedy한 논리는 충분하지 않은 것 같고, 더 명확한 근거가 있을 것 같은데 시간 관계상 고민해보지는 못했다.

To-Do : 풀이가 대강 이해는 되었지만, 이게 왜 되는지, 엄밀하게 이해하기 위해 PQ를 사용했던 논리를 좀 더 발전시켜볼 필요가 있다.

*/
class Solution {
    public int maxArea(int[] height) {
        int i = 0, j = height.length - 1;

        int ans = 0;
        while (i < j) {
            int area = (j - i) * Math.min(height[i], height[j]);
            if (area > ans) {
                ans = area;
            }

            if (height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
        }

        return ans;
    }

    ////// 아래는 solution 2
    private static class Tuple {
        private int x;
        private int h;

        Tuple(int x, int h) {
            this.x = x;
            this.h = h;
        }
    }

    public int maxArea2(int[] height) {
        List<Tuple> tuples = IntStream.range(0, height.length)
                .mapToObj(i -> new Tuple(i, height[i]))
                .collect(Collectors.toList());
        Collections.sort(tuples, (a, b) -> b.h - a.h);

        PriorityQueue<Tuple> minPq = new PriorityQueue<>((a, b) -> a.x - b.x);
        PriorityQueue<Tuple> maxPq = new PriorityQueue<>((a, b) -> b.x - a.x);

        int ans = 0;
        for (int i = 0; i < height.length; i++) {
            minPq.add(tuples.get(i));
            maxPq.add(tuples.get(i));

            Tuple curr = tuples.get(i);

            Tuple left = minPq.peek();
            int leftArea = (curr.x - left.x) * curr.h;
            if (leftArea > ans) {
                ans = leftArea;
            }

            Tuple right = maxPq.peek();
            int rightArea = (right.x - curr.x) * curr.h;
            if (rightArea > ans) {
                ans = rightArea;
            }
        }

        return ans;
    }
}
