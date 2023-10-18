
docker pull mysql:8.0.26
docker run --name mysql1 -p 3306:3306 -p 33060:33060 -e MYSQL_ROOT_PASSWORD=mysecretpw -d mysql:8.0.26

docker start mysql1

mysql -uroot -pmysecretpw -h 127.0.0.1
mysql> ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY 'mysecretpw';
mysql> CREATE DATABASE darkdemo;
mysql> exit

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
nvm install v14.21.3
nvm use v14.21.3

npm start
mysql -uroot -pmysecretpw -h 127.0.0.1 < init.sql

ngrok http 8090 --domain={your_ngrok_domain} --basic-auth="user:password"
