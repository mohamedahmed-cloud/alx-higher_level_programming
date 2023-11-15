class Person {
    constructor(name) {
        this.name = name;
    }
    intro(){
        console.log(`This is ${this.name}`);
    }
}
class Student extends Person {
    constructor(name, age) {
        super(name)
        this.age = age;
    }
    intro(){
        console.log(`This is ${this.name} and age is ${this.age}`);
    }
}

p = new Person("USF");
p.intro();
ss = new Student("USF", 12)

ss.intro();
