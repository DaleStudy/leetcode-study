- https://leetcode.com/problems/group-anagrams/
- time complexity : O(n \* m log m), 여기서 m은 str 배열(strs)의 각 str의 평균이다.
- space complexity : O(n \* m)
- https://algorithm.jonghoonpark.com/2024/05/25/leetcode-49

```java
public List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> result = new ArrayList<>();
    HashMap<String, Integer> map = new HashMap<>();

    for(String str: strs) {
        char[] temp = str.toCharArray();
        Arrays.sort(temp);
        String sorted = String.valueOf(temp);
        if(map.containsKey(sorted)) {
            result.get(map.get(sorted)).add(str);
        } else {
            int newIndex = result.size();
            List<String> newArrayList = new ArrayList<>();
            result.add(newArrayList);
            newArrayList.add(str);
            map.put(sorted, newIndex);
        }
    }

    return result;
}
```

## TC, SC

시간 복잡도는 O(n \* m log m)이고, 공간 복잡도는 O(n \* m)이다.
여기서 m은 str 배열(strs)의 각 str의 평균이다.
