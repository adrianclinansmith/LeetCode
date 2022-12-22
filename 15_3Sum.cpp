/*
LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result = {};
        return result;
    }
    void test(vector<int>& nums) {
        cout << "Input:\n";
        for (int num : nums) {
            cout << num << ", ";
        }
        cout << "\n\nResult:\n";
        vector<vector<int>> result = threeSum(nums);
        for (vector<int>& tri : result) {
            cout << tri[0] << ", " << tri[1] << ", " << tri[2] << "\n";
        }
        cout << "\n";
    }
};

int main() {
    Solution solution;
    vector nums = { 1, 2, -3, 4 };
    solution.test(nums);
    nums = { -1, 2, -3, 4 };
    solution.test(nums);
    return 0;
}