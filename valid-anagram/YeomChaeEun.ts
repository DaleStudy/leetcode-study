function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length) return false

    let counter = {}
    for(let sValue of s) {
        if(!counter[sValue])  { counter[sValue] = 1 }
        else { counter[sValue]++ }

    }

    for(let tValue of t) {
        if(!counter[tValue]) return false
        else counter[tValue]--
    }

    return Object.values(counter).findIndex(value => value !== 0) < 0;
}
