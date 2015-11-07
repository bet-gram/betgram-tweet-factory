drop table if exists metrics;
drop table if exists entries;
create table metrics (
	screen_name text primary key,
	follower_count integer not null,
	retweet_count integer not null,
	favorite_count integer not null
);
