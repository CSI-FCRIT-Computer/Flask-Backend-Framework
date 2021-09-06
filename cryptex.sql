
CREATE TABLE IF NOT EXISTS account1 (
	id int(11) NOT NULL AUTO_INCREMENT,
  	username varchar(50) NOT NULL,
  	password varchar(255) NOT NULL,
  	email varchar(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO account1 (id, username, password, email) VALUES (1, 'Edwin Vincent', 'edu', 'edwinvincent.evt@gmail.com');
select * from account1;

CREATE TABLE IF NOT EXISTS books (
  	book varchar(50) NOT NULL,
    author varchar(50) NOT NULL,
    rating int(5) Not NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
INSERT INTO books (book, author, rating) VALUES ("Angels and Demons","Dan Brown",4);
INSERT INTO books (book, author, rating) VALUES ("Sherlock Holmes","Sir Arthur Conan Doyle",4);
INSERT INTO books (book, author, rating) VALUES ("Clifton Chronicles","Jeffery Archer",3);
select * from books;