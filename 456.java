package com.bawuju.java.demo.pure;

import java.util.Stack;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * s1<s3<s2
     * 所以先找到s3，定下来，然后寻找s2
     * 寻找s2的时候将遍历过的数都用stack记下来
     * 按照策略，s3越大越好，这样s1的选择余地才会大
     * 所以当遍历过程中遇到一个大于s3的数字的时候，就将这个数字作为s2的候选者放入stack中
     * 然后从stack弹出一个数字作为s3
     */
    class Solution {
        public boolean find132pattern(int[] nums) {
            Stack<Integer> stack = new Stack<>();
            int third = Integer.MIN_VALUE;
            for (int i = nums.length - 1; i >= 0; i--) {
                int target = nums[i];
                if (target < third) {
                    return true;
                } else if (target > third) {
                    while (!stack.isEmpty() && stack.peek() < target) {
                        third = stack.pop();
                    }
                    stack.push(target);
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().find132pattern(new int[]{1, 2, 3, 4}));
        System.out.println(new Algorithm().new Solution().find132pattern(new int[]{-1, 3, 2, 0}));
        int[] tmp = new int[10000];
        for (int i = 0; i < tmp.length; i++) {
            tmp[i] = (int) (Math.pow(-1, i) * i * 100000);
        }
        long t = System.currentTimeMillis();
        System.out.println(new Algorithm().new Solution().find132pattern(tmp));
        System.out.println((System.currentTimeMillis() - t) / 1000);
    }

}

