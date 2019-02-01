#include <stdio.h>
#include <assert.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int maxArea(int* height, int heightSize) {
    int max_area = 0;
    int index_start = 0;
    int index_end = heightSize - 1;
    while (index_start < index_end) {
        max_area = max(max_area, min(height[index_start], height[index_end]) * (index_end - index_start));
        if (height[index_start] < height[index_end]) {
            index_start += 1;
        } else {
            index_end -= 1;
        }
    }
    return max_area;
}

int main(int argc, char **args) {
    return 0;
}