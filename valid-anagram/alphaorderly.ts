/**
 * 시간 복잡도: O(n + m)
 * 공간 복잡도: O(k)
 */
function isAnagram(s: string, t: string): boolean {
    let s_map = new Map();
    let t_map = new Map();

    for (let i = 0;i < s.length;i += 1) {
        if (s_map.has(s[i])) s_map.set(s[i], s_map.get(s[i]) + 1);
        else s_map.set(s[i], 1);
    }

    for (let i = 0;i < t.length;i += 1) {
        if (t_map.has(t[i])) t_map.set(t[i], t_map.get(t[i]) + 1);
        else t_map.set(t[i], 1);
    }    

    for (const key of s_map.keys()) {
        if (!t_map.has(key)) return false;
        if (t_map.get(key) != s_map.get(key)) return false;
    }

        for (const key of t_map.keys()) {
        if (!s_map.has(key)) return false;
        if (t_map.get(key) != s_map.get(key)) return false;
    }

    return true;
};
