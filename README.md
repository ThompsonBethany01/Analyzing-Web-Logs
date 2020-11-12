![Header](https://i.pinimg.com/originals/d2/88/bc/d288bcd2ddfff1886ddd267872206f66.png)
## About the Project
### Goals
Find actionable information for upper management to present during the board meeting Thursday morning (November 12th, 9:00am). 

### Deliverables
- Jupyter Notebook documenting process to conclusions
- One slide presentation on the most important findings that require immediate action / actionable insights

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
### Explore
The data is explored with an emphasis on time series analysis and anomaly detection. Depending on the question, data can be split into dataframes based on program (Web Dev or Data Science), cohort, and/or time period.
### Conclusions
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
Taking a look at user IDs for current students, it would appear that several have not accessed the curriculum often. However, checking the IP addresses associated with these users will show that some students have multiple user IDs.
</details>

<details>
<summary> Suspicous Activity? </summary> 

#### Is there suspicous activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
</details>

<details>
<summary> Cross-Access in Curriculum </summary> 

#### At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
</details>

<details>
<summary> After Graduation  </summary> 

#### What topics are grads continuing to reference after graduation and into their jobs (for each program)?
</details>

<details>
<summary> Least Popular Lessons  </summary> 

#### Which lessons are least accessed?
</details>

## How to Reproduce
- [X] Read this readme.md
- [ ] Download <kbd>Data_Analysis.ipynb</kbd> and <kbd>Wrangle.py</kbd> in your working directory.
- [ ] Run the Data_Analysis notebook.  

```Note: You will need the anonymized-curriculum-access.txt file saved in the same working directory.```  

## Author
[Bethany Thompson](https://github.com/ThompsonBethany01)
