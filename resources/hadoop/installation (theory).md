## Hadoop-2 Single Node Cluster Installation

1. Download Hadoop and Java and extract the tar files

2. Modify Hadoop Configuration Files

   - core-site.xml: Give the name node address

   - yarn-site.xml: Give the resource manager address

   - hdfs-site.xml: Give the name and data node directory

   - mapred-site.xml: Give the map reduce framework name

   - Set the java path in hadoop-env.sh, mapred-env.sh, yarn-env.sh

3. Generate ssh key for localhost and copy the public key to the authorized_keys file

4. Format the name node

5. Start all hadoop related services

   ```bash
   start-all.sh
   ```

6. Check the browser web GUI on `http://localhost:19888`

7. List the files in the HDFS

   ```bash
   hadoop fs -ls /
   ```

8. Create a directory in the HDFS

   ```bash
   hadoop fs -mkdir /user
   ```

9. Add a file to the HDFS

   ```bash
   hadoop fs -put /home/username/file.txt /user
   ```

10. Stop all hadoop related services
    ```bash
    stop-all.sh
    ```
