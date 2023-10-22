## Some Command user in my configuration for mysql in ubuntu 22.4

- Enter `mysql` terminal
```sh
	# 	start running sql
	sudo systemctl start mysql

	sudo mysql
	# if give you access denied use this command
	mysql -u root -p
```
- changes the authentication method to mysql_native_password
```sh
	ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
	# my password for sql server is "password"

	# to go back for default auth method use this 
	ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
```
- To exit
```sh
exit
```
- Create new user in your database a different privledge
```sh
	# host => means you can use this user out of your device
	# localhost => you only allowed to use user in your device
	CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
	# to enter a a user 
	mysql -u username -p
	# it's password is => password

	# create a user that authenticates with caching_sha2_password
	CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';

	# create a user that authenticates with caching_sha2_password but older version
	CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

	# To delete user from your system
	ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

---
- After Creating user grant`تعطي` them `PRIVILEGE`
```sh
#  You can grant multiple privileges to the same user in one command by separating each with a comma
# You can also grant a user privileges globally by entering asterisks (*)

	# change `PRIVILEGE` to any priviledge you want
	GRANT PRIVILEGE ON database.table TO 'username'@'host';


	GRANT CREATE, ALTER, DROP, INSERT, UPDATE, INDEX, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

	# to give user all priviledges
	GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

	# To flush all privileges
	FLUSH PRIVILEGES;
```

- using `mysqladmin`
```sh
# For an additional check, you can try connecting to the database using the mysqladmin tool, 
# which is a client that lets you run administrative commands. For example, this command says 
# to connect as a MySQL user named sammy (-u sammy), prompt for a password (-p), and 
# return the version. Be sure to change sammy to the name of your dedicated MySQL 
# user, and enter that user’s password when prompted:
sudo mysqladmin -p -u sammy version	
```
---
- sql ==> statements are divided into two major categories: 
	1. data definition language (DDL) 
		- DDL statements are used to build and modify the structure of your tables and other objects in the database
	2. data manipulation language (DML).
		- DML statements are used to work with the data in tables.
