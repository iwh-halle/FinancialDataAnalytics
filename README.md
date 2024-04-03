[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SAilgt2b)
![head.png](figures/head.jpg)

# Financial Data Analytics in Python 2024

**Prof. Dr. Fabian Woebbeking**</br>
Assistant Professor of Financial Economics

IWH - Leibniz Institute for Economic Research</br>
MLU - Martin Luther University Halle-Wittenberg

fabian.woebbeking@iwh-halle.de


**Birte Winter**</br>
PhD Candidate, Teaching Assistant (TA)

IWH - Leibniz Institute for Economic Research</br>

birte.winter@iwh-halle.de


## Course Description

This course is designed to provide students with a hands-on understanding of the use of data science techniques in the field of finance. Students will learn how to collect, clean, and analyze financial data using Python, SQL and other tools. Topics will include financial data visualization, time series analysis and statistical modeling. Students will work on real-world projects to apply their knowledge to financial data.

## Schedule

This course consists of both lectures and accompanying tutorial sessions. The schedule and rooms are announced on Stud.IP, see important links below.

**Lectures and tutorials start as scheduled cum tempore ($t + 15$ minutes)!**

## Prerequisites

* Strong interest and pre-knowledge in financial economics
* Basic knowledge of programming (preferably Python) and statistics
* All the software used during this course are open-source and/or free, this includes:
    * Python
      * [GitHub Codespaces](https://github.com/features/codespaces)
      * [Anaconda distribution](https://www.anaconda.com/products/distribution)
      * ... whatever works for you
    * Git: https://git-scm.com/
    * GitHub: https://skills.github.com/

## Important links

* [Course repository](https://github.com/iwh-halle/FinancialDataAnalytics)
* [GitHub classroom](https://classroom.github.com/a/SAilgt2b)
* [Stud.IP page](https://studip.uni-halle.de/dispatch.php/course/details?sem_id=5a9defd4ce9b514471199574c12ee710&again=yes)


## Materials

All materials are hosted as a Git repository on GitHub.

```bash
FinancialDataAnalytics/
├── cases/  # Case description and supplements
│   └── ...  
├── figures/  # Figures used in slides.ipynb
│   └── ...  
├── homework/  # Homework assignments and solutions
│   └── ...  
├── src/  # Python helper scripts (.py)
│   └── ...  
├── README.md  # Syllabus (this file)
├── slides.ipynb  # Slides
├── slides_pt[n].ipynb  # More slides, see 'structure' below
└── ...  # TBA
```

You can view or download the materials directly from GitHub, using the link above, or you can clone the repository using
```Bash
git clone https://github.com/iwh-halle/FinancialDataAnalytics.git
```
Make sure to update the repository regularly, especially before a lecture, using
```Bash
git pull
```

## Reading

This course is predominantly hands on and draws from several subject areas, such as financial economics, data science or textual analysis. As such, there exists no single text book recommendation. Relevant 'reading' material is linked in the script. That being said, resources include but are not limited to:
* "Python for Finance" (Yves Hilpisch)
* "Data Analysis for Business, Economics, and Policy" (Gabor Bekes, Gabor Kezdi)
* "Applied Text Analysis with Python" (Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda)
* "The big short" (A. McKay)
* "Margin Call" (J. C. Chandor)
* https://stackoverflow.com/
* https://docs.python.org/3/tutorial/index.html
* https://git-scm.com/book/en/v2


## Grading Policy

The grading policy is discussed in detail during the first lecture.

* Homework assignments: 30%
* Case study: 40%
* Presentation: 30%
* Bonus points: + 15%
  * StudySnips: https://studysnips.eu.pythonanywhere.com/
  * Participation in GitHub discussions: https://github.com/iwh-halle/FinancialDataAnalytics/discussions
  * Bug bounty (pull requests): https://github.com/iwh-halle/FinancialDataAnalytics/pulls

### How to submit your work

All students are required to register using the classroom link that you can find on top of this page, see "Important links". 

You can use your existing GitHub account or create a new account free of charge. Please note that you can optionally sign up for GitHub Pro, which is offered free of charge with your university email address.

All deliverables must be submitted through this system. To this end, there is one simple rule:

**stage + commit + push = submit!**

If this doesn’t make much sense to you now, don't worry. We will discuss how to use Git and GitHub extensively, and you will have tutorial sessions for additional guidance.

### Deadlines

* Homework assignments, have to be submitted before the next lecture.
* Case submission deadlines will be announced with the case description.

The deadlines for all deliverables are tracked through their commit timestamps. We will talk more about this later.


## Structure

### Part 1: Introduction ([slides.ipynb](https://github.com/iwh-halle/FinancialDataAnalytics/blob/master/slides.ipynb))

* Discussion of grading scheme
* Setting up the tech
  * Git and GitHub
  * Necessary Python libraries (Anaconda distribution)
* Introduction to the Python programming language
* Data types and structures
* Packages and modules
* Complex data structures
* Plotting

### Part 2: Stochastic and numerical methods

* Random numbers
* Probability distributions
* Cholesky decomposition
* Numerical integration
* Numerical optimization
* Stochastic processes
* Monte Carlo simulation
* Valuation
* Risk measures

### Part 3: Financial time series
* Correlation
* Linear regression models (OLS)
* Auto regressive models (AR)
* Moving average models (MA)
* Auto regressive moving average (ARMA)
* Cointegration
* Empirical stylized facts

### Part 4: Data management
* Object-oriented programming
* Loose coupling
* Market data APIs
* Structured query language (SQL)
* More on Git (.gitignore)
* Large file storage
* Virtual environments

### Part 5: Data sourcing
* Web scraping
* Server infrastructure
* Scheduled tasks
* Logging

### Part 6: Natural language processing (NLP)
* Processing textual data
* Bag of words
* Word embedding
* Transformer architecture
* Large Language Models (LLM)
* ChatGPT API

### Case study: TBA

## Disclaimer:
This syllabus is a general plan for the course; deviations announced to the class by the instructor may be necessary.
