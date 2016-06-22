# LABORATORIOS UNIVERSITARIOS

Este es un repositorio para los diferentes ejercicios que efectuaremos en Spark / Impala y Solr

  - Instalar git 
```sh
$ sudo yum install git
```
  - Clonar este repo
```sh
$ git clone git@github.com:joaosal/ulabs.git
```

  - Magic

You also need to:
  - Install maven
```sh
$ wget http://mirror.olnevhost.net/pub/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz
```
Afterwards the process is easy

Run the wget command from the dir you want to extract maven too.
run the following to extract the tar,
```sh
tar xvf apache-maven-3.0.5-bin.tar.gz
```
move maven to /usr/local/apache-maven
```sh
mv apache-maven-3.0.5  /usr/local/apache-maven
```
Next add the env variables to your ~/.bashrc file
```sh
export M2_HOME=/usr/local/apache-maven
export M2=$M2_HOME/bin 
export PATH=$M2:$PATH
```
Execute these commands
```sh
source ~/.bashrc
```
Verify everything is working with the following command
```sh
mvn -version
```
### Hadoop

Create directory in HDFS

```sh
$ hadoop fs -mkdir <folder>
```

Copy file to HDFS

```sh
$ hadoop fs -put <file> <directory>
```

### Spark

```sh
$ spark-shell
```

```sh
$ pyspark
```

### Impala / Hive

- Hive

```sh
$ beeline -u jdbc:hive2://localhost:10000
```

- Impala

```sh
$ impala-shell
```

- Install MYSQL
```sh
$ sudo yum install mysql-server
```

- Then to start MYSQL server
```sh
$sudo service mysqld start
```

- To log in to MySQL as the Root User
```sh
$ mysql -u root
```

- Set the root user password for all local domains
```sh
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('new-password');
SET PASSWORD FOR 'root'@'localhost.localdomain' = PASSWORD('new-password');
SET PASSWORD FOR 'root'@'127.0.0.1' = PASSWORD('new-password');
```

Populate DB with script

```sh
mysql> source dbsetup.sql
```
- Verify

```sh
mysql> use dualcore
Database changed
mysql> show tables;
+--------------------+
| Tables_in_dualcore |
+--------------------+
| customers          |
| employees          |
| order_details      |
| orders             |
| products           |
| suppliers          |
+--------------------+
```


### Cloudera Search


### Todos

 - Write Tests
 - Rethink Github Save
 - Add Code Comments

Books
----

[Hadoop Definitive Guide 3rd](https://www.dropbox.com/s/d76kku0iqb7kdqx/OReilly.Hadoop.The.Definitive.Guide.3rd.Edition.May.2012.RETAIL.eBook-ELOHiM.pdf?dl=0)

License
----

MIT


**Free Software, Hell Yeah!**
