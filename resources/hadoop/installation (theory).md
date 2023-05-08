## Hadoop-2 Single Node Cluster Installation

1. Download Hadoop and Java and extract the tar files

2. Set the JAVA_HOME in the .bashrc file

3. Modify Hadoop Configuration Files

   - core-site.xml: Give the name node address

   - yarn-site.xml: Give the resource manager address

   - hdfs-site.xml: Give the name and data node directory

   - mapred-site.xml: Give the map reduce framework name

   - Set the java path in hadoop-env.sh, mapred-env.sh, yarn-env.sh

4. Generate ssh key for localhost and copy the public key to the authorized_keys file

5. Format the name node

6. Start all hadoop related services

   ```bash
   start-all.sh
   ```

7. Check the browser web GUI on `http://localhost:19888`

8. List the files in the HDFS

   ```bash
   hadoop fs -ls /
   ```

9. Create a directory in the HDFS

   ```bash
   hadoop fs -mkdir /user
   ```

10. Add a file to the HDFS

    ```bash
    hadoop fs -put /home/username/file.txt /user
    ```

11. Stop all hadoop related services
    ```bash
    stop-all.sh
    ```
