```
usage: combine [-d {wp}] [-c COLUMNS] [-h]
```

Makes it possible to add a column to a different dataset.

```
optional arguments:
  -d {wp}, --dataset {wp}
                        Dataset to add columns to (default: None)
  -c COLUMNS, --columns COLUMNS
                        The columns we want to add <dataset.column>,<datasetb.column2> (default: None)
  -h, --help            show this help message (default: False)
```

Example:
```
2022 May 31, 04:54 (🦋) /econometrics/ $ load nile

2022 May 31, 04:54 (🦋) /econometrics/ $ load nile -a nile_2

2022 May 31, 04:54 (🦋) /econometrics/ $ combine nile -c nile_2.volume

2022 May 31, 04:55 (🦋) /econometrics/ $ show nile

  Dataset nile | Showing 10 of 100 rows  
┏━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃   ┃ year    ┃ volume  ┃ nile_2_volume ┃
┡━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 0 │ 1871.00 │ 1120.00 │ 1120.00       │
├───┼─────────┼─────────┼───────────────┤
│ 1 │ 1872.00 │ 1160.00 │ 1160.00       │
├───┼─────────┼─────────┼───────────────┤
│ 2 │ 1873.00 │ 963.00  │ 963.00        │
├───┼─────────┼─────────┼───────────────┤
│ 3 │ 1874.00 │ 1210.00 │ 1210.00       │
├───┼─────────┼─────────┼───────────────┤
│ 4 │ 1875.00 │ 1160.00 │ 1160.00       │
├───┼─────────┼─────────┼───────────────┤
│ 5 │ 1876.00 │ 1160.00 │ 1160.00       │
├───┼─────────┼─────────┼───────────────┤
│ 6 │ 1877.00 │ 813.00  │ 813.00        │
├───┼─────────┼─────────┼───────────────┤
│ 7 │ 1878.00 │ 1230.00 │ 1230.00       │
├───┼─────────┼─────────┼───────────────┤
│ 8 │ 1879.00 │ 1370.00 │ 1370.00       │
├───┼─────────┼─────────┼───────────────┤
│ 9 │ 1880.00 │ 1140.00 │ 1140.00       │
└───┴─────────┴─────────┴───────────────┘
```