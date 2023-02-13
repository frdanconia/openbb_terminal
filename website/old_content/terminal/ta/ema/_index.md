```
usage: ema [-l N_LENGTH] [-o N_OFFSET] [--export {csv,json,xlsx}] [-h]
```

The Exponential Moving Average is a staple of technical analysis and is used in countless technical indicators. In a Simple Moving Average, each
value in the time period carries equal weight, and values outside of the time period are not included in the average. However, the Exponential Moving
Average is a cumulative calculation, including all data. Past values have a diminishing contribution to the average, while more recent values have a
greater contribution. This method allows the moving average to be more responsive to changes in the data.

```
optional arguments:
  -l N_LENGTH, --length N_LENGTH
                        Window lengths. Multiple values indicated as comma separated values. (default: [20, 50])
  -o N_OFFSET, --offset N_OFFSET
                        offset (default: 0)
  --export {csv,json,xlsx}
                        Export dataframe data to csv,json,xlsx file (default: )
  -h, --help            show this help message (default: False)
```

![ema](https://user-images.githubusercontent.com/46355364/154310578-6f4a51a8-3667-497c-9c50-7ff16e256fb6.png)
