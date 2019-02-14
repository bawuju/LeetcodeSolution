package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public String shiftingLetters(String S, int[] shifts) {
            StringBuilder builder = new StringBuilder();
            long times = 0;
            for (int shift : shifts) {
                times += shift;
            }
            for (int i = 0; i < S.length(); i++) {
                builder.append((char) ('a' + (S.charAt(i) - 'a' + (times -= i > 0 ? shifts[i - 1] : 0)) % 26));
            }
            return builder.toString();
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().shiftingLetters("abc", new int[]{3, 5, 9}) + " rpl");
        System.out.println(new Algorithm().new Solution().shiftingLetters("mkgfzkkuxownxvfvxasy", new int[]{505870226, 437526072, 266740649, 224336793, 532917782, 311122363, 567754492, 595798950, 81520022, 684110326, 137742843, 275267355, 856903962, 148291585, 919054234, 467541837, 622939912, 116899933, 983296461, 536563513}) + " wqqwlcjnkphhsyvrkdod");
    }

}

