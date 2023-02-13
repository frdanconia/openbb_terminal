```text
usage: decompose [-m] [--export {csv,json,xlsx}] [-h]
```

This type of forecasting attempts to separate and index factors thought to have meaningful impact on the otherwise random movements in stock prices.

Decompose time series as:

- Additive Time Series = Level + CyclicTrend + Residual + Seasonality
- Multiplicative Time Series = Level *CyclicTrend*
Residual * Seasonality

For a detailed research paper discussing analysis of the Indian Auto Sector, download the PDF here: <https://www.researchgate.net/publication/290263806_Decomposition_of_Time_Series_Data_of_Stock_Markets_and_its_Implications_for_Prediction_-_An_Application_for_the_Indian_Auto_Sector>

"This will help in stock selection in the following ways. First, it will indicate the  overall trend of  the sector,  hence the  stock price,  and  help in  taking  a  position. Second, if  seasonality patterns can  be seen, then during which month which sector and hence which stock should be a good buy, can be  inferred. Third, the random component will throw some light on the volatility pattern of the sector and hence the stock. This decomposition will indicate which of the three components are stronger and can shed further light on the efficient market hypothesis. The  decomposition  will  bring  out  the  overall macroeconomic characteristic of a sector, which affects the fundamentals of a company."

```
optional arguments:
  -m, --multiplicative  decompose using multiplicative model instead of additive (default: False)
  --export {csv,json,xlsx}
                        Export dataframe data to csv,json,xlsx file (default: )
  -h, --help            show this help message (default: False)
```

Example:

```
2022 Feb 16, 11:06 (🦋) /stocks/qa/ $ decompose

Time-Series Level is 2660.84
Strength of Trend: 0.0000
Strength of Seasonality: 0.0032
```

![decompose](https://user-images.githubusercontent.com/46355364/154306626-1c5ad11e-a2e9-4107-9aec-5cf18da5358e.png)
