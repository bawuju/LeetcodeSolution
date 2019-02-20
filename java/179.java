package com.bawuju.java.demo.pure;

import java.util.Arrays;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 直接使用String自带的compareTo方法
     * 因为这个方法本身就是从最高位开始按照编码大小开始比较
     */
    class Solution {
        public String largestNumber(int[] nums) {
            return Arrays.stream(nums)
                    .mapToObj(String::valueOf)
                    .sorted((o1, o2) -> (o2 + o1).compareTo(o1 + o2))
                    .reduce((s, s2) -> s.equals("0") ? s2 : s + s2)
                    .get();
        }
    }

    public static void main(String[] args) {

    }

}

