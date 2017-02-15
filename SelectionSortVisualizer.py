# Spin-off of "Project: Selection sort visualizer"

'''
 origin JS code:

var displayArray = function(array) {
    textFont(createFont("monospace"), 12);

};

var swap = function(array, firstIndex, secondIndex){
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = array[firstIndex];
};

var indexOfMinium = function(array, startIndex){
    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex; i < array.length; i++){
        if(array[i] < minValue){
            minValue = array[i];
            minIndex = i;
        }
    }
    return minValue;
};


var selectionSort = function(array) {
    var temp;

    for(var i = 0; i < array.length; i++){
        temp = indexOfMinium(array, i);
        swap(array, i, temp);
    }
};

var array = [2, 1];
array = selectionSort(array);
'''

