const students = [
    {id:1,fname:'moses',marks:90},
    {id:2,fname:'john',marks:87},
    {id:3,fname:'peter',marks:30},
    {id:4,fname:'brian',marks:50},
    {id:5,fname:'louie',marks:20},
    {id:6,fname:'hope',marks:47},
    {id:7,fname:'denise',marks:66}
]

const failed_students = students.filter(student => student.marks<50)
console.log(failed)