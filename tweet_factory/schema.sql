drop table if exists metrics;
drop table if exists geo;
create table metrics (
	screen_name text primary key,
	follower_count real not null,
	retweet_count real not null,
	weighted_rt_index real not null
);
create table geo(
	screen_name text not null,
	tweet_id varchar not null,
	geo text not null,
	primary key (screen_name,tweet_id)
);
