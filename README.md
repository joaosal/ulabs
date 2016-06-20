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


### Spark

### Impala

### Cloudera Search


### Todos

 - Write Tests
 - Rethink Github Save
 - Add Code Comments

License
----

MIT


**Free Software, Hell Yeah!**
