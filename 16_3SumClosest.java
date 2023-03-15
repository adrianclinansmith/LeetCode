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

	private int closer(Integer a, Integer b, int target) {
		if (a == null || b == null) {
			return a == null ? b : a;
		}
		int comp = Math.abs(a - target) - Math.abs(b - target);
		if (comp < 0) {
			return a;
		}
		return b;
	}

	/* V2 is not working! */

	private Integer[] v2pickClosest(int[] nums, int i, int needed) {
		/* Return [nums[i-1], null] or [num[i], null] depending on which is
		closest to needed, or [nums[i-1], null[i]] if both are equally close. */
		if (i == 0) {
			return new Integer[]{nums[0], null};
		}
		else if (i == nums.length) {
			return new Integer[]{nums[i-1], null};
		}
		int comp = Math.abs(nums[i-1] - needed) - Math.abs(nums[i] - needed);
		if (comp < 0) {
			return new Integer[]{nums[i-1], null};
		}
		else if (comp > 0) {
			return new Integer[]{nums[i], null};
		}
		return new Integer[]{nums[i-1], nums[i]}; 
	}

	private int v2(int[] nums, int i, int k, int target, Integer best) {
		while (i < k || 
		(best != null && nums[i] + nums[k] + nums[best] == target)) 
		{
			// int needed = target - nums[i] - nums[k];
			int perfect = target - nums[i] - nums[k];
			int j = Arrays.binarySearch(nums, i, k+1, perfect);
			if (j >= 0) {
				return target;
			}
			j = -1 * j - 1; // make j ≥ 0 if `perfect` is not in `n`
			Integer[] optimal = v2pickClosest(nums, j, perfect);
			best = closer(optimal[0], best, perfect);
			if (optimal[1] != null) {
				best = v2(nums, i+1, k, target, best);
				best = v2(nums, i, k-1, target, best);
			}
			else if (optimal[0] < perfect) {
				k--;
			}
			else {
				i++;
			}	
		}
		return best;
	}

	public int threeSumClosestV2(int[] nums, int target) {
		Arrays.sort(nums);
		return v2(nums, 0, nums.length - 1, target, null);
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