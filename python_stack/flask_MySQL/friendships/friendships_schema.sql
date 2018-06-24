# Assignment: friendships
# Karen Clark
# 2018-06-23

DROP DATABASE IF EXISTS  `friendships`;
CREATE DATABASE `friendships`;
USE `friendships`;

CREATE TABLE `users` (
  `id` INT unsigned NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45),
  `last_name` VARCHAR(45),
  `created_at` DATETIME,
  `updated_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;

CREATE TABLE `friendships`(
  `id` INT unsigned NOT NULL AUTO_INCREMENT,
  `user_id` INT unsigned,
  `friend_id` INT unsigned,
  `created_at` DATETIME,
  `updated_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;

ALTER TABLE friendships
ADD CONSTRAINT friendships_users_id_fk
FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE friendships
ADD CONSTRAINT friendships_friends_id_fk
FOREIGN KEY (friend_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE;