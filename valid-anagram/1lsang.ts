const getCountObj = (s: string) => {
    const obj:Record<string, number> = {};
    s.split('').forEach((v) => obj[v] ? obj[v]+=1 : obj[v] = 1);
    return obj;
}

const isEqual = (a: Record<string, number>, b: Record<string, number>) => {
    return Object.entries(a).every(([key, value]) => b[key] === value)
}

function isAnagram(s: string, t: string): boolean {
    return s.length === t.length && isEqual(getCountObj(s), getCountObj(t));
};