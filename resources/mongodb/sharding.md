## Commands to enable MongoDB sharding on localhost

**First of all, stop the mongod service if it is running already and delete any existing data directories.**

```bash
sudo service mongod stop
sudo systemctl stop mongod
sudo rm -r data/
```

### Create the data directories for the config server and the two shards

```bash
mkdir -p data/configdb
mkdir -p data/db1
mkdir -p data/db2
```

## **You will need to open EIGHT seperate terminal windows/tabs for the following steps.**

Each of the following commands will also include instructions on which terminal to run them in.

### [Terminal 1] Start the config server</span>

```bash
mongod --configsvr --replSet config --dbpath data/configdb
```

### [Terminal 2] Connect to the config server

```bash
mongosh --port 27019
```

### [Terminal 2 (within mongosh)] Initiate the config server replica set

```bash
rs.initiate()
```

### [Terminal 3] Start the first shard

```bash
mongod --shardsvr --replSet shard1 --dbpath data/db1 --port 27010
```

### [Terminal 4] Connect to the first shard

```bash
mongosh --port 27010
```

### [Terminal 4 (within mongosh)] Initiate the first shard replica set

```bash
rs.initiate()
```

### [Terminal 5] Start the second shard

```bash
mongod --shardsvr --replSet shard2 --dbpath data/db2 --port 27011
```

### [Terminal 6] Connect to the second shard

```bash
mongosh --port 27011
```

### [Terminal 6 (within mongosh)] Initiate the second shard replica set

```bash
rs.initiate()
```

### [Terminal 7] Start the mongos router

```bash
mongos --configdb config/127.0.0.1:27019
```

### [Terminal 8] Connect to the mongos router

```bash
mongosh
```

### [Terminal 8 (within mongosh)] Add the shards to the cluster

```bash
sh.addShard("shard1/localhost:27010")
sh.addShard("shard2/localhost:27011")
```

### [Terminal 8 (within mongosh)] Enable sharding on the database

```bash
sh.enableSharding("populations")
```

### [Terminal 8 (within mongosh)] Enable sharding on the collection

```bash
sh.shardCollection("populations.cities", { "country": "hashed" })
```

### [Terminal 8 (within mongosh)] Switch to the database

```bash
use populations
```

### [Terminal 8 (within mongosh)] Insert some data

```bash
db.cities.insertMany([
    {"name": "Seoul", "country": "South Korea", "continent": "Asia", "population": 25.674 },
    {"name": "Mumbai", "country": "India", "continent": "Asia", "population": 19.980 },
    {"name": "Lagos", "country": "Nigeria", "continent": "Africa", "population": 13.463 },
    {"name": "Beijing", "country": "China", "continent": "Asia", "population": 19.618 },
    {"name": "Shanghai", "country": "China", "continent": "Asia", "population": 25.582 },
    {"name": "Osaka", "country": "Japan", "continent": "Asia", "population": 19.281 },
    {"name": "Cairo", "country": "Egypt", "continent": "Africa", "population": 20.076 },
    {"name": "Tokyo", "country": "Japan", "continent": "Asia", "population": 37.400 },
    {"name": "Karachi", "country": "Pakistan", "continent": "Asia", "population": 15.400 },
    {"name": "Dhaka", "country": "Bangladesh", "continent": "Asia", "population": 19.578 },
    {"name": "Rio de Janeiro", "country": "Brazil", "continent": "South America", "population": 13.293 },
    {"name": "São Paulo", "country": "Brazil", "continent": "South America", "population": 21.650 },
    {"name": "Mexico City", "country": "Mexico", "continent": "North America", "population": 21.581 },
    {"name": "Delhi", "country": "India", "continent": "Asia", "population": 28.514 },
    {"name": "Buenos Aires", "country": "Argentina", "continent": "South America", "population": 14.967 },
    {"name": "Kolkata", "country": "India", "continent": "Asia", "population": 14.681 },
    {"name": "New York", "country": "United States", "continent": "North America", "population": 18.819 },
    {"name": "Manila", "country": "Philippines", "continent": "Asia", "population": 13.482 },
    {"name": "Chongqing", "country": "China", "continent": "Asia", "population": 14.838 },
    {"name": "Istanbul", "country": "Turkey", "continent": "Europe", "population": 14.751 }
])
```

### [Terminal 8 (within mongosh)] Check the sharding status

```bash
sh.status()
db.cities.getShardDistribution()
db.cities.find().explain()
db.cities.find({"continent": "Europe"}).explain()
db.cities.find({"country": "Japan"}).explain()
```
