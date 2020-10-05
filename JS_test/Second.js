
let person_1 = {
    name : 'Andrii',
    age : 30,
    weight : 70,
    height : 180,
};

let person_2 = {
    name : 'Ira',
    age : 22,
    weight : 50,
    height : 165,
};

// for (ageTest in person_1) {
//     if (person_1[ageTest] == 30) {
//         console.log( 'It\'s Ok')
//     }
//     else {
//         console.log( 'It\'s not Ok')
//     }
// }
// console.log (person_1.name)

function forPerson_1(){
    person_1.name = person_2.name
    person_1.age = person_2.age
    person_1.weight = person_2.weight
    person_1.height = person_2.height
}
forPerson_1()
console.log (person_1)
  