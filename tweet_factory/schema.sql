drop table if exists metrics;
drop table if exists tweets;
create table metrics(
	screen_name text primary key,
	follower_count real not null,
	retweet_count real not null,
	weighted_rt_index real not null
);
create table tweets(
	screen_name text not null,
	tweet_id text not null,
	primary key (screen_name,tweet_id)
);
