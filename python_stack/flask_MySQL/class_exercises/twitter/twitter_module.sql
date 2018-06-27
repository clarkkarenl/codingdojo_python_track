select * from users left join tweets on users.id = tweets.user_id where users.id = 1;

select tweets.tweet from users left join tweets
  on users.id = tweets.user_id
  where users.id = 1;

select tweets.tweet as kobe_tweets from users
left join tweets on users.id = tweets.user_id
where users.id = 1;

select first_name, tweet from users
left join faves on users.id = faves.user_id
left join tweets on faves.tweet_id = tweets.id
where users.id = 2;

select first_name, tweet
from users
left join faves
  on users.id = faves.user_id
left join tweets
  on faves.tweet_id = tweets.id
where users.id = 1 or users.id = 2;

Select users.first_name as followed,
  users2.first_name as follower
from users
left join follows
  on users.id = follows.followed_id
left join users as users2
  on users2.id = follows.follower_id
where users.id = 1;

select * from users where users.id not in (select
follower_id from follows where followed_id = 2)
and users.id != 2;

select users.first_name as user, count(users2.first_name)
as follower_count from users
left join follows
  on users.id = follows.followed_id
left join users as users2
  on users2.id = follows.follower_id
where users.id = 1
group by users.id;

select first_name, tweet from users
left join tweets
  on users.id = tweets.user_id;

select first_name, tweet
from users
join tweets
on users.id = tweets.user_id;
