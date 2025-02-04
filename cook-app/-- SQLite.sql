-- SQLite
create table recipes (
   id          integer primary key,
   name        text not null,
   ingredients text not null
);