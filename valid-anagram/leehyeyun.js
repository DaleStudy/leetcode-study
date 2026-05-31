/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/*
    두 문자열 s와 t가 주어졌을 때,
    t가 s의 애너그램(anagram)이면 true,
    아니면 false를 반환하는 함수.

    애너그램이란?
    → 문자열에 포함된 문자들의 종류와 개수가 모두 동일한 경우.
      (순서는 상관 없음)

    요청형식 : isAnagram(s, t)

    입력형식 :
      - s, t는 모두 소문자 알파벳으로 구성된 문자열
      - 1 <= s.length, t.length <= 5 * 10^4

    출력형식 :
      - t가 s의 애너그램이면 true
      - 아니면 false

    요청예시 :
      isAnagram("anagram", "nagaram")
    출력예시 :
      true

      isAnagram("rat", "car")
    출력예시 :
      false

    Follow-up :
      - 만약 유니코드 문자(한글, 일본어, 이모지 등)를 포함한다면
        문자 빈도수를 저장할 때 ASCII 배열 대신
        해시맵(Map, Object)을 사용하여 해결할 수 있다.
*/

var isAnagram = function(s, t) {
    
    const map = new Map();

    //문자열 s를 순회하면서 각 요소를 map 방식으로 넣어줌
    for(const s_char of s){
        if(map.has(s_char))
        {
            var s_char_count =  map.get(s_char)

            s_char_count ++;
            
            map.set(s_char,s_char_count)
        }else {
            map.set(s_char,1)
        }
    }

    //문자열 t를 순회하면서 각 요소를 map에서 빼줌
    for(const t_char of t){
        if(map.has(t_char))
        {
            var t_char_count = map.get(t_char)

            t_char_count --;

            if(t_char_count === 0)
            {
                map.delete(t_char)
            }else if(t_char_count > 0)
            {
                map.set(t_char,t_char_count)
            }else {
                return false;
            }
        }else {
            return false;
        }
    }

    //최종 리턴
    if(map.size == 0)
    {
        return true;
    }else {
        return false;
    }
};

console.log("Example 1:", isAnagram("anagram", "nagaram")); // true
console.log("Example 2:", isAnagram("rat", "car")); // false

