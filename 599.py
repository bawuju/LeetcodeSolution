#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_sum = -1
        result = []
        map1 = {}
        for index in range(len(list1)):
            map1[list1[index]] = index
        for index in range(len(list2)):
            c = list2[index]
            if c not in map1.keys():
                continue
            sum_loop = map1[c] + index
            if index_sum == -1:
                index_sum = sum_loop
                result.append(c)
                continue
            if sum_loop > index_sum:
                continue
            elif sum_loop == index_sum:
                result.append(c)
            else:
                index_sum = sum_loop
                result.clear()
                result.append(c)
        return result


if __name__ == '__main__':
    assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]) == ["Shogun"]
    assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]
    assert Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]) == ["KFC","Burger King","Tapioca Express","Shogun"]
    assert Solution().findRestaurant(["k", "KFC"], ["k", "KFC"]) == ["k"]
