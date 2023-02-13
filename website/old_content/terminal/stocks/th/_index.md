---
title: Introduction to Trading Hours
keywords: "markets, trading, hours, stocks, time, global, world, location, open, close, exchange"
date: "2022-05-20"
type: guides
status: publish
excerpt: "An Introduction to the Trading Hours menu, within the Stocks menu. This set of features displays the status of international markets."
geekdocCollapseSection: true
---
This set of features is for checking the operating status of markets globally. To access the Trading Hours features,
enter `th` from the <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/" target="_blank" rel="noreferrer noopener">Stocks</a> menu.
Alternatively, a user can access the submenu with absolute path navigation from anywhere in the Terminal: `/stocks/th`

<a target="_blank" href="https://user-images.githubusercontent.com/46355364/170244188-17ffac5f-3345-4c40-be44-fb5128ad9612.png"><img alt="Trading Hours" src="https://user-images.githubusercontent.com/46355364/170244188-17ffac5f-3345-4c40-be44-fb5128ad9612.png"></a>

## How to use

A symbol is not required to be loaded. Once in the Trading Hours menu, the operation is simple.
Choose from: <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/open/" target="_blank" rel="noreferrer noopener">open</a>,
<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/closed/" target="_blank" rel="noreferrer noopener">closed</a>,
<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/all/" target="_blank" rel="noreferrer noopener">all</a> or
<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/exchange/" target="_blank" rel="noreferrer noopener">exchange</a>.
<a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/holidays/" target="_blank" rel="noreferrer noopener">holidays</a>.

Below, examples are given what these commands display, note that the tables are purposely cut off to keep the
introduction compact.

````
(🦋) /stocks/th/ $ open
                      Open markets
┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃     ┃ name                              ┃ short_name ┃
┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ FRA │ Frankfurt Stock Exchange          │ F          │
├─────┼───────────────────────────────────┼────────────┤
│ STU │ Börse Stuttgart                   │ SG         │
├─────┼───────────────────────────────────┼────────────┤
│ MUN │ Börse München                     │ MU         │
├─────┼───────────────────────────────────┼────────────┤
│ DUS │ Börse Düsseldorf                  │ DU         │
├─────┼───────────────────────────────────┼────────────┤
│ MEX │ Bolsa Mexicana de Valores         │ MX         │
├─────┼───────────────────────────────────┼────────────┤
│ FKA │ Frankfurt Stock Exchange          │ F          │
├─────┼───────────────────────────────────┼────────────┤
│ NYQ │ New York Stock Exchange           │ NYSE       │
├─────┼───────────────────────────────────┼────────────┤
│ VAN │ TSX Venture Exchange              │ V          │
├─────┼───────────────────────────────────┼────────────┤
<continues>

(🦋) /stocks/th/ $ closed
                    Closed markets
┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃     ┃ name                             ┃ short_name ┃
┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ SHZ │ Shenzen Stock Exchange           │ SHZE       │
├─────┼──────────────────────────────────┼────────────┤
│ KSC │ Korea Exchange                   │ KRX        │
├─────┼──────────────────────────────────┼────────────┤
│ KOE │ Korea Exchange                   │ KRX        │
├─────┼──────────────────────────────────┼────────────┤
│ HKG │ Hong Kong Stock Exchange         │ HKEX       │
├─────┼──────────────────────────────────┼────────────┤
│ KLS │ Bursa Malaysia                   │ KLSE       │
├─────┼──────────────────────────────────┼────────────┤
│ ENX │ Euronext                         │ NX         │
├─────┼──────────────────────────────────┼────────────┤
│ TWO │ Taipei Exchange                  │ TWO        │
├─────┼──────────────────────────────────┼────────────┤
│ HAM │ Hamburger Börse                  │ HM         │
├─────┼──────────────────────────────────┼────────────┤
│ TW  │ Taiwan Stock Exchange            │ TWSE       │
├─────┼──────────────────────────────────┼────────────┤
<continues>

(🦋) /stocks/th/ $ all
                         World markets
┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
┃     ┃ name                              ┃ short_name ┃ open  ┃
┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
│ SHZ │ Shenzen Stock Exchange            │ SHZE       │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ KSC │ Korea Exchange                    │ KRX        │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ KOE │ Korea Exchange                    │ KRX        │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ HKG │ Hong Kong Stock Exchange          │ HKEX       │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ KLS │ Bursa Malaysia                    │ KLSE       │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ FRA │ Frankfurt Stock Exchange          │ F          │ True  │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ STU │ Börse Stuttgart                   │ SG         │ True  │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ ENX │ Euronext                          │ NX         │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ TWO │ Taipei Exchange                   │ TWO        │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
│ HAM │ Hamburger Börse                   │ HM         │ False │
├─────┼───────────────────────────────────┼────────────┼───────┤
<continues>
````
Lastly, <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/exchange/" target="_blank" rel="noreferrer noopener">exchange</a>
shows the status of a single venue.

<a target="_blank" href="https://user-images.githubusercontent.com/46355364/170244354-f5ab043d-0290-46ec-ba86-87cc2dc0e47a.png"><img alt="Trading Hours Autocomplete" src="https://user-images.githubusercontent.com/46355364/170244354-f5ab043d-0290-46ec-ba86-87cc2dc0e47a.png"></a>

## Examples
Below an example is given for a symbol and whether that market is open. By calling <a href="https://openbb-finance.github.io/OpenBBTerminal/terminal/stocks/tradinghours/exchange/" target="_blank" rel="noreferrer noopener">exchange</a>
you can obtain more information about the exchange (e.g. enter `BO`)
````
(🦋) /stocks/th/ $ symbol RY.TO

Selected symbol
Symbol:        RY.TO
Name:          ROYAL BANK OF CANADA
Market open:   False

(🦋) /stocks/th/ $ symbol FB2.L

Selected symbol
Symbol:        FB2.L
Name:          LEVERAGE SHARES PUBLIC LIMITED
Market open:   False

(🦋) /stocks/th/ $ exchange BO
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                       ┃ BSE                                                                       ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ name                  │ BSE                                                                       │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ short_name            │ BO                                                                        │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ website               │ https://www.bseindia.com/static/markets/equity/EQReports/tra_trading.aspx │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ market_open           │ 09:15:00                                                                  │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ market_close          │ 15:30:00                                                                  │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ lunchbreak_start      │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ lunchbreak_end        │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ opening_auction_start │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ opening_auction_end   │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ closing_auction_start │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ closing_auction_end   │ None                                                                      │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ timezone              │ Asia/Kolkata                                                              │
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ flag                  │ 🇮🇳
├───────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ open                  │ False                                                                     │
└───────────────────────┴───────────────────────────────────────────────────────────────────────────┘



(🦋) /stocks/th/ $ holidays BATS 2024
         BATS
┏━━━━━━┳━━━━━━━━━━━━━━┓
┃      ┃ Holiday Date ┃
┡━━━━━━╇━━━━━━━━━━━━━━┩
│ 1805 │ 2024-01-01   │
├──────┼──────────────┤
│ 1806 │ 2024-01-15   │
├──────┼──────────────┤
│ 1807 │ 2024-02-19   │
├──────┼──────────────┤
│ 1808 │ 2024-03-29   │
├──────┼──────────────┤
│ 1809 │ 2024-05-27   │
├──────┼──────────────┤
│ 1810 │ 2024-07-04   │
├──────┼──────────────┤
│ 1811 │ 2024-09-02   │
├──────┼──────────────┤
│ 1812 │ 2024-11-28   │
├──────┼──────────────┤
│ 1813 │ 2024-12-25   │
└──────┴──────────────┘

````
