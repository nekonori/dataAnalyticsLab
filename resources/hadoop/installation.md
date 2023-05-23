# Hadoop-2 Single Node Cluster Creation Installation
															
Download Hadoop and Java (11 is recommended | instructions for Java installation not included)
  curl https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz > hadoop
  tar -xzvf hadoop

sudo apt-get install vim (Install USER Friendly Editer)

 vim ~/.bashrc (Set the java Path in your Home Path)

export JAVA_HOME=<enter your jdk path here e.g. "/user/alice/jdk1.8.0_202">
export PATH=HOME/bin:JAVA_HOME/bin:PATH

 source .bashrc (Execute the bashrc file)
 echo JAVA_HOME (Check the java path)

=========================================================================================================================================


2. Modify Hadoop Configuration Files
NAMENODE ----> core-site.xml
RESOURCE MANGER ----> mapperd-site.xml
SECONDARYNAMENODE ---->
DATANODE ----> slaves
NODEMANGER ----> slaves & yarn-site.xml


 vim etc/hadoop/core-site.xml

<property>
<name>fs.default.name</name>
<value>hdfs://localhost:50000</value>
</property>

 vim etc/hadoop/yarn-site.xml

<property>
<name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name> <value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
<property>
<description>The hostname of the RM.</description>
<name>yarn.resourcemanager.hostname</name>
<value>localhost</value>
</property>
<property>
<description>The address of the applications manager interface in the RM.</description>
<name>yarn.resourcemanager.address</name>
<value>localhost:8032</value>
</property>

 vim etc/hadoop/hdfs-site.xml

<property>
<name>dfs.namenode.name.dir</name>
<value>/home/pragadeshbs/hadoop-dir/namenode-dir</value>
</property>
<property>
<name>dfs.datanode.data.dir</name>
<value>/home/pragadeshbs/hadoop-dir/datanode-dir</value>
</property>

 vim etc/hadoop/mapred-site.xml

<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>

Enter your Java path in the following files
 vim etc/hadoop/hadoop-env.sh
export JAVA_HOME=/user/alice/jdk1.8.0_202

 vim etc/hadoop/mapred-env.sh
export JAVA_HOME=/user/alice/jdk1.8.0_202

 vim etc/hadoop/yarn-env.sh
export JAVA_HOME=/user/alice/jdk1.8.0_202

 vim etc/hadoop/slaves
localhost

Install the ssh key
(Generates, Manages and Converts Authentication keys)
 sudo apt-get install openssh-server
 ssh-keygen -t rsa
(Setup passwordless ssh to localhost and to slaves )
 cd .ssh
 ls
 cat id_rsa.pub >> authorized_keys (copy the .pub)
(Copy the id_rsa.pub from NameNode to authorized_keys in all machines)
 ssh localhost
(Asking No Password )

=========================================================================================================================================


3. Format NameNode
 cd hadoop-2.9.1
 bin/hadoop namenode -format (Your Hadoop File System Ready)

=========================================================================================================================================

4. Start All Hadoop Related Services
 sbin/start-all.sh
(Starting Daemon’s For DFS & YARN)
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager


(check the Browser Web GUI )
Hadoop Web GUI -> http://localhost:8088/
Node manager info -> http://localhost:8042/
HDFS -> http://localhost:9870/


=========================================================================================================================================

5.Stop All Hadoop and Yarn Related Services
 sbin/stop-all.sh
