import pandas as pd
from acquisition import acquisition
from cleaning import cleaning
from webscraping import webscraping
import analysis
import matplotlib
from time import sleep
from sending import sending_email


def main():
    print('Prepare yourself for an analysis of the billionaires of 2018:')
    sleep(1)
    print('1- Which country has maximum numbers of billionaires?')
    sleep(1)
    print('2- Male to female ratio based on the total of dollares')
    sleep(1)
    print('3- Which country has the greatest share in terms of total money held by its billionaires?')
    sleep(1)
    print('4- Top 10 most profitable field of work')
    sleep(1)
    type_of_analysis = int(input('Choose from 1 to 4 what would you like to know about the billionaires of 2018? '))

    acquisition('df_acquisition')
    cleaning('cleaned')
    webscraping('web')
    df = pd.read_csv('web')

    if type_of_analysis == 1:
        analysis.num_billionaires_per_country(df)
    elif type_of_analysis == 2:
        analysis.male_female_ratio(df)
    elif type_of_analysis == 3:
        analysis.more_even_country(df)
    elif type_of_analysis == 4:
        analysis.profitable_work_field(df)
    else:
        print('Not a valid number, try again with a choice from 1 to 4!')

if __name__ == '__main__':
    main()
    sending_email()
