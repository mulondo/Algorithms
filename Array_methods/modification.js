// for - loops through a block of code a number of times
// for/in - loops through the properties of an object
// for/of - loops through the values of an iterable object
// while - loops through a block of code while a specified condition is true
// do/while - also loops through a block of code while a specified condition is true

const students = [
    {
        id: 1,
        name: 'John'
    },
    {
        id: 2,
        name: 'Adam'
    },
    {
        id: 3,
        name: 'Brian'
    },
    {
        id: 4,
        name: 'Peter'
    }
]

const newStudents = []
let i

// creating the map functions's array behavior with plain for loop

for(i =0; i<students.length;i++){
    const newDict = {}
    newDict.id = students[i].id
    newDict.name = students[i].name+'s'
    newStudents.push(newDict)
}

// create the same effect with the ordinary for loop

const modifiedStudents = []
for(let std in students){
    const newDict = {}
    newDict.id = students[std].id
    newDict.name = students[std].name + 'z'
    modifiedStudents.push(newDict)
}

// craete the same effect with for of
const editStudentsData = []

for(let std in students){
    console.log('for the for of', students[std])
    const newDict = {}
    newDict.id = students[std].id
    newDict.name = students[std].name + 'zz'
    editStudentsData.push(newDict)
}

console.log(editStudentsData)