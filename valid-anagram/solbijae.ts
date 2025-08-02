function isAnagram(s: string, t: string): boolean {
    // 첫 시도: 시간 복잡도 O(n log n), 공간 복잡도 O(n)
    // const sSort = s.split('').sort();
    // const tSort = t.split('').sort();
    // return JSON.stringify(sSort) === JSON.stringify(tSort);

    // 시간 복잡도 O(n), 공간복잡도 O(1)
    if (s.length !== t.length) return false;

    const count = new Array(26).fill(0);
    for (let i=0; i<s.length; i++) {
        count[s.charCodeAt(i) - 97]++;
        count[t.charCodeAt(i) - 97]--;
    }

    return count.every(c => c === 0);
};
