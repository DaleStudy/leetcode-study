function maxArea(height: number[]): number {
    let res = 0
    let l = 0
    let r = height.length - 1
    while (l < r) {
        const area = (r - l) * Math.min(height[l], height[r])
        res = Math.max(res, area)
        if (height[l] > height[r]) {
            r -= 1
        } else {
            l += 1
        }
    }
    return res
};
