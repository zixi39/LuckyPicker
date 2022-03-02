# LuckyPicker
LuckyPicker is a tool that allows you to pick random winners given a tweet URL.

## Before you start
You need will need a "Bearer Token" in order to use this application. 
To acquire a "Bearer Token", you will need to [register](https://developer.twitter.com/en) as a Twitter developer. 
The application will remember your token once you set the token. 
Therefore, you don't need to set it every time.

## Modes
1. Followers: pick winners from the followers of the author of the given tweet.
2. Likes: pick winners from the users that have "liked" the given tweet.
3. Comments: pick winners from the users that have "replied" the given tweet.
4. Retweets: pick winners from the users that have "retweeted" the given tweet.

You can combine different modes together. For example, if both "Likes" and "Comments" are selected, the application will pick winners from users that have "liked" and "replied" to the given tweet.

## Result
The winners displayed on the bottom-right panel of the application are **usernames** of the users that have been picked.

## Known Issues
1. Due to the limitation of Twitter API, the application can only collect replies within 7 days.
2. Due to the limitation of Twitter API, a user with a protected Twitter account will not be collected by the API thus will not be considered as a valid candidate. This is true for all modes **EXCEPT** for the Follower mode.