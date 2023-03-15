/*
Given an integer array nums of length n and an integer target, find three 
integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
*/

import java.util.Arrays;   

class Solution {
    public int threeSumClosestV1(int[] nums, int target) {
		Arrays.sort(nums);
		int bestSum = nums[0] + nums[1] + nums[nums.length - 1];
		for (int i = 0; i < nums.length; i++) {
			int j = i + 1;
			int k = nums.length - 1;
			while (j < k) {
				int currentSum = nums[i] + nums[j] + nums[k];
				if (currentSum > target) {
					k--;
				}
				else if (currentSum < target) {
					j++;
				}
				else {
					return currentSum;
				}
				if (Math.abs(currentSum - target) < Math.abs(bestSum - target)) {
					bestSum = currentSum;
				}
			}
		}
		return bestSum;
	}

	private Integer[] v2pickClosest(int[] nums, int i, int target) {
		if (i == 0) {
			return new Integer[]{nums[0], null};
		}
		else if (i == nums.length) {
			return new Integer[]{nums[i-1], null};
		}
		int comp = Math.abs(target - nums[i-1]) - Math.abs(target - nums[i]);
		if (comp < 0) {
			return new Integer[]{nums[i-1], null};
		}
		else if (comp > 0) {
			return new Integer[]{nums[i], null};
		}
		return new Integer[]{nums[i-1], nums[i]}; 
	}

	public int threeSumClosestV2(int[] nums, int target) {
		Arrays.sort(nums);
		// int t = Arrays.binarySearch(nums, target);
		// t = t < 0 ? -1 * t - 1 : t;
		int i = 0;
		int k = nums.length - 1;
		int best;
		while (i < k) {
			// int needed = target - nums[i] - nums[k];
			int needed = target - nums[i] - nums[k];
			int j = Arrays.binarySearch(nums, i, k, needed);
			if (j >= 0) {
				return target;
			}
			j = -1 * j - 1;
			if (j == 0) {
				k--;
			}
			else if (j == nums.length) {
				i++;
			}
			int n = Math.abs(needed - nums[j-1]) - Math.abs(needed - nums[j]);
			if (n < 0 ) {

			}
		}
	}

	public static void test(int[] nums, int target) {
		Solution s = new Solution();
		String numsStr = Arrays.toString(nums);
		int v1Solution = s.threeSumClosestV1(nums, target);
		int v2Solution = s.threeSumClosestV2(nums, target);
		System.out.println("V1" + numsStr + ": " + v1Solution);
		System.out.println("V2" + numsStr + ": " + v2Solution + "\n");
	}

	public static void main(String[] args) {
    	test(new int[]{1, 2, -3, 3, 0}, 3); 
    }
}