export function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i]

        for (let j = i + 1; j < nums.length; j++)
            if (num + nums[j] === target) return [i, j]
    }
}
