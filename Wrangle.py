import pandas as pd

################################ Acquire Web Logs ################################

def acquire_logs():
    '''
    Convert csv file of curriculumn web logs to a cleaned dataframe.
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

    return df

##################################################################################