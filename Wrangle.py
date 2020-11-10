import pandas as pd

################################ Acquire Web Logs ################################

def acquire_logs():
    '''
    Convert txt file of curriculumn web logs to a cleaned dataframe.
    '''
    # read csv file to data frame
    df = pd.read_csv('anonymized-curriculum-access.txt',
                      engine='python',
                     header=None,
                     index_col=False,
                     sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                     na_values='"-"',
                     )

    # rename columns from basic integers to names
    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    # setting index as date and time column combined
    df.index = pd.to_datetime(df.date + " " + df.time)

    # dropping unneeded columns
    df = df.drop(columns=['date','time'], axis=1)

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")

    df['ip_int'] = df.ip.str.replace(".","").astype("int")

    # filtering out non-curriculumn pages
    df = df[df.page_viewed.str.contains('jpeg') != True]

    df = df[df.page_viewed.str.contains('json') != True]

    df = df[df.page_viewed.str.contains('jpg') != True]

    df = df[df.page_viewed.str.contains('appendix') != True]

    df = df[df.page_viewed.str.contains('Appendix') != True]

    df = df[df.page_viewed != '/']

    df = df[df.page_viewed != 'toc']

    return df

##################################################################################