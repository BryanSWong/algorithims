var insert = function(array, rightIndex, value) {
    var i;

    for(i = rightIndex; i >= 0; i--){
        if(value < array[i]){
          array[i + 1] = array[i];
          array[i] = value;
        }
    }
    return array;
};

var array = [3, 5, 7, 11, 13, 2, 9, 6];

insert(array, 4, 2);
console.log("Array after inserting 2:  " + array);


insert(array, 5, 9);
console.log("Array after inserting 9:  " + array);


insert(array, 6, 6);
console.log("Array after inserting 6:  " + array);

