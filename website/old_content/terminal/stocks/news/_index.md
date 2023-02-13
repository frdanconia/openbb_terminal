```
usage: news [-n N_NUM] [-d N_START_DATE] [-o] [-s SOURCES [SOURCES ...]] [-h]
```

Using the loaded ticker, the 'news' command will search articles and blogs with the [News API](https://newsapi.org) where the ticker symbol or company name are mentioned. Searches are limited to the past thirty days when using the free API key available. Searches may bring unwanted results when the ticker or business name contains words used as the Dictionary defines. Optional arguments can be added to the command string as described below.

```
optional arguments:
  -n N_NUM, --num N_NUM
                        Number of latest news being printed.
  -d N_START_DATE, --date N_START_DATE
                        The starting date (format YYYY-MM-DD) to search articles from
  -o, --oldest          Show oldest articles first
  -s SOURCES [SOURCES ...], --sources SOURCES [SOURCES ...]
                        Show news only from the sources specified (e.g bbc yahoo.com)
  -h, --help            show this help message
```

Example:
```
2022 Jul 04, 16:54 (🦋) /stocks/ $ news
543 news articles for Apple+Inc. were found since 2022-06-27


                         Three ways to patch your thinking about open-source software security
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Content                                                                                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2022-07-04 20:11:03                                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ What comes to mind when you hear “open source?” Is it a community? Better-quality software? A technology advantage  │
│ that helps companies scale quickly? If so, congratulations. You understand the value developing with open-source    │
│ software can bring to a business…                                                                                    │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ https://siliconangle.com/2022/07/04/three-ways-patch-thinking-open-source-software-security/                        │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


                            HUUUGE, INC.: Informacja o kwartalnych przychodach ze sprzedaży
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Content                                                                                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2022-07-04 18:55:11                                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Spis treści:1. RAPORT BIEŻĄCY2. MESSAGE (ENGLISH VERSION)3. INFORMACJE O PODMIOCIE4. PODPISY OSÓB REPREZENTUJĄCYCH  │
│ SPÓŁKĘ KOMISJA NADZORU FINANSOWEGO <html> <head> </head> <body><font face='Times New...                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ https://www.bankier.pl/wiadomosc/HUUUGE-INC-Informacja-o-kwartalnych-przychodach-ze-sprzedazy-8369875.html          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


                              5 Carpooling Apps to Help You Save Money on Transportation
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Content                                                                                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2022-07-04 16:00:22                                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ When we were kids, our parents told us not to get into cars with strangers, but that’s before we all had            │
│ smartphones in our pockets and the price of gas skyrocketed. Now, if you need to get around, carpooling is a way to │
│ save at the gas pump — or the electric…                                                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ https://www.thepennyhoarder.com/save-money/carpool-apps/                                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
