#create database LibraryManagementSystem;
use LibraryManagementSystem;
#create table admin(id integer unsigned not null auto_increment ,primary key(id),admin_id varchar (10),email_id varchar (50),password varchar (20),phone bigint (10),first_name varchar (15),last_name varchar (15),status boolean, time_stamp datetime default current_timestamp);
#drop table student;
select * from admin;
#create table student(student_id varchar (20),password varchar (30),validity varchar (20),status boolean,due integer (5) default 0);
select * from student;
#drop table student;
#create table teacher(teacher_id varchar (20),password varchar (30),status boolean);
select * from teacher;
#delete from book_log where returned_on='2023-05-06';

#create table book_mas(id integer unsigned not null auto_increment ,primary key(id),book_id varchar (10),book_name varchar (50),book_cat varchar (20),available_qty integer (5),taken_qty integer (5) default 0,created_by varchar (10),created_at datetime default current_timestamp)
#select distinct book_cat from book_mas;
#create table book_log(book_id varchar (10),book_name varchar (50),borrower_id varchar (20),status varchar (10),issued_on date,issued_at time,returned_on date,returned_at time)
select * from book_log;
#drop table book_log;
select * from book_mas;
#SELECT column_name
#FROM INFORMATION_SCHEMA.COLUMNS
#WHERE TABLE_NAME = N'book_log' order by ordinal_position asc;
select distinct borrower_id from book_log where status='BORROWED';
select count(book_name) from book_log where borrower_id='EIE/2020/044';
select book_mas.book_cat from book_mas,book_log where book_mas.book_id=book_log.book_id and book_log.borrower_id='EIE/2020/044';
#update book_mas set taken_qty=5 where book_id='BOOK002';
#ALTER TABLE book_log drop column pay_stat;
#ALTER TABLE book_log add pay_stat varchar (10) default 'UNPAID';
#select distinct student.student_id from student inner join book_log on student.student_id=book_log.borrower_id;
#insert into student values('CE/2020/001','StudentPwd6^','30/06/2026',1,0);
#insert into book_log values('BOOK001','BLUEJ','CE/2020/001','BORROWED','2023-01-08','11:34:22',null,NULL,'2023-05-06','UNPAID');
#insert into book_log values('BOOK004','LET US SQL','CE/2020/001','RETURNED','2023-01-08','11:34:22','2023-05-10',NULL,'2023-05-01','UNPAID');
#update admin set status=1 where admin_id='AD003';