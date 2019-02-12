package com.bawuju.java.demo.pure;

import java.util.Stack;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * proxy
     */
    class Solution {
        public int longestValidParentheses(String s) {
            return new StackSolution().longestValidParentheses(s);
        }
    }

    /**
     * 用栈
     */
    class StackSolution {
        public int longestValidParentheses(String s) {
            int max = 0;
            Stack<Integer> stack = new Stack<>();
            stack.push(-1);
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '(') {
                    stack.push(i);
                } else {
                    stack.pop();
                    if (stack.isEmpty()) {
                        stack.push(i);
                    } else {
                        max = Math.max(max, i - stack.peek());
                    }
                }
            }
            return max;
        }
    }

    /**
     * 动态规划
     */
    class DPSolution {
        public int longestValidParentheses(String s) {
            int[] dp = new int[s.length()];
            int max = 0;
            for (int i = 1; i < s.length(); i++) {
                int other = i - dp[i - 1] - 1;
                if (s.charAt(i) != ')') {
                    continue;
                } else if (s.charAt(i - 1) == '(') {
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                } else if (other >= 0 && s.charAt(other) == '(') {
                    dp[i] = dp[i - 1] + 2 + (other >= 1 ? dp[other - 1] : 0);
                }
                max = Math.max(max, dp[i]);
            }
            return max;
        }
    }

    /**
     * 智障解法
     */
    class StupidSolution {
        public int longestValidParentheses(String s) {
            return longestValidParentheses(s.toCharArray(), 0, new int[s.length()]);
        }

        private int longestValidParentheses(char[] chars, int start, int[] dp) {
            if (start >= chars.length) {
                return 0;
            }
            int index = start;
            while (index < chars.length && chars[index] == ')') {
                index++;
            }
            Stack<Character> stack = new Stack<>();
            int maxLength = 0;
            int tmpLength = 0;
            while (index < chars.length) {
                if (dp[index] > 0) {
                    maxLength += dp[index];
                    tmpLength += dp[index];
                    index += dp[index];
                }
                if (chars[index] == '(') {
                    stack.push('(');
                    tmpLength = stack.size() == 1 ? 0 : tmpLength;
                } else if (chars[index] == ')' && !stack.isEmpty()) {
                    stack.pop();
                    maxLength += 2;
                    tmpLength += 2;
                } else if (chars[index] == ')' && stack.isEmpty()) {
                    break;
                }
                index++;
            }
            if (!stack.isEmpty()) {
                maxLength = maxLength - tmpLength;
                index -= (stack.size() + tmpLength);
                if (index == start) {
                    index += 1;
                }
            }
            return Math.max(maxLength, longestValidParentheses(chars, index, dp));
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().longestValidParentheses("(()") + " 2");
        System.out.println(new Algorithm().new Solution().longestValidParentheses(")()())") + " 4");
        System.out.println(new Algorithm().new Solution().longestValidParentheses("()(())") + " 6");
        System.out.println(new Algorithm().new Solution().longestValidParentheses("()(()") + " 2");
        System.out.println(new Algorithm().new Solution().longestValidParentheses(")()(((())))(") + " 10");
        System.out.println(new Algorithm().new Solution().longestValidParentheses("(()(((()") + " 2");
        System.out.println(new Algorithm().new Solution().longestValidParentheses("())") + " 2");
        System.out.println(new Algorithm().new Solution().longestValidParentheses("(()()") + " 4");
    }

}

