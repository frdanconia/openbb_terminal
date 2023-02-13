```
usage: social [--export {csv,json,xlsx}] [-h]
```

Shows social media corresponding to loaded coin. You can find there name of telegram channel, urls to twitter, reddit, bitcointalk, facebook and
discord.

```
optional arguments:
  --export {csv,json,xlsx}
                        Export dataframe data to csv,json,xlsx file (default: )
  -h, --help            show this help message (default: False)
```

Example:

```
2022 Feb 15, 07:47 (🦋) /crypto/dd/ $ social
          Social Media for Loaded Coin
┌───────────┬───────────────────────────────────┐
│ Metric    │ Value                             │
├───────────┼───────────────────────────────────┤
│ Telegram  │                                   │
├───────────┼───────────────────────────────────┤
│ Twitter   │ https://twitter.com/bitcoin       │
├───────────┼───────────────────────────────────┤
│ Subreddit │ https://www.reddit.com/r/Bitcoin/ │
├───────────┼───────────────────────────────────┤
│ Facebook  │ bitcoins                          │
└───────────┴───────────────────────────────────┘
```
