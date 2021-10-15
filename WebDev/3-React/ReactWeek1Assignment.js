class Student {
    constructor(name, email, community){
        this.name = name;
        this.email = email;
        this.community = community; 
    }
}

class Bootcamp {
    constructor(name, level, students = []) {
    this.name= name;
    this.level = level;
    this.students = students;
    }     
    registerStudent(student) {
        const isRegistered = this.students.filter(s => s.email === student.email).length;
        if (emailExist) {
            console.log(`The student ${student.email} is already registered!`);
        } else {
            this.students.push(student);
            console.log(`Registering ${sudent.email} to the bootcamp ${this.name}.`)
        }
        return this.student;
    }
}


const Nucamp = new Bootcamp("Jurgen", 10);
console.log(Nucamp);

const student1 = new Student("John", "john@yahoo.com", "nucamp");
Nucamp.registerStudent(student1);

