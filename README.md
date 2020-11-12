![Header](https://i.pinimg.com/originals/d2/88/bc/d288bcd2ddfff1886ddd267872206f66.png)
## About the Project
### Goals
Find actionable information for upper management to present during the board meeting Thursday morning (November 12th, 9:00am) on analysis of curriculum web logs. 

### Deliverables
- Jupyter Notebook documenting process to conclusions - [Data_Analysis.ipynb](https://github.com/ThompsonBethany01/Analyzing-Web-Logs/blob/main/Data_Analysis.ipynb)
- One slide [presentation](https://www.canva.com/design/DAENRN4KY-w/KAwBt-fdS0MwwYFH_qC_uw/view?utm_content=DAENRN4KY-w&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu) on the most important findings that require immediate action / actionable insights

### Data Dictionary
| feature     | description                                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------|
| index       | YYYY-MM-DD hh:mm:ss of the observation (page viewed by user)                                                                           |
| page_viewed | End url of curriculum accessed ds.codeup.com/<page_viewed>                                                                             |
| user_id     | Unique id for user, a student can have multiple IDs but multiple students can not share the same id                                    |
| cohort_id   | Unique id for cohort, also a staff group; some values are null                                                                         |
| ip          | Internet Protocol address for the observation (page viewed by user), an identifying number for network hardware connected to a network |

## Project Steps
### Wrangle
The curriculum logs are stored in a txt file called ```anonymized-curriculum-access.txt```. Within the Wrangle.py module, this data is aquired and prepped.   
- Txt file is read to a dataframe
- Index is set to the timestamp of the observation
- Columns are renamed appropriately
- Null cohort IDs are set to 0
- Converted IP address to integer in seperate column for different manipulation
- Non-curriculum pages are filtered out of the df, such as '/' or appendix pages  

The prepped dataframe is returned. Because no modeling is needed, the data will not be split.
### Explore
The data is explored with an emphasis on time series analysis and anomaly detection. Depending on the question, data can be split into dataframes based on program (Web Dev or Data Science), cohort, and/or time period.
### Conclusions, Click for Details
<details>
<summary> Top Lessons </summary> 

#### Which lesson appears to attract the most traffic consistently across cohorts (per program)?
Introductory curriculum attracts the most page views for both Data Science and Web Dev(Intro to DS and Javascript-i respectively). For Data Science the views peak at the beginning of each cohort, but the trends are consistent across multiple cohorts. Web Dev has a greater amount of cohorts, so trends for the start of the program are not as pronounced.  

![Popular-Lessons-Chart](https://i.pinimg.com/originals/41/a4/c2/41a4c2292cd7de4c7d2ae0596063f2dd.png)
</details>

<details>
<summary> Views by Cohort </summary> 

#### Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?
- Within Data Science cohorts, there is some variation in most popular lessons viewed. While Darden spent a larger amount of time with the Classification Overview, Curie spent more time with MySQL Overview, and Bayes spent more time on Intro to DS.  
- Within Web Dev, the lesson did not significantly affect the page views. Views stayed consistent across cohorts, so a lesson was viewed less or more by cohort. For example, throughout the most popular lessons, Cera does not view as often as Fortuna.  

![Popular-Lessons-Cohorts](https://i.pinimg.com/originals/c3/29/96/c32996a8e623d0c9032198731c08bc99.png)
</details>

<details>
<summary> Inactive Students </summary> 

#### Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
Taking a look at user IDs for current students, it would appear that several have not accessed the curriculum often. However, checking the IP addresses associated with these users will show that some students have multiple user IDs. This was the case for the six current users with the least amount of curriculum visits.
</details>

<details>
<summary> Suspicous Activity </summary> 

#### Is there suspicous activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
Pages to Look Into  
- ```%20https://github.com/RaulCPena```
- ```java-iii/jdbc/poop```
- ```spring/extra-features/error-pages/asdfasdf```
- ```students/643/This%20alumnus%20works%20for%20Appdiction%20Studios,%20as%20of%20this%20timestamp.%20This%20company%20is%20launching%20a%20bootcamp%20program%20in%20competition.%20For%20this%20reason,%20curriculum%20access%20is%20disabled%20until%20further%20notice.```

User 590  
- Has 73 different IP addresses used since starting in Curie (Feb. 2020)
- One IP address may originate from China when checking the location on a free IP lookup site
- Visits some pages for less than a minute before changing to other sites

</details>

<details>
<summary> Cross-Access in Curriculum </summary> 

#### At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
While there is evidence of cross-access in the past, only three users show this occurrence recently.  
User 730:
- Attended Bash WD cohort
- Accessed DS curriculum November 1st, 2020  

User 280:
- Attended previous WD cohort Xanadu
- Currently associated with Darden cohort ID
- Is this an employee/instructor mislabeled as Darden instead of Staff cohort ID?  

User 590:
- Attended Curie cohort
- Accessed Web Dev curriculum in May 2020
- Is this an employee/instructor? Or before cut off?
</details>

<details>
<summary> After Graduation  </summary> 

#### What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
I chose to look at each graduated cohort, plotting the cohort's most viewed page over time. To do so, I created a loop to filter out the df to only the observations made by the specific cohort, find the most viewed page from this, then resample on a bi-weekly period. There are 34 total graduated cohorts which are subplotted in 17 columns by 2 rows.

<details>
<summary> Click for Subplot </summary>

![Top-Lesson-By-Bohort-Over-Time](https://i.pinimg.com/originals/71/d4/fc/71d4fcd51751223de0b7b4762bfc30bf.png)

</details>

Some cohorts viewed their most popular page more in the beginning, while others stayed more consistent. For example:  
- Cohort 7 viewed javascript-i (specifically operators and variables) with peaks over time
- Cohort 8 viewed java-i consistently in 2018 but dropped off in views after
- Cohort 17 viewed javascript-i consistently past graduation

</details>

<details>
<summary> Least Popular Lessons  </summary> 

#### Which lessons are least accessed?
There were many pages viewed only once through out the web log. Within Data Science, these included:  
- 12-distributed-ml/spark-topics
- anomaly-detection/time-series-anomaly-detection-part-1
- 7.4.1-pandas-overview
- 2.1-spreadsheets-overview
- 4-python/pandas-lesson
- regression/least-angle-regression
- classification/handling-missing-values
- regression/ridge-regression
- advanced-topics/tidy-data  

Within Web Dev, these included:
- cli/4-navigating-the-filesystem
- javascript-i/math
- 8.0_Intro_Module
- 4-stats/1-descriptive-stats
- 6-regression/4-multivariate-regression-in-excel
- 2-sql/database-design
- 5-stats/4.2-compare-means/null
- 12-distributed-ml/spark-topics
- java-iii/servelet
</details>

## How to Reproduce
- [X] Read this readme.md
- [ ] Download <kbd>Data_Analysis.ipynb</kbd> and <kbd>Wrangle.py</kbd> in your working directory.
- [ ] Run the Data_Analysis notebook.  

```Note: You will need the anonymized-curriculum-access.txt file saved in the same working directory.```  

## Author
[Bethany Thompson](https://github.com/ThompsonBethany01)
