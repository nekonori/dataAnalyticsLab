## Joining Collections

```
db.teachers.insertMany([
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses taken": [1, 2]
  },
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "courses taken": [2, 3]
  },
  {
    "name": "Robert Johnson",
    "email": "robert.johnson@example.com",
    "courses taken": [1, 3]
  }
]);
```

```
db.courses.insertMany([
  {
    "_id": 1,
    "name": "Mathematics"
  },
  {
    "_id": 2,
    "name": "Physics"
  },
  {
    "_id": 3,
    "name": "Chemistry"
  }
]);
```

### Join

```
db.teachers.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "courses taken",
            foreignField: "_id",
            as: "courses_info"
        }
    }
]);
```

### Join with Projection

```
db.teachers.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "courses taken",
            foreignField: "_id",
            as: "courses_info"
        }
    },
    {
        $project: {
            _id: 0,
            name: 1,
            "courses_info.name": 1
        }
    }
]);
```
