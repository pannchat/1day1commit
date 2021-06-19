BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(3,'lee','lee@naver.com','010-1234-1234','lee.com','2021-06-17 21:34:25');
INSERT INTO "users" VALUES(4,'cho','cho@naver.com','010-4321-1234','cho.com','2021-06-17 21:34:25');
INSERT INTO "users" VALUES(5,'yoo','yoo@naver.com','010-0000-0000','yoo.com','2021-06-17 21:34:25');
COMMIT;
