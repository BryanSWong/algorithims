
'''

Swap function

A key step in many sorting algorithms (including selection sort) is swapping the location of two items in an array.
Here's a swap function that looks like it might work, but doesn't:
-the code prints out [9, 9, 4] when it should print out [9, 7, 4].

Fix the swap function.

Hint: Work through the code line by line, writing down the values of items in the array after each step.
Could you use an extra temporary variable to solve the problem that shows up?

Once implemented, uncomment the Program.assertEqual() at the bottom to verify that the test assertion passes.

var swap = function(array, firstIndex, secondIndex) {
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = array[firstIndex];
};

var testArray = [7, 9, 4];
swap(testArray, 0, 1);

println(testArray);

//Program.assertEqual(testArray, [9, 7, 4]);

'''

# code converted to python
test_array = [7, 9, 4]


def swap(array, slot1, slot2):
    temp = array[slot1]
    array[slot1] = array[slot2]
    array[slot2] = temp


swap(test_array, 0, 1)
print(test_array)
