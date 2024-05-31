- 문제 : https://leetcode.com/problems/top-k-frequent-elements/
- time complexity : O(nlogn)
- space complexity : O(n)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/04/18/leetcode-347

```java
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> counter = new HashMap<>();

    Arrays.stream(nums)
            .forEach(num -> {
                counter.put(num, counter.getOrDefault(num, 0) + 1);
            });

    return Arrays.copyOfRange(counter.entrySet().stream()
            .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
            .mapToInt(Map.Entry::getKey)
            .toArray(), 0, k);
}
```

## tc, sc 관련 그렇게 생각한 이유

빈도를 기준으로 map을 생성하기 때문에 n 보다 적은 경우가 대다수 이겠지만, 최악의 경우 n개의 map entry가 생성될 수 잇음.
