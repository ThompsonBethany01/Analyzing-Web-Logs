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

### Questions Asked
- Which lesson appears to attract the most traffic consistently across cohorts (per program)?
- Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
- Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
- Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
- At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
- What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
- Which lessons are least accessed?  

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

## How to Reproduce
- [X] Read this readme.md
- [ ] Download <kbd>Data_Analysis.ipynb</kbd> and <kbd>Wrangle.py</kbd> in your working directory.
- [ ] Run the Data_Analysis notebook.  

```Note: You will need the anonymized-curriculum-access.txt file saved in the same working directory.```  

## Author
[Bethany Thompson](https://github.com/ThompsonBethany01)
