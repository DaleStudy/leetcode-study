import java.util.*;
class Solution {

    /**
     runtime : 17ms
     memory : 44.65mb
     */

    /**
     * [idea 04] : HashMap 1개 사용
     * 길이가 다르다면 anagram이 될 수 없으므로 false 리턴한다.
     * 첫 번째 문자열(s)에 대해서만 Frequency Map(=sFrequency)에 빈도수를 저장한다.
     * 두 번째 문자열(t)을 순회하며 Frequency Map에 저장된 각 Character를 조회하고,
     * 값이 존재하면 해당 값을 꺼내어 1을 뺀 값을 다시 해당 Character(=key)에 저장한다.
     * 갱신된 Frequency Map에 0이 아닌 값이 남아있다면 anagram이 될 수 없으므로 false를 리턴한다.
     * 갱신된 Frequency Map에 값이 0만 남아있다면 anagram이므로 true를 리턴한다.

     * [time-complexity] : O(N)
     * frequency map에 Character 빈도수 저장 : O(N) -> hashMap의 put 메서드와 get 메서드는 각각 O(1)시간 안에 수행 가능
     * frequency map에 저장된 각 Character 빈도수 조회 및 갱신(다시 저장) : O(N)
     *
     * [space-complexity] :  O(K) ≈ O(N)
     * N개의 Character에 대해서, 중복이 제거된 key의 개수가 K라고 할 때, O(K)
     * 최악의 경우, N=K이면(중복된 key가 없다면) O(N)
     *
     */

    public boolean isAnagram04(String s, String t) {

        if (s.length() != t.length()) return false;

        Map<Character, Integer> sFrequency = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sFrequency.put(s.charAt(i), sFrequency.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            if (sFrequency.getOrDefault(t.charAt(i), 0) != 0) {
                sFrequency.put(t.charAt(i), sFrequency.get(t.charAt(i)) - 1);
            }
        }

        for (int count : sFrequency.values()) {
            if (count != 0) return false;
        }
        return true;
    }


    /**
     runtime : 24ms
     memory : 44.66mb
     */

    /**
     * [idea 03] : HashMap 2개 사용
     * 길이가 다르다면 anagram이 될 수 없으므로 false 리턴한다.
     * 같은 길이의 String에 대해서 각각의 Character의 등장 빈도수 map에 저장한다.
     * 하나의 String을 순회하면서 각 Character의 등장 빈도수를 비교한다.
     * 만약 각 frequency map에 저장된 Character의 빈도수가 하나라도 다르다면 anangram이 될 수 없으므로 false를 리턴한다.
     * 모든 Character의 빈도수가 동일하면 anagram이므로 true를 리턴한다.
     *
     * [time-complexity] : O(N)
     * frequency map에 Character 빈도수 저장 : O(N) -> hashMap의 put 메서드와 get 메서드는 각각 O(1)시간 안에 수행 가능
     * frequency map에 저장된 각 Character 빈도수 비교 : O(N)
     *
     * [space-complexity] : O(K) ≈ O(N)
     * N개의 Character에 대해서, 중복이 제거된 key의 개수가 K라고 할 때, O(K)
     * 최악의 경우, N=K이면(중복된 key가 없다면) O(N)
     *
     */

     public boolean isAnagram03(String s, String t) {

         if (s.length() != t.length()) return false;

         Map<Character, Integer> sFrequency = new HashMap<>();
         Map<Character, Integer> tFrequency = new HashMap<>();

         for (int i = 0; i < s.length(); i++) {
             sFrequency.put(s.charAt(i), sFrequency.getOrDefault(s.charAt(i), 0) + 1);
             tFrequency.put(t.charAt(i), tFrequency.getOrDefault(t.charAt(i), 0) + 1);
         }

         for (int i = 0; i < s.length(); i++) {
             if (!sFrequency.get(s.charAt(i)).equals(tFrequency.get(s.charAt(i)))) return false;
         }
         return true;

     }



    /**
     runtime : 8ms
     memory : 44.94mb
     */

    /**
     * [idea 02] : Array를 정렬하여 비교 (=Arrays.sort())
     * 각 String을 char Array 저장한 후 오름차순으로 정렬한다.
     * 그리고 각 원소를 비교하여 다른 부분이 있으면 anagram이 아니므로 false를 리턴한다.
     * 각 원소가 모두 동일하면 anagram이므로 true를 리턴한다.
     *
     * [time-complexity] : O(NlogN)
     * String 길이만큼 Array에 저장 -> O(N)
     * char Array를 오름차순으로 정렬 -> O(NlogN)
     *
     * [space-complexity] : O(N)
     * String 길이만큼 Char Array 저장 -> O(N)
     * Arrays.sort()는 in-place 정렬이기 때문에 추가적인 메모리 사용하지 않음
     *   -> Dual-Pivot QuickSort 기반
     *
     */


     public boolean isAnagram02(String s, String t) {

         if (s.length() != t.length()) return false;

         char[] sArray = new char[s.length()];
         char[] tArray = new char[t.length()];

         for (int i = 0; i < s.length(); i++) {
             sArray[i] = s.charAt(i);
             tArray[i] = t.charAt(i);
         }

         Arrays.sort(sArray);
         Arrays.sort(tArray);

         for (int i = 0; i < sArray.length; i++) {
             if (sArray[i] != tArray[i]) return false;
         }
         return true;

     }


    /**
     runtime : 32ms
     memory : 45.41mb
     */

    /**
     * [idea 01] : List를 정렬하여 비교 (=Collections.sort())
     * 각 String을 Character List로 저장한 후 오름차순으로 정렬한다.
     * 그리고 각 원소를 비교하여 다른 부분이 있으면 anagram이 아니므로 false를 리턴한다.
     * 각 원소가 모두 동일하면 anagram이므로 true를 리턴한다.
     *
     * [time-complexity] : O(NlogN)
     * String 길이만큼 List에 저장 -> O(N)
     * List를 오름차순으로 정렬 -> O(NlogN)
     *
     * [space-complexity] : O(N)
     * String 길이만큼 List 저장 -> O(N)
     * Collections.sort()는 추가 공간 O(N) 필요
     *   -> TimSort (MergeSort + InsertionSort) 기반
     *   -> List는 내부적으로 객체 박싱 + 배열 변환 + TimSort (상대적으로 비효율적)
     *
     */

     public boolean isAnagram01(String s, String t) {

         if (s.length() != t.length()) return false;

         List<Character> sList = new ArrayList<>();
         List<Character> tList = new ArrayList<>();

         for (int i = 0; i < s.length(); i++) {
             sList.add(s.charAt(i));
             tList.add(t.charAt(i));
         }

         Collections.sort(sList);
         Collections.sort(tList);

         for (int i = 0; i < sList.size(); i++) {
             if (!sList.get(i).equals(tList.get(i))) return false;
         }
         return true;
     }


}