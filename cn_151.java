package com.bawuju.java.demo.pure;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bawuju on 2019/1/21.
 * Email: bawuju@gmail.com
 */
public class Main {

    public static void main(String[] args) {
        System.out.println(new Main().new Solution().reverseWords("the sky is blue").equals("blue is sky the"));
    }

    public class Solution {
        public String reverseWords(String s) {
            s += " ";
            List<StringBuilder> builderList = new ArrayList<>();
            StringBuilder builder = new StringBuilder();
            StringBuilder tmp = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                char target = s.charAt(i);
                if (target == ' ') {
                    if (tmp.length() > 0) {
                        builderList.add(tmp);
                        tmp = new StringBuilder();
                    }
                } else {
                    tmp.append(target);
                }
            }
            for (int i = builderList.size() - 1; i >= 0; i--) {
                builder.append(builderList.get(i));
                if (i > 0) {
                    builder.append(" ");
                }
            }
            return builder.toString();
        }
    }

}
