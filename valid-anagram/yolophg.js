var isAnagram = function(s, t) {
    firstList = s.split("").sort();
    secondList = t.split("").sort();

    // compare if these are same and return
    return JSON.stringify(firstList) === JSON.stringify(secondList);
};