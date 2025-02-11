## SDSS Computing Studies Python Assignment
### Assignment #xx (Total Marks xx)

Objectives:
* Define a table in a database
* Define a record in a table
* Determine the relation between a record and a row


Writing your data/variables to a file is a quick way of putting data in non-volatile storage, but it is not very efficient.  Think about how many people play an MMORPG - if everyone's data was constantly being written/read from file every time that a player entered or left the game, that would be a lot of disk reading/writing and it would be very slow.  The same would happen with websites that store user or game data.  Not very efficient.

SQL Databases (Structured Query Languages) have become the standard for storing data in a way that is scalable (works for large numbers) as well as fast, although it's like learning a new language in many ways.  We will be looking at SQL databases to see how we can create new data sets (called tables), read from them, search them, update existing entries or add new entries.

We will be using a basic version that connects to a file based database using SQLite3.  Complete documentation is available at https://www.tutorialspoint.com/sqlite/sqlite_python.htm, but you may have more success starting with simple code snippets or tutorials

The basic way to connect to a database is through a command prompt.  We can connect to our database using the command:

```
.\sqlite3 <filename>

example:
.\sqlite3 dbase.db
```

Once you connect, you will be looking at a command prompt. Some of the important commands you can do at this prompt include:

```
.tables
.quit
```

We can also issue queries/commands to the database, but note that each command needs to end with a semicolon (;).  If you don't put a semi colon in, it will let you keep typing longer commands over multiple lines until you put in the semicolon.

Some of the commands we want to experiment with today include:
```
.tables
.schema customers;

```

```
select name from sqlite_master where type='table';
```
```
PRAGMA table_info(customers);
```
```
create table if not exists customers (
    id integer primary key autoincrement,
    name tinytext,
    email tinytext,
    cnum int);
```
```
select name from customers
select name,cnum from customers
select name from customers where cnum > 10
select name from customers order by name asc
select * from customers order by cnum desc
```
```
update customers set email='bassist@monkees.ca',cnum=80 where name='Peter Nesmith'
update customers set cnum=10 where email='miley@cyrus.com'
```
```
insert into customers (name,email,cnum) values ('Benjamin Tantalus','benjamin@tantalus.com',1000)
```
```
delete from customers where email='Miley Cyrus'
```

Assignment:

Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.

