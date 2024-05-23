# 0x0D. SQL - Introduction

## Learning Objectives
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are subqueries
- How to use MySQL functions

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on `Ubuntu 20.04 LTS` using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## Tasks
|File| Description|
|---|---|
|`0-list_databases.sql`| Write a script that lists all databases of your MYSQL server|
|`1-create_database_if_missing.sql`| Write a script that creates a database `hbtn_0c+0` in your MYSQL server; ( -> If the database already exists, your script should not fail; -> You are not allowed to use the `SELECT` or `SHOW` statements)|
|`2-remove_database.sql`|Write a script that deletes the database `hbtn+0c+0` in your MYSQL server (-> If the database does not exist, your script should not fail; -> you are not allowed to use the `select` and `SHOW` statements)|
