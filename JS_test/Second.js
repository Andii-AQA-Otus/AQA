
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

for (ageTest in person_1) {
    if (person_1[ageTest] == 30) {
        console.log( 'It\'s Ok')
    }
    else {
        console.log( 'It\'s not Ok')
    }
}
console.log (person_1.name)