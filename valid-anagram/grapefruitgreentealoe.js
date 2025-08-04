
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;

    const map = new Map();

    for (let ch of s) {
        map.set(ch, (map.get(ch) || 0) + 1);
    }

    for (let ch of t) {
        if (!map.has(ch)) return false;
        map.set(ch, map.get(ch) - 1);
        if (map.get(ch) < 0) return false;
    }

    return true;
};

//시간복잡도 : O(n)
//공간복잡도 : O(1) (영문자니까 들어갈 수 있는 수가 한정되어있으므로. )
