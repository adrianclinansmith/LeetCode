/*
LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

import java.util.*; 

class Solution {
	public int binarySearch(int[] nums, int k) {
		int i = Arrays.binarySearch(nums, k);
		while (i > 0 && nums[i - 1] == k) {
			i = Arrays.binarySearch(nums, 0, i, k);
		}
		return i < 0 ? -i - 1 : i;
	}

    public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		int locOfFirst0 = binarySearch(nums, 0);
		System.out.println("Loc of first 0: " + locOfFirst0);
		return null;
    }

	public static void test(int[] nums) {
		Solution s = new Solution();
		System.out.println("Testing: " + Arrays.toString(nums));
		List<List<Integer>> result = s.threeSum(nums);
		// for (List<Integer> list : result) {
		// 	System.out.println(list.get(0) + ", " + list.get(1) + ", " + list.get(2));
		// }
		System.out.println();
	}

    public static void main(String[] args) {
    	test(new int[]{1, 2, -3, 3, 0}); 
		test(new int[]{0, 0, 0, 0}); 
		test(new int[]{-1, 0, 0, 0, 0, 1}); 
		test(new int[]{0, 2, 3});
		test(new int[]{1, 2, 3}); 
		test(new int[]{-2, 1, 1}); 
    }
}