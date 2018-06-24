# Assignment: friendships
# Karen Clark
# 2018-06-23

SELECT
  users.first_name,
  users.last_name,
  users2.first_name AS friend_first_name,
  users2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON friendships.friend_id = users.id
LEFT JOIN users AS users2 ON friendships.user_id = users2.id
ORDER BY users.last_name, friend_last_name ASC;