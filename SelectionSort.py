'''

Selection sort loops over positions in the array. For each position, it finds the index of the minimum value
in the subarray starting at that position. Then it swaps the values at the position and at the minimum index.
Write selection sort, making use of the swap and indexOfMinimum functions.

Once implemented, uncomment the Program.assertEqual() at the bottom to verify that the test assertion passes.

javascript code:

var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    }
    return minIndex;
};

var selectionSort = function(array) {

};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
println("Array after sorting:  " + array);

//Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

'''


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def index_of_minimum(array, start_index):
    min_value = array[start_index]
    min_index = start_index

    for index in range(min_index, len(array)):
        if array[index] < min_value:
            min_index = index
            min_value = array[index]

    return min_index


def selection_sort(array):

    for num in range(len(array)):
        temp = index_of_minimum(array, num)
        swap(array, num, temp)


test = [22, 11, 99, 88, 9, 7, 42]
selection_sort(test)
print("Array after sorting: ")
print(test)
