-- Assignment: Normalization (Optional)
-- Karen Clark
-- 2018-06-19
-- NOTE: MySQL Workbench keeps crashing on my PC
-- I'm using https://app.sqldbm.com instead.

-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;

DROP TABLE `students_interests`;


DROP TABLE `students_dojos`;


DROP TABLE `students`;


DROP TABLE `interests`;


DROP TABLE `dojos`;


-- ************************************** `students`

CREATE TABLE `students`
(
 `id`              INT NOT NULL AUTO_INCREMENT ,
 `name`            VARCHAR(255) NOT NULL ,
 `address1`        VARCHAR(255) NOT NULL ,
 `address2`        VARCHAR(255) NOT NULL ,
 `city`            VARCHAR(255) NOT NULL ,
 `state_province`  VARCHAR(64) NOT NULL ,
 `zip_postal_code` VARCHAR(10) NOT NULL ,
 `country`         VARCHAR(64) NOT NULL ,
 `created_at`      DATETIME NOT NULL ,
 `updated_at`      DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `interests`

CREATE TABLE `interests`
(
 `id`       INT NOT NULL AUTO_INCREMENT ,
 `interest` VARCHAR(255) NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `dojos`

CREATE TABLE `dojos`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `name`       VARCHAR(255) NOT NULL ,
 `location`   VARCHAR(255) NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `students_interests`

CREATE TABLE `students_interests`
(
 `id`          INT NOT NULL AUTO_INCREMENT ,
 `interest_id` INT NOT NULL ,
 `student_id`  INT NOT NULL ,
 `created_at`  DATETIME NOT NULL ,
 `updated_at`  DATETIME NOT NULL ,

PRIMARY KEY (`id`, `interest_id`, `student_id`),
KEY `fkIdx_61` (`interest_id`),
CONSTRAINT `FK_61` FOREIGN KEY `fkIdx_61` (`interest_id`) REFERENCES `interests` (`id`),
KEY `fkIdx_83` (`student_id`),
CONSTRAINT `FK_83` FOREIGN KEY `fkIdx_83` (`student_id`) REFERENCES `students` (`id`)
);



-- ************************************** `students_dojos`

CREATE TABLE `students_dojos`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `dojo_id`    INT NOT NULL ,
 `student_id` INT NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `dojo_id`, `student_id`),
KEY `fkIdx_34` (`dojo_id`),
CONSTRAINT `FK_34` FOREIGN KEY `fkIdx_34` (`dojo_id`) REFERENCES `dojos` (`id`),
KEY `fkIdx_77` (`student_id`),
CONSTRAINT `FK_77` FOREIGN KEY `fkIdx_77` (`student_id`) REFERENCES `students` (`id`)
);
