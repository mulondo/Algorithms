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

console.log(newStudents)