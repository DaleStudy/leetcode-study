class Solution {
    // t가 s의 철자를 모두 포함하고 있는 애너그램인지를 확인하는 문제
    // 푸는 방법은 2가지
    // 1. 유니코드로 변환해서 sort 해서 푸는 방법
    // 2. 정렬하지 않고 mutableMap으로 맵을 만들어 푸는 방법
    // 2번으로 문제를 풀었다.
    fun isAnagram(s: String, t: String): Boolean {
        //우선 처음부터 두 String의 길이가 다르면 바로 false를 반환
        if(s.length != t.length) false

        // s의 문자열을 카운트하면서 저장할 가변배열을 선언해준다.
        val countMap = mutableMapOf<Char, Int>()

        // s에 있는 각각의 문자들에 대해서 반복문을 돌면서 출현횟수를 맵으로 구성
        for(c in s){
            countMap[c] = countMap.getOrDefault(c, 0) + 1
        }

        // 이제 t의 문자들이 아까 만들어진 countMap에 모두 존재하는지 확인
        for(c in t){
            val count = countMap.getOrDefault(c, 0)
            if (count == 0) return false
            countMap[c] = count - 1
        }
        // countMap에 들어있는 value가 전부 0이면 true를 반환
        return countMap.values.all { it == 0 }
    }
}

