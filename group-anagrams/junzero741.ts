// TC: O(N*KlogK)
// SC: O(N*K)
function groupAnagrams(strs: string[]): string[][] {

    const idMap = new Map<string, string[]>();

    for(const str of strs) {
        const id = str.split("").sort().join("");

        if(!idMap.has(id)) {
            idMap.set(id, [])
        }

        idMap.get(id)!.push(str)
    }

    return [...idMap.values()]

};
