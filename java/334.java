package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public boolean increasingTriplet(int[] nums) {
            int s1 = Integer.MAX_VALUE;
            int s2 = Integer.MAX_VALUE;
            for (int num : nums) {
                if (num <= s1) {
                    s1 = num;
                } else if (num <= s2) {
                    s2 = num;
                } else {
                    return true;
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().increasingTriplet(new int[]{1, 2, 3, 4, 5}));
        System.out.println(new Algorithm().new Solution().increasingTriplet(new int[]{5, 4, 3, 2, 1}));
    }

}

