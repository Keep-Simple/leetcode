// nums1.length == m
// nums2.length == n
// 0 <= m <= 1000
// 0 <= n <= 1000
// 1 <= m + n <= 2000
// -106 <= nums1[i], nums2[i] <= 106

export function findMedianSortedArrays(
    nums1: number[],
    nums2: number[]
): number {
    nums1 = nums1.concat(nums2).sort((a, b) => a - b)

    const mergedArrayLength = nums1.length

    if (mergedArrayLength % 2 === 0) {
        const mid1 = nums1[mergedArrayLength / 2 - 1]
        const mid2 = nums1[mergedArrayLength / 2]
        return (mid1 + mid2) / 2
    }

    return nums1[Math.floor(mergedArrayLength / 2)]
}

function insertAfter<T>(arr: T[], idx: number, val: T) {
    arr.splice(idx, 0, val)

    return arr
}
