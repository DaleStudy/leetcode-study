/**
[문제풀이]
- 이전에 배열로 풀었던 아나그램 솔루션을 참고해보자.
time: O(N^2 * M), space: O(N * M)
    class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
            List<List<String>> result = new ArrayList<>();
            boolean[] used = new boolean[strs.length];

            for (int i = 0; i < strs.length; i++) {
                if (used[i]) {
                    continue;
                }

                List<String> sub = new ArrayList<>();
                String current = strs[i];
                sub.add(current);
                used[i] = true;

                for (int j = i + 1; j < strs.length; j++) {
                    String next = strs[j];
                    if (isAnagram(current, next)) {
                        sub.add(next);
                        used[j] = true;
                    }
                }
                result.add(sub);
            }
            return result;
        }

        private boolean isAnagram(String current, String next) {
            if (current.length() != next.length()) {
                return false;
            }

            int[] counting = new int[26];
            for (char ch : current.toCharArray()) {
                counting[ch - 'a']++;
            }
            for (char ch : next.toCharArray()) {
                counting[ch - 'a']--;
            }

            for (int count : counting) {
                if (count != 0) {
                    return false;
                }
            }
            return true;
        }
    }

- sorting
time: O(N * M log M), space: O(N * M)

[회고]
중첩 for문을 써서 시간복잡도 커트라인에 턱걸이했다..

이전에 풀었던 아나그램을 베이스로 풀다 보니 최적화하기가 어려운 것 같다.
문제에 맞는 풀이법을 생각해보자..

주어진 문자열을 문자 배열로 만들고, 문자 배열을 sorting한다면 아나그램의 key가 된다.
key가 없으면 list를 만들어주고, 있으면 그 key에 문자열을 넣어주자.
해설을 보고, 이해하고 풀고나면 쉬운데..
왜 처음에 못 풀까..
 */
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        
        for (String str : strs) {
            char[] tempArray = str.toCharArray();
            Arrays.sort(tempArray);
            String key = new String(tempArray);

            result.putIfAbsent(key, new ArrayList<>());
            result.get(key).add(str);
        }
        return new ArrayList<>(result.values());
    }
}

