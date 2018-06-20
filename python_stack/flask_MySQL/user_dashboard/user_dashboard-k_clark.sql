-- Assignment: User Dashboard
-- Karen Clark
-- 2018-06-19
-- NOTE: MySQL Workbench keeps crashing on my PC
-- I'm using https://app.sqldbm.com instead.

-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;

DROP TABLE `threads`;


DROP TABLE `users_levels`;


DROP TABLE `messages`;


DROP TABLE `users_permissions`;


DROP TABLE `levels`;


DROP TABLE `permissions`;


DROP TABLE `users`;


-- ************************************** `levels`

CREATE TABLE `levels`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `level`      VARCHAR(8) NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `permissions`

CREATE TABLE `permissions`
(
 `id`               INT NOT NULL AUTO_INCREMENT ,
 `view_all_users`   TINYINT NOT NULL ,
 `add_user`         TINYINT NOT NULL ,
 `edit_user`        TINYINT NOT NULL ,
 `edit_own_profile` TINYINT NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `users`

CREATE TABLE `users`
(
 `id`          INT NOT NULL AUTO_INCREMENT ,
 `email`       VARCHAR(255) NOT NULL ,
 `first_name`  VARCHAR(255) NOT NULL ,
 `last_name`   VARCHAR(255) NOT NULL ,
 `password`    VARCHAR(64) NOT NULL ,
 `description` VARCHAR(255) NOT NULL ,
 `created_at`  DATETIME NOT NULL ,
 `updated_at`  DATETIME NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `users_levels`

CREATE TABLE `users_levels`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `user_id`    INT NOT NULL ,
 `level_id`   INT NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `user_id`, `level_id`),
KEY `fkIdx_67` (`user_id`),
CONSTRAINT `FK_67` FOREIGN KEY `fkIdx_67` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_71` (`level_id`),
CONSTRAINT `FK_71` FOREIGN KEY `fkIdx_71` (`level_id`) REFERENCES `levels` (`id`)
);



-- ************************************** `messages`

CREATE TABLE `messages`
(
 `id`             INT NOT NULL AUTO_INCREMENT ,
 `user_id`        INT NOT NULL ,
 `content`        VARCHAR(255) NOT NULL ,
 `created_at`     DATETIME NOT NULL ,
 `updated_at`     DATETIME NOT NULL ,
 `poster_user_id` INT NOT NULL ,

PRIMARY KEY (`id`, `user_id`),
KEY `fkIdx_44` (`user_id`),
CONSTRAINT `FK_44` FOREIGN KEY `fkIdx_44` (`user_id`) REFERENCES `users` (`id`)
);



-- ************************************** `users_permissions`

CREATE TABLE `users_permissions`
(
 `id`            INT NOT NULL AUTO_INCREMENT ,
 `user_id`       INT NOT NULL ,
 `permission_id` INT NOT NULL ,
 `created_at`    DATETIME NOT NULL ,

PRIMARY KEY (`id`, `user_id`, `permission_id`),
KEY `fkIdx_35` (`user_id`),
CONSTRAINT `FK_35` FOREIGN KEY `fkIdx_35` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_39` (`permission_id`),
CONSTRAINT `FK_39` FOREIGN KEY `fkIdx_39` (`permission_id`) REFERENCES `permissions` (`id`)
);



-- ************************************** `threads`

CREATE TABLE `threads`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `message_id` INT NOT NULL ,
 `user_id`    INT NOT NULL ,
 `created_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `message_id`, `user_id`),
KEY `fkIdx_52` (`message_id`, `user_id`),
CONSTRAINT `FK_52` FOREIGN KEY `fkIdx_52` (`message_id`, `user_id`) REFERENCES `messages` (`id`, `user_id`)
);
