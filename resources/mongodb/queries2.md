## Employee Database Queries

Create employee table with the following schema using MongoDB and implement the following:

(eid, ename, dept, designation, salary,yearofioining, address(dno,street, locality, city))

Note: Insert 10 records.

### 1. Display all the employees with salary in range (50000, 75000)

```bash
db.employees.find({salary: {$gt: 50000, $lt: 75000}})
```

### 2. Update the salary of employee whose designation is `Developer' by 5000 increment

```bash
db.employees.updateMany({designation: "Developer"}, {$inc: {salary: 5000}})
```

### 3. Display the details of employees are ranked as `TOP 5' based on the salary they receive.

```bash
db.employees.find().sort({salary: -1}).limit(5)
```

### 4. Remove the details of an employee who are not assigned with any department.

```bash
db.employees.deleteMany({dept: null})
```

### 5. Display the count of employees in each department

```bash
db.employees.aggregate([{$group: {_id: "$dept", count: {$sum: 1}}}])
```
