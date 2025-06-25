#include <iostream>
using namespace std;

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void sort_array(int array[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                swap(&array[j], &array[j + 1]);
            }
        }
    }
}

int main() {
    int array[5] = { 5, 6, 6, 4, 3};
    int odd_array[3];
    int even_array[2];
    int sorted_array[5];
    int j = 0, k = 0;
    for (int i = 0; i < 5; i++) {
        if (i % 2 == 0) {
            even_array[j] = array[i];
            j++;
        }
        else {
            odd_array[k] = array[i];
            k++;
        }
    }
    sort_array(even_array, 2);
    sort_array(odd_array, 3);
    j = 0;
    k = 0;
    for (int i = 0; i < 5; i++) {
        if (i % 2 == 0) {
            sorted_array[i] = even_array[j];
            j++;
        }
        else {
            sorted_array[i] = odd_array[k];
            k++;
        }
    }
    for (int i = 0; i < 5; i++) {
        cout << sorted_array[i] << " ";
    }
    return 0;
}