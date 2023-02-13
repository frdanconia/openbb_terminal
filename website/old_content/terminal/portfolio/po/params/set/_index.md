```
usage: set -m {maxsharpe,minrisk,maxutil,maxret,maxdiv,maxdecorr,ef,riskparity,relriskparity,hrp,herc,nco} [-h]
```

Select one of the portfolio optimization models

```
optional arguments:
  -m {maxsharpe,minrisk,maxutil,maxret,maxdiv,maxdecorr,ef,riskparity,relriskparity,hrp,herc,nco}, --model {maxsharpe,minrisk,maxutil,maxret,maxdiv,maxdecorr,ef,riskparity,relriskparity,hrp,herc,nco}
                        Frequency used to calculate returns (default: None)
  -h, --help            show this help message (default: False)

```

Example:
```
2022 May 02, 05:51 (🦋) /portfolio/po/params/ $ set maxdecorr

2022 May 02, 05:52 (🦋) /portfolio/po/params/ $ ?
╭──────────────────────────────────────────────────────────────────────────────────────────── Portfolio - Portfolio Optimization - Parameters ────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                                                                         │
│ Portfolio Risk Parameters (.ini or .xlsx)                                                                                                                                                                                               │
│                                                                                                                                                                                                                                         │
│ Loaded file: OpenBB_Parameters_Template v1.0.0.xlsx                                                                                                                                                                                     │
│                                                                                                                                                                                                                                         │
│     file          load portfolio risk parameters                                                                                                                                                                                        │
│     save          save portfolio risk parameters to specified file                                                                                                                                                                      │
│                                                                                                                                                                                                                                         │
│ Model of interest: maxdecorr                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                         │
│     clear         clear model of interest from filtered parameters                                                                                                                                                                      │
│     set           set model of interest to filter parameters                                                                                                                                                                            │
│     arg           set a different value for an argument                                                                                                                                                                                 │
│                                                                                                                                                                                                                                         │
│ Parameters:                                                                                                                                                                                                                             │
│     historic_period         : 3y                                                                                                                                                                                                        │
│     log_returns             : 0                                                                                                                                                                                                         │
│     return_frequency        : d                                                                                                                                                                                                         │
│     max_nan                 : 0.05                                                                                                                                                                                                      │
│     threshold_value         : 0.3                                                                                                                                                                                                       │
│     nan_fill_method         : time                                                                                                                                                                                                      │
│     risk_free               : 0.003                                                                                                                                                                                                     │
│     significance_level      : 0.05                                                                                                                                                                                                      │
│     covariance              : hist                                                                                                                                                                                                      │
│     long_allocation         : 1                                                                                                                                                                                                         │
│                                                                                                                                                                                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── OpenBB Terminal ─╯
```