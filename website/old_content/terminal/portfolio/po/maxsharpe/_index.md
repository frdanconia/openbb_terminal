```
usage: maxsharpe [-p HISTORIC_PERIOD] [-s START_PERIOD] [-e END_PERIOD] [-lr]
                 [--freq {d,w,m}] [-mn MAX_NAN] [-th THRESHOLD_VALUE]
                 [-mt NAN_FILL_METHOD]
                 [-rm {MV,MAD,MSV,FLPM,SLPM,CVaR,EVaR,WR,ADD,UCI,CDaR,EDaR,MDD}]
                 [-r RISK_FREE] [-a SIGNIFICANCE_LEVEL] [-tr TARGET_RETURN]
                 [-tk TARGET_RISK] [-m {hist,ewma1,ewma2}]
                 [-cv {hist,ewma1,ewma2,ledoit,oas,shrunk,gl,jlogo,fixed,spectral,shrink}]
                 [-de SMOOTHING_FACTOR_EWMA] [-v LONG_ALLOCATION]
                 [-vs SHORT_ALLOCATION] [--name NAME] [-h]
```

Maximizes the Risk-Adjusted Return Ratio. The Sharpe ratio is one of the most widely used methods for calculating risk-adjusted return. Modern Portfolio Theory (MPT) states that adding assets to a diversified portfolio that has low correlations can decrease portfolio risk without sacrificing returns. Adding diversification should increase the Sharpe ratio compared to similar portfolios with a lower level of diversification. For this to be true, investors must also accept the assumption that risk is equal to volatility, which is not unreasonable but may be too narrow to be applied to all investments. Post-Modern Portfolio Theory (PMPT) allows to extend the concept of Sharpe ratio to other risk measures like conditional value at risk or conditional drawdown at risk to consider downside risk aversion.

The Risk-Adjusted Return Ratio is calculated as follows:

1. Subtract the risk-free rate from the return of the portfolio. The risk-free rate could be a U.S. Treasury rate or yield, such as the one-year or two-year Treasury yield.

2. Divide the result by the selected risk measure of the portfolio’s excess return.

The Risk-Adjusted Return Ratio can also help explain whether a portfolio's excess returns are due to smart investment decisions or a result of too much risk.
```
optional arguments:
  -p HISTORIC_PERIOD, --period HISTORIC_PERIOD
                        Period to get yfinance data from. Possible frequency
                        strings are: 'd': means days, for example '252d' means
                        252 days 'w': means weeks, for example '52w' means 52
                        weeks 'mo': means months, for example '12mo' means 12
                        months 'y': means years, for example '1y' means 1 year
                        'ytd': downloads data from beginning of year to today
                        'max': downloads all data available for each asset
                        (default: 3y)
  -s START_PERIOD, --start START_PERIOD
                        Start date to get yfinance data from. Must be in
                        'YYYY-MM-DD' format (default: )
  -e END_PERIOD, --end END_PERIOD
                        End date to get yfinance data from. Must be in 'YYYY-
                        MM-DD' format (default: )
  -lr, --log-returns    If use logarithmic or arithmetic returns to calculate
                        returns (default: False)
  --freq {d,w,m}
                        Frequency used to calculate returns. Possible values
                        are: 'd': for daily returns 'w': for weekly returns
                        'm': for monthly returns (default: d)
  -mn MAX_NAN, --maxnan MAX_NAN
                        Max percentage of nan values accepted per asset to be
                        considered in the optimization process (default: 0.05)
  -th THRESHOLD_VALUE, --threshold THRESHOLD_VALUE
                        Value used to replace outliers that are higher to
                        threshold in absolute value (default: 0.3)
  -mt NAN_FILL_METHOD, --method NAN_FILL_METHOD
                        Method used to fill nan values in time series, by
                        default time. Possible values are: 'linear': linear
                        interpolation 'time': linear interpolation based on
                        time index 'nearest': use nearest value to replace nan
                        values 'zero': spline of zeroth order 'slinear':
                        spline of first order 'quadratic': spline of second
                        order 'cubic': spline of third order 'barycentric':
                        builds a polynomial that pass for all points (default:
                        time)
  -rm {MV,MAD,MSV,FLPM,SLPM,CVaR,EVaR,WR,ADD,UCI,CDaR,EDaR,MDD}, --risk-measure {MV,MAD,MSV,FLPM,SLPM,CVaR,EVaR,WR,ADD,UCI,CDaR,EDaR,MDD}
                        Risk measure used to optimize the portfolio. Possible
                        values are: 'MV' : Variance 'MAD' : Mean Absolute
                        Deviation 'MSV' : Semi Variance (Variance of negative
                        returns) 'FLPM' : First Lower Partial Moment 'SLPM' :
                        Second Lower Partial Moment 'CVaR' : Conditional Value
                        at Risk 'EVaR' : Entropic Value at Risk 'WR' : Worst
                        Realization 'ADD' : Average Drawdown of uncompounded
                        returns 'UCI' : Ulcer Index of uncompounded returns
                        'CDaR' : Conditional Drawdown at Risk of uncompounded
                        returns 'EDaR' : Entropic Drawdown at Risk of
                        uncompounded returns 'MDD' : Maximum Drawdown of
                        uncompounded returns (default: MV)
  -r RISK_FREE, --risk-free-rate RISK_FREE
                        Risk-free rate of borrowing/lending. The period of the
                        risk-free rate must be annual (default: 0.00329)
  -a SIGNIFICANCE_LEVEL, --alpha SIGNIFICANCE_LEVEL
                        Significance level of CVaR, EVaR, CDaR and EDaR
                        (default: 0.05)
  -tr TARGET_RETURN, --target-return TARGET_RETURN
                        Constraint on minimum level of portfolio's return
                        (default: -1)
  -tk TARGET_RISK, --target-risk TARGET_RISK
                        Constraint on maximum level of portfolio's risk
                        (default: -1)
  -m {hist,ewma1,ewma2}, --mean {hist,ewma1,ewma2}
                        Method used to estimate the expected return vector
                        (default: hist)
  -cv {hist,ewma1,ewma2,ledoit,oas,shrunk,gl,jlogo,fixed,spectral,shrink}, --covariance {hist,ewma1,ewma2,ledoit,oas,shrunk,gl,jlogo,fixed,spectral,shrink}
                        Method used to estimate covariance matrix. Possible
                        values are 'hist': historical method 'ewma1':
                        exponential weighted moving average with adjust=True
                        'ewma2': exponential weighted moving average with
                        adjust=False 'ledoit': Ledoit and Wolf shrinkage
                        method 'oas': oracle shrinkage method 'shrunk':
                        scikit-learn shrunk method 'gl': graphical lasso
                        method 'jlogo': j-logo covariance 'fixed': takes
                        average of eigenvalues above max Marchenko Pastour
                        limit 'spectral': makes zero eigenvalues above max
                        Marchenko Pastour limit 'shrink': Lopez de Prado's
                        book shrinkage method (default: hist)
  -de SMOOTHING_FACTOR_EWMA, --d-ewma SMOOTHING_FACTOR_EWMA
                        Smoothing factor for ewma estimators (default: 0.94)
  -v LONG_ALLOCATION, --value LONG_ALLOCATION
                        Amount to allocate to portfolio in long positions
                        (default: 1)
  -vs SHORT_ALLOCATION, --value-short SHORT_ALLOCATION
                        Amount to allocate to portfolio in short positions
                        (default: 0.0)
  --name NAME           Save portfolio with personalized or default name
                        (default: MAXSHARPE_0)
  -h, --help            show this help message (default: False)
```

Example:
```
2022 Apr 05, 13:52 (🦋) /portfolio/po/ $ maxsharpe --pie

 [3 Years] Display a maximal return/risk ratio portfolio using
volatility as risk measure

     Weights
┏━━━━━━┳━━━━━━━━━┓
┃      ┃ Value   ┃
┡━━━━━━╇━━━━━━━━━┩
│ AAPL │ 51.47 % │
├──────┼─────────┤
│ AMZN │  0.0 %  │
├──────┼─────────┤
│ BA   │  0.0 %  │
├──────┼─────────┤
│ FB   │  0.0 %  │
├──────┼─────────┤
│ MSFT │  0.0 %  │
├──────┼─────────┤
│ T    │  0.0 %  │
├──────┼─────────┤
│ TSLA │ 48.52 % │
└──────┴─────────┘

Annual (by 252) expected return: 86.15%
Annual (by √252) volatility: 44.22%
Sharpe ratio: 1.9441
```
