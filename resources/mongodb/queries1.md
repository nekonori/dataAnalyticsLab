## Student Database Queries

Create student table with the following schema using MongoDB and implement the following:

(Sregno, Sname, phoneno, address, mailid, dept, Sem, CGPA)

Note: Insert 10 records.

#### 1. Display all the student who study in (IT, CSE) department.

```bash
db.students.find({dept: {$in: ["IT", "CSE"]}})
```

#### 2. Update the CGPA of the students after their marks got improved in reevaluation

```bash
db.students.updateMany({cgpa: {$lt: 7}}, {$inc: {cgpa: 0.5}})
```

#### 3. Display the details of students are ranked as 'TOP 5' based on the CGPA.

```bash
db.students.find().sort({cgpa: -1}).limit(5)
```

#### 4. Remove the details of the students who are not assigned with register no.

```bash
db.students.deleteMany({sregno: null})
```

#### 5. Display the count of students in each department

```bash
db.students.aggregate([{$group: {_id: "$dept", count: {$sum: 1}}}])
```

#### 6. Display all the IT department students with CGPA greater than 6, but less than 7.5.

```bash
db.students.find({dept: "IT", cgpa: {$gt: 6, $lt: 7.5}})
```

#### 7. Display all the CSE students in ascending order

```bash
db.students.find({dept: "CSE"}).sort({sname: 1})
```

#### 8. Update the phone number and mailid of any student in CSE department.

```bash
db.students.updateOne({dept: "CSE"}, {$set: {phoneno: "1234567890", mailid: "new.mail@example.com"}})
```
