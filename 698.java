package com.bawuju.java.demo.pure;

import java.util.Arrays;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {

        public boolean canPartitionKSubsets(int[] nums, int k) {
            int sum = Arrays.stream(nums).sum();
            if (sum % k > 0) {
                return false;
            }
            int target = sum / k;
            return search(new int[k], nums.length - 1, nums, target);
        }

        public boolean search(int[] groups, int point, int[] nums, int target) {
            if (point < 0)
                return true;
            int value = nums[point--];
            for (int i = 0; i < groups.length; i++) {
                if (groups[i] + value <= target) {
                    groups[i] += value;
                    if (search(groups, point, nums, target))
                        return true;
                    groups[i] -= value;
                }
                if (groups[i] == 0)
                    break;
            }
            return false;
        }

    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().canPartitionKSubsets(new int[]{4, 3, 2, 3, 5, 2, 1}, 4) + " " + true);
        System.out.println(new Algorithm().new Solution().canPartitionKSubsets(new int[]{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, 5) + " " + true);
        System.out.println(new Algorithm().new Solution().canPartitionKSubsets(new int[]{10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6}, 3) + " " + true);
    }

}

