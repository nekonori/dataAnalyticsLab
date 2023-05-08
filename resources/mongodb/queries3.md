## Product Database Queries

Create product table with the following schema using MongoDB and implement the following:

Prod uct(pid,pname,ptype,price,manufacturer,stockqty ,tax (CGST,SCGST))

Note: Insert 10 records.

### 1. Display all the products which has price greater than Rs.500/-

```bash
db.products.find({price: {$gt: 500}})
```

### 2. Update the tax field based on the tax structure issued by Govenrment

```bash
db.products.updateMany({}, {$set: {tax: {cgst: 0.09, sgst: 0.09}}})
```

### 3. Display the total count of the product based on the type of product.

```bash
db.products.aggregate([{$group: {_id: "$ptype", count: {$sum: 1}}}])
```

### 4. Delete the product if the manufacturer of the product stops its production.

```bash
db.products.deleteMany({manufacturer: null})
```

### 5. Update the stock count of the product if more products are delivered

```bash
db.products.updateMany({}, {$inc: {stockqty: 10}})
```
