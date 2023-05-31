![head.png](https://github.com/cafawo/FinancialDataAnalytics/blob/master/figures/head.jpg?raw=1)

# Financial Data Analytics in Python

**Prof. Dr. Fabian Woebbeking**</br>
Assistant Professor of Financial Economics

IWH - Leibniz Institute for Economic Research</br>
MLU - Martin Luther University Halle-Wittenberg

fabian.woebbeking@iwh-halle.de


# Case study: Algorithmic trading

The overarching idea of this case study is to develop a robust software environment with learning objectives geared towards:
* data collection and management,
* financial data analysis,
* risk management and reporting, 
* robust software design and loose coupling.

At the heart of this case is the development and execution of an algorithmic trading strategy. This includes, in particular, the development, back-testing and live paper-trading of a strategy. It is up to the student to decide both on the type strategy as well as its parametrization. 

Guidance is provided in class, through dedicated tutorial sessions and on the course's [GitHub discussion board](https://github.com/cafawo/FinancialDataAnalytics/discussions). Please also note that you find plenty of guidance on the internet, including Wikipedia, YouTube and ChatGPT.

The ultimate deliverable of this case study is something like a funds/strategy proposal that includes the quantitative results from both of the following parts of the case study as well as your economic reasoning and explanations. There are some examples in `casestudy/literature` folder, however, you are free to deviate in terms of style and content. If you want to go above and beyond, feel free to build a web application that displays your performance live, although a PDF file will also do fine.

A secondary but equally important objective is that your code must be robust enough be executed and delivered through GitHub (see the course's README.md). 

**You will NOT be evaluated on the performance of your strategy.** However, you will be evaluated on making a reasonable effort towards developing a valid investment strategy. Randomly placing trades is not a valid investment strategy. Your results must be explained and critically reviewed inside your fund proposal.

# Assignments

## Part 1: Strategy development and back-testing

Development and [back-testing](https://en.wikipedia.org/wiki/Backtesting) of a strategy are two very much related tasks. In fact, it would be very inefficient to think about a strategy, invest for a year and see what happens. Instead we download historical data and test a strategy on it. This allows us to back-test different strategies and their parametrization. Careful with strategies that look too good, back-testing is prone to data mining and over-fitting. Also one must be extremely careful to avoid any look-ahead-bias.

For this case study you have to decide on your own trading strategy, however, some guidance is provided in class and you might want to have a look at [Kakushadze, Z., & Serur, J. A. (2018). 151 Trading Strategies. Z. Kakushadze and JA Serur.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3247865), where you will find plenty ideas. Please note that some ideas therein might simply not be applicable to our underlying asset (cryptocurrencies) and some are more difficult to implement than others.

There is little sense in developing a trading strategy without being able to assess its performance. We will therefore use a benchmark strategy. Said benchmark is a simple [buy and hold](https://en.wikipedia.org/wiki/Buy_and_hold) investment in Bitcoin (BTC). Additionally (only for the first part of the case study) you will implement a given trading strategy that will be used as a second benchmark.

The second benchmark strategy is called *single moving average* (see 3.11 in Kakushadze, Z., & Serur, J. A., 2018). We will use a version that invests long or short in BTC, based on the following signal. Let $t$ denote time measured in the units of your choosing (e.g. 1 minute), with $t = 0$ corresponding to the most recent time. The signal for the strategy is

$$
\text{Signal} = 
\begin{cases} 
\text{`long'} & \text{if } P \ge \text{SMA}(10) \\
\text{`short'} & \text{if } P < \text{SMA}(10)
\end{cases}
$$

where $P$ is the current price of the underlying in $t=0$ and $\text{SMA}(10)$ is the simple moving average with a look-back period of $T = 10$, which is defined as

$$
\text{SMA}(T) = \frac{1}{T} \sum_{t=1}^T P(t).
$$

Strictly speaking there must be a time difference between the information that is available up until $t=0$ and the price in $t > 0$ at which we are able to execute the trading strategy. NEVER use information from $t>0$ and pretend to trade on a price $t \le 0$, this is called look-ahead bias and produces great results that are completely useless! However, for simplification, you might get away with the assumption that you can trade on the price in $t=0$.

Now it is time that you **develop your own strategy**, which you should also document, explain and rationalize in your proposal. Make sure to also explain your economic rationale as well as the limits and risks of your strategy.


## Part 2: Live paper-trading

Back-testing, while useful for development purposes, lends itself to data mining and, therefore, its information value to potential investors can be limited. In other words, no one really cares, without a proper track record. Instead of trading the strategy live with real money - which could be costly - we will simulate the strategy in a paper-trading setup. This can be thought of as an out of sample test of the trading strategy. You are expected to **run the strategy in paper-trading for at least $6$ hours before the submission deadline**, which is a bare minimum, more is better.

Of course we also a brokerage firm that allows us to execute orders via API and keep track of the invested capital. We will use [test.deribit.com](https://test.deribit.com/), one of the largest crypto asset derivatives exchanges. Deribit, kindly enough, provides a free paper-trading API. We will have a dedicated tutorial session on how to set up Deribit's paper-trading. However, you can also find plenty resources on the respective websites.

Now, with a broker at hand, you are all set to test your strategy in a realistic yet safe (no real money lost) environment. Doing so requires you to handle the extraction of live data from Deribit, the generation of trading signals as well as the execution of trades through Deribit's private test API. Finally you also have to collect data on the performance of your account from Deribit.

The results should be presented together with the back-test as part of your proposal. I leave the specifics to you but would expect descriptions of the strategy, its economic rational and performance. On top of that you should provide pictures and reasonable metrics that express the risk and return characteristics of your strategy.


# Repository structure and code

This README is part of your deliverable. You should give some guidance on navigating your repository and how to run your program in this section.

```Bash
casestudy/
├── supplements/  # Relevant literature
│   ├── 151TradingStrategies.pdf  # Inspiration for potential strategies
│   └── Example [...].pdf  # Example strategy proposals
├── README.md  # Case description
├── requirements.yml  # Conda environment
├── run.py  # Replicate the results
├── backtest.py   # The backtest is conducted here
├── data.py       # Deribit API data is downloaded here
├── signals.py    # Trading signals are generated here
└── trading.py    # Trades are executed here
```

The structure, especially the .py files above are just a suggestion. You can structure your code differently if you like (e.g. use notebooks instead of scripts), however, you have to document the structure here in the README.md file.


# Data

The case study will be primarily based on data that you have to acquire from Deribit's API in $1$-minute frequency. You can choose any asset you like, as long as it is traded on Deribit. Here is an example on how to download data from Deribit:

```Python
import time
import requests

url = 'https://test.deribit.com/api/v2/'

msg = {
        "jsonrpc" : "2.0",
        "id" : 833,
        "method" : "public/get_tradingview_chart_data",
        "params" : {
        "instrument_name" : "BTC-PERPETUAL",
        "end_timestamp": int(time.time() * 1000),  # In Epoch milliseconds
        "start_timestamp": int((time.time() - 1e6) * 1000), # In Epoch milliseconds
        "resolution" : "1"  # Minute data
        }
    }
response = requests.post(url, json=msg)
data = response.json()
```

You can add additional data sources as you like. However, the trades have to be executed on Deribit.


# Supplementary materials and support

Some literature (you will find plenty more on the internet):
* *Python for Finance* (Yves Hilpisch): Part IV. Algorithmic Trading
* [*151 Trading Strategies* (Kakushadze and Serur, 2018)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3247865)
* [*Algorithmic Trading Review* (Treleaven, Galas and Lalchand, 2013)](https://dl.acm.org/doi/pdf/10.1145/2500117)
* [*Basics of Algorithmic Trading: Concepts and Examples* (Investopedia, 2023)](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)

You have time to submit your results until the last lecture, how you provision your time until then is up to you. In order to support you on the way we will have tutorial sessions to:

* discuss your strategy ideas and back-test,
* set up the brokerage account and API,
* discuss the final deliverable.

Attendance of these sessions is voluntary yet highly recommended.

In order to ensure that your code runs smoothly on my system, you should run everything in a dedicated Conda environment. A base environment is contained in `requirements.yml`. You are free to install additional packages (make sure that you update requirements.yml thereafter). In order to install the environment on your machine, you can run
```Bash
conda env create -f requirements.yml 
```
In order to run code inside the environment
```Bash
conda activate case-env
# Do your thing ...
conda deactivate
```
If you have installed packages into your active(!) casestudy environment, you have to update requirements.yml with
```Bash
conda env export > requirements.yml
```


# Summary of deliverables

All your codes and results have to be submitted within one GitHub repository as outlined in the [Syllabus (HERE)](https://github.com/cafawo/FinancialDataAnalytics#how-to-submit-your-work). The only exception are large data files (if any), which cannot be hosted on GitHub [(see HERE)](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). We discussed alternatives (e.g. Dropbox) during class.

Code:
* Submit **executable** code.
* You are expected to guide us through your work, e.g. by an appropriate **README.md** file and comments inside your code. 
* Make sure (test) that your code can be executed.
* Use and update the environment in **requirements.yml**.

Strategy proposal:
* For inspiration, have a look at the examples inside casestudy/supplements/
* Summarize your results.
* Show the performance of both back-test and paper-trading.
* Provide risk and return metrics.
* Explain the economic intuition behind your strategy.
* Conclude critically on the limitations and risks of your strategy.


Best of luck!

**If you need more help, post a question on the discussion board or contact the TA for this course.**