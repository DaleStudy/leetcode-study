/*
[문제풀이]
- char 배열로 맞춰보자 (x)
- s와 t의 길이가 같아야 한다.
- 각 철자의 개수가 s와 t 모두 일치하는지 확인한다. (테스트케이스 하나 실패)

- s 철자의 개수를 세어 놓고, t 철자의 개수는 하나씩 빼서 0을 체크해보자. Map (O)
time: O(N), space: O(N)
    class Solution {
        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) {
                return false;
            }

            Map<Character, Integer> counting = new HashMap<>();
            for (char ch : s.toCharArray()) {
                counting.put(ch, counting.getOrDefault(ch, 0) + 1);
            }
            for (char ch : t.toCharArray()) {
                if (!counting.containsKey(ch)) {
                    return false;
                }
                counting.put(ch, counting.get(ch) - 1);
            }

            return counting.values().stream()
                .allMatch(count -> count == 0);
        }
    }

- Arrays로 정렬 및 비교를 해보자. (O)
time: O(NlogN), space: O(N)
    class Solution {
        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) {
                return false;
            }

            char[] sToCharArray = s.toCharArray();
            char[] tToCharArray = t.toCharArray();
            Arrays.sort(sToCharArray);
            Arrays.sort(tToCharArray);

            return Arrays.equals(sToCharArray, tToCharArray);
        }
    }

- s 철자의 개수를 세어 놓고, t 철자의 개수는 하나씩 빼서 0을 체크해보자. Array (O)
time: O(N), space: O(1)

[회고]
Arrays처럼 자바에서 제공해주는 util을 잘 활용하지 못한 것 같다.. (띵킹하자!)

처음 성공한 솔루션 접근법은 좋았는데 왜 성능이 안나왔나..
HashMap은 내부적으로 해시 테이블 구조를 사용하므로, 동일한 데이터를 저장하더라도 배열보다 메모리를 더 많이 사용한다.
또한, 키와 값을 객체 타입으로 저장하기 때문에 오토박싱/언박싱 비용이 발생하고, 해시 계산과 충돌 처리 등의 추가 연산이 필요하다.
따라서 배열에 비해 느린 것 같다.
*/
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] counting = new int[26];
        for (char ch : s.toCharArray()) {
            counting[ch - 'a']++;
        }
        for (char ch : t.toCharArray()) {
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
