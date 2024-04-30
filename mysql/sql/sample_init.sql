create database indicator;
use indicator;
create table BlockAccess
(
    id      int auto_increment
        primary key,
    date    varchar(30) null,
    control int         null,
    blocked int         null
);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (1, '2024-04-03', 31, 82);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (2, '2024-04-02', 23, 54);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (3, '2024-04-01', 99, 57);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (4, '2024-03-31', 38, 73);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (5, '2024-03-30', 62, 35);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (6, '2024-03-29', 47, 37);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (7, '2024-03-28', 65, 67);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (8, '2024-03-27', 80, 17);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (9, '2024-03-26', 23, 66);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (10, '2024-03-25', 71, 23);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (11, '2024-03-24', 17, 53);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (12, '2024-03-23', 25, 43);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (13, '2024-03-22', 84, 85);
INSERT INTO indicator.BlockAccess (id, date, control, blocked) VALUES (14, '2024-03-21', 85, 75);

use mysql;
create user 'inspire12'@'%' identified by 'abcde12#';
show grants for 'inspire12'@'%';
grant all privileges on indicator.BlockAccess to 'inspire12'@'%';
select host, user from user;
flush privileges;

use indicator;


select date, control, blocked from indicator.BlockAccess;
select sum(control), sum(blocked) from indicator.BlockAccess;