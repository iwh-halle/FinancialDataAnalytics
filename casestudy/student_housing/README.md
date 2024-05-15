![head.png](https://github.com/cafawo/FinancialDataAnalytics/blob/master/figures/head.jpg?raw=1)

# Financial Data Analytics in Python

**Prof. Dr. Fabian Woebbeking**</br>
Assistant Professor of Financial Economics

IWH - Leibniz Institute for Economic Research</br>
MLU - Martin Luther University Halle-Wittenberg

fabian.woebbeking@iwh-halle.de



# Case study: Student_Housing

In this case study, you will delve into the world of apartment sharing markets, focusing on data collection, analysis, and interpretation. Your task is to scrape data from the [WG-Gesucht website](https://www.wg-gesucht.de/) for a city that will be assigned to you. WG-gesucht is an online platform facilitating the exchange between individuals seeking shared living arrangements (Wohngemeinschaften or WGs) by allowing WG owners to advertise available rooms and prospective tenants to contact them directly. The objective is to analyze the determinants of apartment prices and the factors influencing the duration a WG (Wohngemeinschaft, German for shared apartment) listing stays online.

Guidance is provided in class, through dedicated tutorial sessions and on the course's [GitHub discussion board](https://github.com/cafawo/FinancialDataAnalytics/discussions). Please also note that you find plenty of guidance on the internet, including Wikipedia, YouTube and ChatGPT.

The ultimate deliverable is a summary of your analysis and findings in a README.md (results/README.md) file. The summary should include results from both parts of the case study, along with economic reasoning and explanations grounded in relevant literature. It should be succinct, clearly written, and supported by evidence from both the literature and your analysis. Additionally, if applicable, state possible limitations of your study. 

A secondary but equally important objective is that your code must be robust enough be executed and delivered through GitHub (see the course's README.md). 

## Part 1: Determinants of Apartment Prices

Your first step is to conduct a literature review to identify the determinants of real estate prices in urban areas. Look for academic papers and research articles that discuss factors such as location, amenities, neighborhood characteristics, transportation access, and market demand. 
Additionally, consider factors that contribute to the success of WG listings, as outlined by [WG-gesucht](https://www.wg-gesucht.de/artikel/creating-an-offer-this-is-how-you-successfully-place-an-ad).

Summarize your findings and develop hypotheses regarding which variables might influence apartment prices in your assigned city. Furtheremore, elaborate on your web scraping model. Assume that you want to maintain a regular scraping of this platform for at least one year. What is the best way to fully automatize the task? What would be the rootpage? Which tools do you need? Discuss the ethical aspects of doing such a job.

Next, scrape apartment listings from WG-Gesucht for your assigned city. Collect data on apartment features such as size, location, number of rooms, and rental price. Use regression analysis or machine learning techniques to examine the relationship between these variables and apartment prices. Assess the significance and magnitude of each variable and interpret the results in the context of your literature review.

## Part 2: Determinants of WG Listing Duration

In the second part of the analysis, focus on understanding the factors that affect the duration a WG listing remains online. Hypothesize about which factors might influence the likelihood of a WG listing being rented quickly or staying online for an extended period.

Use the scraped data from WG-Gesucht, including the duration each listing has been online. Analyze the relationship between the data and listing duration using statistical methods or machine learning algorithms. Identify significant predictors and provide insights into why certain WG listings might linger on the market longer than others.

In blue, you can find the price of the shared apartment, and in pink, you see the duration. Please be aware that the duration is in days after 23 hours.

![wg_gesuch.png](https://github.com/cafawo/FinancialDataAnalytics/blob/master/figures/wg_gesucht.jpg?raw=1)


## Repository Structure and Code

Your GitHub repository should be organized as follows:

```bash
apartment_analysis/
├── literature_review/     # Contains relevant academic papers
│   ├── UrbanEconPapers.pdf
│   └── RealEstateJournals.pdf
├── README.md              # Description of the case study and instructions
├── scraper.py             # Python script for web scraping WG-Gesucht
├── data_analysis.ipynb    # Jupyter notebook for data analysis
├── results/               # Folder for storing analysis results
│   ├── regression_results.csv
│   └── README.md  # Summary file of analysis results
└──


```

The structure, above are just a suggestion. You can structure your code differently if you like, however, you have to document the structure here in the README.md file. For this project, the web scraping should be implemented in  Python scripts (.py file) to collect data from WG-Gesucht. Once the data is gathered, the analysis should be conducted in a Jupyter Notebook. This approach allows for a clear separation between the data collection process and the analysis, making the workflow more organized and easier to manage.

# Summary of deliverables

All your codes and results have to be submitted within one GitHub repository as outlined in the [Syllabus (HERE)](https://github.com/cafawo/FinancialDataAnalytics#how-to-submit-your-work). The only exception are large data files (if any), which cannot be hosted on GitHub [(see HERE)](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). We discussed alternatives (e.g. Dropbox) during class.

You have time to submit your results until the last lecture, how you provision your time until then is up to you.

Code:
* Submit **executable** code.
* You are expected to guide us through your work, e.g. by an appropriate **README.md** file and comments inside your code. 
* Make sure (test) that your code can be executed.

Summary of Results (results/README.md) should include the following:  
* Literature
* Your findings
* Economic intuition 
* Conclude critically on possible limitations 

# Presentation 
In the final two sessions of the lecture, you'll have the opportunity to present your work to your peers. Each presentation should last around 15 minutes. Remember, active participation during presentations earns you points. Asking relevant questions and engaging in discussions contribute to your participation score. Let's make it an interactive and engaging learning experience for everyone!

Best of luck!

**If you need more help, post a question on the [discussion board](https://github.com/iwh-halle/FinancialDataAnalytics/discussions) or contact the TA for this course.**