-- Assignment: Books
-- Karen Clark
-- 2018-06-18
-- NOTE: MySQL Workbench keeps crashing on my PC
-- I'm using https://app.sqldbm.com instead.

-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;

DROP TABLE `favorites`;


DROP TABLE `books`;


DROP TABLE `users`;



-- ************************************** `books`

CREATE TABLE `books`
(
 `id`           INT NOT NULL AUTO_INCREMENT ,
 `title`        VARCHAR(255) NOT NULL ,
 `author`       VARCHAR(255) NOT NULL ,
 `publish_date` DATETIME NOT NULL ,
 `created_at`   DATETIME NOT NULL ,
 `updated_at`   DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);





-- ************************************** `users`

CREATE TABLE `users`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `first_name` VARCHAR(255) NOT NULL ,
 `last_name`  VARCHAR(255) NOT NULL ,
 `email`      VARCHAR(255) NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);





-- ************************************** `favorites`

CREATE TABLE `favorites`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `user_id`    INT NOT NULL ,
 `book_id`    INT NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `user_id`, `book_id`),
KEY `fkIdx_24` (`user_id`),
CONSTRAINT `FK_24` FOREIGN KEY `fkIdx_24` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_28` (`book_id`),
CONSTRAINT `FK_28` FOREIGN KEY `fkIdx_28` (`book_id`) REFERENCES `books` (`id`)
);
