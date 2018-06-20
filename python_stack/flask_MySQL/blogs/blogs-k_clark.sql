-- Assignment: Blogs
-- Karen Clark
-- 2018-06-18
-- NOTE: MySQL Workbench keeps crashing on my PC
-- I'm using https://app.sqldbm.com instead.

-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;

DROP TABLE `users_comments`;


DROP TABLE `posts_uploads`;


DROP TABLE `comments`;


DROP TABLE `users_permissions`;


DROP TABLE `posts`;


DROP TABLE `blogs`;


DROP TABLE `uploads`;


DROP TABLE `permissions`;


DROP TABLE `users`;


-- ************************************** `uploads`

CREATE TABLE `uploads`
(
 `id`       INT NOT NULL AUTO_INCREMENT ,
 `filename` VARCHAR(255) NOT NULL ,
 `url`      VARCHAR(2083) NOT NULL ,

PRIMARY KEY (`id`)
);


-- ************************************** `permissions`

CREATE TABLE `permissions`
(
 `id`            INT NOT NULL AUTO_INCREMENT ,
 `rename_blog`   TINYINT NOT NULL ,
 `add_posts`     TINYINT NOT NULL ,
 `edit_posts`    TINYINT NOT NULL ,
 `add_comments`  TINYINT NOT NULL ,
 `edit_comments` TINYINT NOT NULL ,
 `upload_files`  TINYINT NOT NULL ,

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


-- ************************************** `blogs`

CREATE TABLE `blogs`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `user_id`    INT NOT NULL ,
 `name`       VARCHAR(255) NOT NULL ,
 `url`        VARCHAR(2083) NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `user_id`),
KEY `fkIdx_81` (`user_id`),
CONSTRAINT `FK_81` FOREIGN KEY `fkIdx_81` (`user_id`) REFERENCES `users` (`id`)
);


-- ************************************** `users_permissions`

CREATE TABLE `users_permissions`
(
 `id`            INT NOT NULL AUTO_INCREMENT ,
 `user_id`       INT NOT NULL ,
 `permission_id` INT NOT NULL ,
 `blog_id`       INT NOT NULL ,
 `role`          VARCHAR(255) NOT NULL ,
 `created_at`    DATETIME NOT NULL ,
 `updated_at`    DATETIME NOT NULL ,

PRIMARY KEY (`id`, `user_id`, `permission_id`, `blog_id`),
KEY `fkIdx_50` (`user_id`),
CONSTRAINT `FK_50` FOREIGN KEY `fkIdx_50` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_54` (`permission_id`),
CONSTRAINT `FK_54` FOREIGN KEY `fkIdx_54` (`permission_id`) REFERENCES `permissions` (`id`),
KEY `fkIdx_74` (`blog_id`, `user_id`),
CONSTRAINT `FK_74` FOREIGN KEY `fkIdx_74` (`blog_id`, `user_id`) REFERENCES `blogs` (`id`, `user_id`)
);


-- ************************************** `posts`

CREATE TABLE `posts`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `blog_id`    INT NOT NULL ,
 `user_id`    INT NOT NULL ,
 `content`    LONGTEXT NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `blog_id`, `user_id`),
KEY `fkIdx_63` (`blog_id`, `user_id`),
CONSTRAINT `FK_63` FOREIGN KEY `fkIdx_63` (`blog_id`, `user_id`) REFERENCES `blogs` (`id`, `user_id`),
KEY `fkIdx_70` (`user_id`),
CONSTRAINT `FK_70` FOREIGN KEY `fkIdx_70` (`user_id`) REFERENCES `users` (`id`)
);


-- ************************************** `posts_uploads`

CREATE TABLE `posts_uploads`
(
 `id`        INT NOT NULL AUTO_INCREMENT ,
 `upload_id` INT NOT NULL ,
 `post_id`   INT NOT NULL ,

PRIMARY KEY (`id`, `upload_id`, `post_id`),
KEY `fkIdx_98` (`upload_id`),
CONSTRAINT `FK_98` FOREIGN KEY `fkIdx_98` (`upload_id`) REFERENCES `uploads` (`id`),
KEY `fkIdx_104` (`post_id`),
CONSTRAINT `FK_104` FOREIGN KEY `fkIdx_104` (`post_id`) REFERENCES `posts` (`id`)
);


-- ************************************** `comments`

CREATE TABLE `comments`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `post_id`    INT NOT NULL ,
 `content`    VARCHAR(255) NOT NULL ,
 `created_at` DATETIME NOT NULL ,
 `updated_at` DATETIME NOT NULL ,

PRIMARY KEY (`id`, `post_id`),
KEY `fkIdx_131` (`post_id`),
CONSTRAINT `FK_131` FOREIGN KEY `fkIdx_131` (`post_id`) REFERENCES `posts` (`id`)
);


-- ************************************** `users_comments`

CREATE TABLE `users_comments`
(
 `id`         INT NOT NULL AUTO_INCREMENT ,
 `user_id`    INT NOT NULL ,
 `comment_id` INT NOT NULL ,

PRIMARY KEY (`id`, `user_id`, `comment_id`),
KEY `fkIdx_123` (`user_id`),
CONSTRAINT `FK_123` FOREIGN KEY `fkIdx_123` (`user_id`) REFERENCES `users` (`id`),
KEY `fkIdx_127` (`comment_id`, `user_id`),
CONSTRAINT `FK_127` FOREIGN KEY `fkIdx_127` (`comment_id`, `user_id`) REFERENCES `comments` (`id`, `user_id`)
);
