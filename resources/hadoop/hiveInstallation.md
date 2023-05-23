# Hive installation

Make sure you have Hadoop installed, have it in the path (.bashrc file) and running.

## Modify the following hadoop file
vim <HADOOP_HOME>/etc/hadoop/mapred-site.xml

    <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=${full path of your hadoop distribution directory}</value>
    </property>
    <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=${full path of your hadoop distribution directory}</value>
    </property>
    <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=${full path of your hadoop distribution directory}</value>
    </property>

## Download mysql

    sudo apt install mysql-server

## Download Hive

    curl https://dlcdn.apache.org/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz > apache-hive-2.3.9-bin.tar.gz
    tar -xzf apache-hive-2.3.9-bin.tar.gz

## Download MySQL Jar file into the lib folder in the hive directory.

    curl https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar > mysql-connector-java-8.0.33.jar

## Create the hive-site.xml file

    touch hive-site.xml

Insert the following into the file

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
    <configuration>

    <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost/metastore?createDatabaseIfNotExist=true</value>
    </property>


    <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
    </property>

    <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>root</value>
    </property>

    <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>root</value>
    </property>
    <property>
    <name>hive.metastore.schema.verification</name>
    <value>false</value>
    </property>
    </configuration>

## Create the metastore database in mysql

    bin/schematool -dbType mysql -initSchema

## View metadata in mysql

    mysql -u root -p
    show databases;
    use metastore;
    show tables;

## Start hive
    bin/hive

## Create a database
    create database test;
    use test;
    create table test.emp (id int, name string, salary double) row format delimited fields terminated by ',';

## Insert data into the table
    insert into test.emp values (1, 'A', 1000), (2, 'B', 2000), (3, 'C', 3000);

## View the data
    select * from test.emp;
