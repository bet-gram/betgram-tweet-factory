drop table if exists metrics;
create table metrics (
	screen_name text primary key,
	follower_count real not null,
	retweet_count real not null,
	weighted_rt_index real not null
);
