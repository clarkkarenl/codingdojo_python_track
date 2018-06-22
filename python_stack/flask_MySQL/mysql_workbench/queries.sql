-- Assignment: MySQL Workbench
-- Karen Clark
-- 2018-06-21
-- NOTE: I am using DataGrip because MySQL Workbench
-- keeps crashing on my PC

use twitter;

select count(*) from users;
select count(*) from tweets;
select count(*) from faves;

select users.id, users.first_name, tweets.id from users
left join tweets on
  users.id = tweets.user_id;

select users.id, count(tweets.id) from users
left join tweets on
  users.id = tweets.user_id group by users.id;

select users.first_name, count(faves.id) from users
left join faves
    on users.id = faves.user_id;

select count(distinct(user_id)) from faves;

select max(created_at) from faves;

select birthday from users order by birthday desc;

select * from tweets
join users on
tweets.user_id = users.id
where users.birthday = '1975-06-07';