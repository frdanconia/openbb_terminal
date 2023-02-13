```
usage: events [-c COUNTRY] [-s START_DATE] [-e END_DATE] [-d SPEC_DATE] [-i {high,medium,low,all}]
              [--categories {employment,credit,balance,economic_activity,central_banks,bonds,inflation,confidence_index}] [-h] [--export EXPORT] [--raw] [-l LIMIT]
              [--source {Nasdaq,Investing}]

Economic calendar. If no start or end dates, default is the current day.

Note that using the Nasdaq flag is preferred due to issues with the investing.com api endpoints.
```
optional arguments:
  -c COUNTRY, --country COUNTRY
                        Display calendar for specific country. Single countries should be separated with commas.(default: )
  -s START_DATE, --start START_DATE
                        The start date of the data (format: YEAR-MONTH-DAY, i.e. 2010-12-31) (default: 2022-10-20)
  -e END_DATE, --end END_DATE
                        The start date of the data (format: YEAR-MONTH-DAY, i.e. 2010-12-31) (default: 2022-10-20)
  -d SPEC_DATE, --date SPEC_DATE
                        Get a specific date for events. Overrides start and end dates. (default: None)
  -i {high,medium,low,all}, --importance {high,medium,low,all}
                        [Investing only] Event importance classified as high, medium, low or all. (default: None)
  --categories {employment,credit,balance,economic_activity,central_banks,bonds,inflation,confidence_index}
                        [INVESTING source only] Event category. (default: None)
  -h, --help            show this help message (default: False)
  --export EXPORT       Export raw data into csv, json, xlsx (default: )
  --raw                 Flag to display raw data (default: False)
  -l LIMIT, --limit LIMIT
                        Number of entries to show in data. (default: 100)
  --source {Nasdaq,Investing}
                        Data source to select from (default: Nasdaq)
```

Example:
```
2022 Oct 20, 15:19 (🦋) /economy/ $ events -c united_kingdom,spain -s 2022-10-20 -e 2022-11-05 -l 15

                                                Economic Calendar
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Time (GMT) ┃ Country        ┃ Event                              ┃ actual ┃ consensus ┃ previous ┃ Date       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 04:40      │ Spain          │ Spanish 3-Year Bonos Auction       │ 2.663% │ -         │ 1.416%   │ 2022-10-20 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 04:40      │ Spain          │ Spanish 7-Year Obligacion Auction  │ 3.247% │ -         │ 1.550%   │ 2022-10-20 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 19:01      │ United Kingdom │ GfK Consumer Confidence            │ -      │ -52       │ -49      │ 2022-10-20 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Core Retail Sales                  │ -      │ -0.3%     │ -1.6%    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Core Retail Sales                  │ -      │ -4.1%     │ -5.0%    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Public Sector Net Borrowing        │ -      │ 12.30B    │ 11.06B   │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Public Sector Net Cash Requirement │ -      │ -         │ 5.321B   │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Retail Sales                       │ -      │ -5.0%     │ -5.4%    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 02:00      │ United Kingdom │ Retail Sales                       │ -      │ -0.5%     │ -1.6%    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 04:30      │ United Kingdom │ BoE Consumer Credit                │ -      │ -         │ 1.077B   │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 04:30      │ United Kingdom │ M4 Money Supply                    │ -      │ -         │ -0.2%    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 04:30      │ United Kingdom │ Mortgage Approvals                 │ -      │ 62.00K    │ 74.34K   │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 04:30      │ United Kingdom │ Mortgage Lending                   │ -      │ 4.90B     │ 6.14B    │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 15:30      │ United Kingdom │ CFTC GBP speculative net positions │ -      │ -         │ -39.2K   │ 2022-10-21 │
├────────────┼────────────────┼────────────────────────────────────┼────────┼───────────┼──────────┼────────────┤
│ 14:00      │ United Kingdom │ BoE MPC Member Mann                │ -      │ -         │ -        │ 2022-10-22 │
└────────────┴────────────────┴────────────────────────────────────┴────────┴───────────┴──────────┴────────────┘
```
