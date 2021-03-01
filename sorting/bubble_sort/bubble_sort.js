const numbers = [9,4,1,2,0,8]

let j,i

function sort(arr){
    for(i=0; i< arr.length; i++){
        for(j=0; j<arr.length-i-1; j++){
            if(arr[j]>arr[j+1]){
                var temp
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
}

sort(numbers)

console.log(numbers)