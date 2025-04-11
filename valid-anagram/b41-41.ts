function isAnagram(s: string, t: string): boolean {
    /* 방법 1:
     * 문자열을 순서대로 정렬 후 맞는지 비교한다.

     * 시간 복잡도: O(n log n) - 문자열 정렬에 O(n log n) 시간이 소요됨
     * 공간 복잡도: O(n) - 정렬된 문자열을 저장하기 위한 추가 배열 필요
     */
    const checkAnagramFromSort = (): boolean => {
        if (s.length !== t.length) {
            return false;
        }

        const sortedS: string[] = [...s].sort();
        const sortedT: string[] = [...t].sort();

        for(let i = 0; i < s.length; i++) {
            console.log(sortedS[i], sortedT[i]);
            if(sortedS[i] !== sortedT[i]) {
                return false;
            }
        }

        return true;
    }

    /* 방법 2: (Failed)
     * Size 체크 후 Set객체에 s단어를 할당한 후 t에서 has메소드로 체크

     * 시간 복잡도: O(n) - 문자열을 한 번씩 순회
     * 공간 복잡도: O(k) - k는 고유 문자의 수 (최대 알파벳 개수만큼)
     * 실패 이유: Set 객체를 사용하여 중복 문자가 사라지기 때문에 정상적인 비교가 불가
     */
    const checkAnagramFromSetObject = (): boolean => {
        const sSet = new Set(s);
        const tSet = new Set(t);

        if (s.length !== t.length) {
            return false;
        } else {
            for(let str of sSet) {
                if(!tSet.has(str)) {
                    return false;
                }
            }

            return true;
        }
    };

    /* 방법3:
     * countMap을 만들어 둠
     * Map<string, number> 타입
     * S, T의 길이가 일치한다는 가정 하에
     * S는 알파벳마다 +1을 T는 -1을 계산
     * 값이 0이 되는 순간 항상 삭제
     * 전부 돌았을 때 countMap.size가 0인 경우 true
     * 
     * 시간 복잡도: O(n) - 문자열을 한 번만 순회
     * 공간 복잡도: O(k) - k는 고유 문자의 수 (최대 알파벳 개수만큼)
     */
    const checkAnagramFromCountMap = ():boolean => {
        if(s.length !== t.length) return false;

        const countMap = new Map<string, number>();

        for(let i = 0; i < s.length; i++) {
            const sWord = s[i];
            const tWord = t[i];

            const prevSValue = countMap.get(sWord) ?? 0;
            const nextSValue = prevSValue + 1;
            if(nextSValue === 0) {
                countMap.delete(sWord)
            } else {
                countMap.set(sWord, nextSValue);
            }

            const prevTValue = countMap.get(tWord) ?? 0;          
            const nextTValue = prevTValue - 1;
            if (nextTValue === 0) {
                countMap.delete(tWord)
            } else {
                countMap.set(tWord, nextTValue);
            }
        };

        return countMap.size === 0;
    
    };
    
    // return checkAnagramFromSort();
    // return checkAnagramFromSetObject();
    return checkAnagramFromCountMap();
};
