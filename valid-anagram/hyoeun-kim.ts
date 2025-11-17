function isAnagram(s: string, t: string): boolean {
    let sObj = {}
    let tObj = {}

    s.split('').sort().map((sChar) => {
        if(sChar in sObj) {
            sObj[sChar] += 1
        } else {
            sObj[sChar] = 1
        }
    })

    t.split('').sort().map((tChar) => {
        if(tChar in tObj) {
            tObj[tChar] += 1
        } else {
            tObj[tChar] = 1
        }
    })

    return JSON.stringify(sObj) === JSON.stringify(tObj)
};