// 모든 단어를 정렬해야하기 때문에 시간 복잡도가 꽤 나오는 문제
// 하지만 모든 단어를 정렬해도 된다는건 글자 수가 100자 제한이 있어서 유추할 수 있다.
// O(N) * O(MlogM) N 배열 길이, M 글자수의 시간복잡도가 나옴
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> anagrams = new HashMap<>();
        for(String str: strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);
            anagrams.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(anagrams.values());
    }
}
