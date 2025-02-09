/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
    let start = 0;
    let end = 0;

    /** t의 모든 문자열이 슬라이드 윈도우의 범위에 들어왔을 때, 그 범위의 최소 길이 */
    let min = s.length;

    /** while 문이 한 번 순회할 때, start 또는 end값 중 end값이 증가했는지 여부 */
    let isEndIndexUp = true;

    /** min 값이 갱신되면 s문자열의 start, end 인덱스값을 저장할 변수 */
    let index = null;

    /** 문자열 t가 보유한 문자와 해당 문자가 들어있는 수를 key, value로 설정한 map객체 */
    const charMap = t.split('').reduce((acc, cur) => {
        if (acc.has(cur)) {
            acc.set(cur, acc.get(cur) + 1);
        } else {
            acc.set(cur, 1);
        }

        return acc;
    }, new Map());

    while (end < s.length) {
        const curChar = s[end];

        if (isEndIndexUp && t.includes(curChar)) {
            // end가 증감되었고 s의 end 인덱스의 문자가 t에 존재한다면 해당 키의 값에 1을 감소
            charMap.set(curChar, charMap.get(curChar) - 1);
        }

        /** 모든 t의 문자들이 슬라이드 윈도우의 범위에 들어왔는지 여부를 체크하는 불린값 */
        const everyCharCollected = [...charMap].every(([_, value]) => value <= 0);

        if (everyCharCollected) {
            // 모든 문자열이 슬라이드 윈도우의 문자열에 포착된 경우
            if (t.includes(s[start])) {
                // s의 start 인덱스 문자가 t에 존재한다면 charMap에 해당 키의 값에 1을 증감
                charMap.set(s[start], (charMap.get(s[start]) || 0) + 1);
            }

            const gap = end - start;
            if (gap < min) {
                // t의 모든 문자가 슬라이드 윈도우의 범위에 있고, 현재 그 윈도우의 길이가 이전의 min값 보다 작다면 업데이트
                min = gap;
                index = [start, end];
            }

            start++;
            isEndIndexUp = false;
        } else {
            // 윈도우에 문자열이 하나라도 부족한 경우
            end++;
            isEndIndexUp = true;
        }
    }

    return index ? s.slice(index[0], index[1] + 1) : '';
};

// 공간복잡도 O(t) -> 최대 t의 길이에 따라 맵의 크기가 결정되므로
// 시간복잡도 O(s * t) -> s를 순회하는 while 문에서 최대 O(t)의 공간복잡도를 따르는 map 객체가 배열로 변환되어 every 메소드가 호출되기 때문에
