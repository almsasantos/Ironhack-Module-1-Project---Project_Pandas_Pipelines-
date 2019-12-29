import pandas as pd
from acquisition import acquisition
from cleaning import cleaning
from webscraping import webscraping
import analysis
import matplotlib
from time import sleep
from sending import sending_email
import urllib.request
import os
import glob

def extra_analysis(file):
    print('Would you like to do an extra analysis of the billionaires list and check who occupies a specific position?')
    extra_analysis_answer = input('Write "Y" for Yes and "N" for No: ').upper().strip()
    if extra_analysis_answer == 'Y':
        num_position = int(input("From 0 to 2207, choose a number to see who's billionaire occupies that position: "))
        urllib.request.urlretrieve(df['image'][num_position], f"../data/results/{df['name'][num_position]}.jpg")
    else:
        pass


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
    print('5- Percentage of billionaires with studies')
    sleep(1)
    type_of_analysis = int(input('Choose from 1 to 5 what would you like to know about the billionaires of 2018? '))


    acquisition('df')
    cleaning('df')
    webscraping('df')
    df = pd.read_csv('df')


    if type_of_analysis == 1:
        analysis.num_billionaires_per_country(df)
    elif type_of_analysis == 2:
        analysis.male_female_ratio(df)
    elif type_of_analysis == 3:
        analysis.more_even_country(df)
    elif type_of_analysis == 4:
        analysis.profitable_work_field(df)
    elif type_of_analysis == 5:
        analysis.education_ratio(df)
    else:
        while not type_of_analysis in [1, 2, 3, 4, 5]:
            print(f'Not a valid number, try again with a choice from 1 to 5!')
            type_of_analysis = int(input('Choose from 1 to 5 what would you like to know about the billionaires of 2018? '))


def clear_results():
    # This function will remove all files .jpg, so once you decide to execute the code all works out perfectly
    files = glob.glob('../data/results/*.jpg')
    for f in files:
        os.remove(f)


if __name__ == '__main__':
    main()
    df = pd.read_csv('df')
    extra_analysis('df')
    sending_email()
    clear_results()
