package com.bawuju.java.demo.pure;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {

        private Map<Integer, Map<Integer, Integer>> dp;

        public int findTargetSumWays(int[] nums, int S) {
            dp = new HashMap<>();
            return findTargetSumWays(nums, S, nums.length - 1);
        }

        private int findTargetSumWays(int[] nums, int S, int end) {
            if (dp.getOrDefault(S, Collections.emptyMap()).getOrDefault(end, Integer.MIN_VALUE) >= 0) {
                return dp.get(S).get(end);
            }
            int result;
            if (end == 0) {
                result = (nums[0] == S ? 1 : 0) + (nums[0] == -S ? 1 : 0);
            } else {
                result = findTargetSumWays(nums, S - nums[end], end - 1) + findTargetSumWays(nums, S + nums[end], end - 1);
            }
            if (!dp.containsKey(S)) {
                dp.put(S, new HashMap<>());
            }
            dp.get(S).put(end, result);
            return result;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
    }

}

