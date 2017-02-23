var insert = function(array, rightIndex, value) {
    for(var j = rightIndex;
        j >= 0 && array[j] > value;
        j--) {
        array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
};

var insertionSort = function(array) {
	//filled in the code here
    for(var i = 0; i < array.length-1; i++){
        insert(array, i, array[i+1]);
    }

};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);
// the second part where you made your own array with negative numbers
// also a zero included and a larger array.
var array2 = [99, 77, 88, 55, 66, -11, 2 , 6, 9, 11, 0, 44];
insertionSort(array2);
println("Array after sorting:  " + array2);
Program.assertEqual(array2, [-11, 0, 2, 6, 9, 11, 44, 55, 66, 77, 88, 99]);
