import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

def cleaning_pipeline(df, drop_col):
    '''
    Performs general cleanup of dataframe. Drop columns that did not offer information
    useful for machine learning or were a source of data leakage. Removes entries that
    did not complete the survey. Converts the target column to binary. Returns a clean
    dataframe.
    =========
    Parameters:

        df: pandas dataframe

        drop_col: list of the columns that need to be dropped

    =========
    Returns:

        return_df: pandas dataframe that has been cleaned
    '''
    # drop specified columns
    return_df = df.drop(drop_col, axis=1)
    # remove entries that did not complete the survey
    return_df = return_df[return_df['HRFS12M1'] != -1]

    # convert target col to binary: 1 for food insecure, 0 for food secure
    return_df['HRFS12M1'] = return_df['HRFS12M1'].replace({1: 0, 2: 1, 3: 1, -9: 0})

    return return_df


def plot_hours_worked_food_security(df):
    '''
    Creates 2 bar plots; the first is the hours worked for individuals that are
    food secure, the second is the hours worked for individuals that are food
    insecure. Option to save the figure by uncommenting fig.savefig line 
    =========
    Parameters:

        df: pandas dataframe


    =========
    Returns:

        None
    '''
    plt.style.use('ggplot')

    secure_df = df[df['HRFS12M1']==0]
    insecure_df = df[df['HRFS12M1']==1]

    # Convert the ints representing classes to their classes
    secure_hours = secure_df['PRHRUSL'].sort_values().replace({-1: 'Not Working',
                                                            1: '0-20 HRS',
                                                            2: '21-34 HRS',
                                                            3: '35-39 HRS',
                                                            4: '40 HRS',
                                                            5: '41-49 HRS',
                                                            6: '50 OR MORE HRS',
                                                            7: 'VARIES-FULL TIME',
                                                            8: 'VARIES-PART TIME'})
    insecure_hours = insecure_df['PRHRUSL'].sort_values().replace({-1: 'Not Working',
                                                            1: '0-20 HRS',
                                                            2: '21-34 HRS',
                                                            3: '35-39 HRS',
                                                            4: '40 HRS',
                                                            5: '41-49 HRS',
                                                            6: '50 OR MORE HRS',
                                                            7: 'VARIES-FULL TIME',
                                                            8: 'VARIES-PART TIME'})                                                        


    sorted_secure = secure_hours.value_counts()
    sorted_insecure = insecure_hours.value_counts()

    sorted_secure = sorted_secure.reindex(['Not Working', '0-20 HRS', '21-34 HRS',
                                   '35-39 HRS', '40 HRS', '41-49 HRS', '50 OR MORE HRS',
                                   'VARIES-FULL TIME', 'VARIES-PART TIME'])
    sorted_insecure = sorted_insecure.reindex(['Not Working', '0-20 HRS', '21-34 HRS',
                                   '35-39 HRS', '40 HRS', '41-49 HRS', '50 OR MORE HRS',
                                   'VARIES-FULL TIME', 'VARIES-PART TIME'])

    for plot_data, status in [(sorted_secure, 'Food Secure'), (sorted_insecure, 'Food Insecure')]:
        # create a new fig for each iteration so img can be saved individually
        fig, ax = plt.subplots(figsize=(10,10))
        ax.bar(plot_data.index, plot_data.values)
        ax.set_title(f'Hours Worked For {status} Individuals')
        ax.set_ylabel('Number of People')
        ax.set_xlabel('Number of Hours Worked')
        plt.xticks(rotation=45)

        # un-comment line below to save image
        # fig.savefig(f'../img/worked_{status}.png');

if __name__ == '__main__':
    filepath = '../data/dec19pub.csv'
    data = pd.read_csv(filepath)
    drop_list = ['HRHHID', 'HRHHID2', 'FILLER', 'HRMONTH', 'HRYEAR4',
             'PULKDK6', 'PULKPS4', 'PULKPS5', 'PULKPS6',
             'HXPHONEO', 'QSTNUM']
    weights = ['HWHHWGT', 'PWSSWGT', 'HHSUPWGT', 'PWSUPWGT',
           'PWFMWGT', 'PWLGWGT', 'PWORWGT', 'PWVETWGT',
           'PWCMPWGT']
    data_leakage = ['HRFS12CX', 'HRFS12MD', 'HRFS12M3', 'HRFS12M4',
                'HRFS12MC', 'HRFS12M6', 'HRFS12M7', 'HRFS12M8',
                'HRFS12M9', 'HRFS12ME', 'HRFS30D1', 'HRFS30D2',
                'HRFS30D3', 'HRFS30D4', 'HRFS30D5', 'HRFS30D6',
                'HRFS30D7', 'HRFS30D8', 'HRFS30D9', 'HRFS30DE', 
                'HESH4', 'HESHF3', 'HESHM3', 'HESSM4', 'HETSHMF3', 
                'HESH3', 'HESSH1', 'HESS3', 'HESS2', 'HESSM6', 
                'HESS4', 'HESSH4', 'HESSH3', 'HESH2', 'HESH5', 
                'HESSH5', 'HESS6', 'HETSHMF2', 'HESHM2', 'HESSM3', 
                'HESHF2', 'HES9', 'HESSM2', 'HESSH2', 'HESS1', 'HESSM5']

    total_drop_list = drop_list + weights + data_leakage
    clean_data = cleaning_pipeline(data, total_drop_list)

    plot_hours_worked_food_security(clean_data)

