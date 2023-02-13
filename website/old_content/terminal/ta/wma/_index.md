```
usage: wma [-l N_LENGTH] [-o N_OFFSET] [--export {csv,json,xlsx}] [-h]
```

A Weighted Moving Average puts more weight on recent data and less on past data. This is done by multiplying each bar’s price by a weighting factor.
Because of its unique calculation, WMA will follow prices more closely than a corresponding Simple Moving Average.

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

![wma](https://user-images.githubusercontent.com/46355364/154312618-43430406-97c1-4740-87be-2414de9a1c06.png)
