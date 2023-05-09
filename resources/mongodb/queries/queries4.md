## Customer Database Queries

Create customer table with the following schema using MongoDB and implement the following:

(customer_id, acc_name, accountno, phoneno,email,branchname,balance)

Note: Insert 10 records.

### 1. Display all the details of customer who belong to specific location.

```bash
db.customers.find({branchname: "Chennai"})
```

### 2. Update the balance of customer as they get interest for the amount on quarterly basis.

```bash
db.customers.updateMany({}, {$mul: {balance: 1.01}})
```

### 3. Display the details of customers are ranked as ‘TOP 5’ based on their balance.

```bash
db.customers.find().sort({balance: -1}).limit(5)
```

### 4. Remove the details of the customer who has zero balance.

```bash
db.customers.deleteMany({balance: 0})
```

### 5. Display the count of customer in each location.

```bash
db.customers.aggregate([{$group: {_id: "$branchname", count: {$sum: 1}}}])
```

### 6. Display all the customers who belong to specific location and also with balance greater than 1000, but less than 1 lakhs.

```bash
db.customers.find({branchname: "Chennai", balance: {$gt: 1000, $lt: 100000}})
```

### 7. all the customer details in descending order based on their balance

```bash
db.customers.find().sort({balance: -1})
```

### 8. Update the phone number and email of specific customer.

```bash
db.customers.updateOne({customer_id: 1}, {$set: {phoneno: 1234567890, email: "mail@example.com"}})
```
