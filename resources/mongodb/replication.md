## MongoDB Replication commands

**First of all, stop the mongod service if it is running already and delete any existing data directories.**

```bash
sudo service mongod stop
sudo systemctl stop mongod
sudo rm -r data/
```

### Create the data directories for the three nodes

```bash
mkdir -p data/db1
mkdir -p data/db2
mkdir -p data/db3
```

### Start the three nodes in separate terminals

```bash
mongod --port 27017 --dbpath data/db1 --replSet rs0
```

```bash
mongod --port 27018 --dbpath data/db2 --replSet rs0
```

```bash
mongod --port 27019 --dbpath data/db3 --replSet rs0
```

### Connect to the node on port 27017

```bash
mongosh --port 27017
```

---

## The following commands are executed in the mongosh shell that you just opened

### Initiate the replica set

```bash
rs.initiate()
```

### Add the other two nodes to the replica set

```bash
rs.add("localhost:27018")
rs.add("localhost:27019")
```

### Check the status of the replica set

```bash
rs.status()
```

If successful, data that is written through the primary node should be replicated across the three nodes.

### Connect to the other two nodes on two separate terminals

```bash
mongosh --port 27018
```

```bash
mongosh --port 27019
```

To read data from the secondary nodes, run the following command in the last two mongosh shells (on port 27018 & 27019) that you opened.

```bash
db.getMongo().setReadPref('secondary')
```
