/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = function (s, t) {
    const counter = Array.from(t).reduce((obj, char) => {
        obj[char] = (obj[char] || 0) + 1;
        return obj;
    }, {});

    let lettersToSatisfy = Object.keys(counter).length;
    let minStart = 0;
    let minEnd = Infinity;

    let start = 0;
    for (let end = 0; end < s.length; end++) {
        // s[end]가 t에 포함된 문자인 경우
        if (s[end] in counter) {
            counter[s[end]]--;

            // 해당 문자가 범위 안에 모두 포함된 경우
            if (counter[s[end]] === 0) {
                lettersToSatisfy--;
            }
        }

        // 현재 범위에 t 내 모든 문자가 포함된 경우
        while (lettersToSatisfy === 0) {
            // 더 작은 범위로 정답 갱신
            if (end - start < minEnd - minStart) {
                minStart = start;
                minEnd = end;
            }

            // start 늘리기
            if (s[start] in counter) {
                counter[s[start]]++;
                if (counter[s[start]] > 0) {
                    lettersToSatisfy++;
                }
            }

            start++;
        }
    }

    return minEnd === Infinity ? '' : s.slice(minStart, minEnd + 1);
};

// 시간복잡도: O(m) (m: s.length)
// 공간복잡도: O(1)
