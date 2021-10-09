import pandas as pd
from model16 import trainModel
import subprocess
import os

def getFileNumber(filename) :
    number = filename.split('_')[-1]
    return number

max_limit = 1048576
starting_file_name = input('Enter File Name\t')
file_number = getFileNumber(starting_file_name)

template_data_list = [*pd.read_csv('template_filled.csv', chunksize=170,header=None)]
for template in template_data_list:
    template.reset_index(drop=True, inplace=True)
PPI_data_list = [*pd.read_csv('PPI.csv', chunksize=1,header=None)]
number_of_iter = len(PPI_data_list)


for i in range(0,number_of_iter):
    print('\nPerforming operation for product', i+1, '\n')
    last_column = template_data_list[i].pop(template_data_list[i].columns[-1])
    PPI_append = pd.concat([PPI_data_list[i]]*170, ignore_index=True)
    data = pd.concat([template_data_list[i],PPI_append,last_column], axis=1)
    data.to_csv('dataset_specific_rolling.csv',index=False,header=False)
    
    while(1): 
        print('\nRuning trainModel()\n')
        trainModel()

        char = input('Is Accuracy upto the Mark ? (y/n)\t')
        if char.upper() == 'Y':
            break
    # else:
    PPI_data_list[i].to_csv('input.csv',index=False,header=False)
    print('Input the Created CSV \n')
    
    print('runing main.py\n')
    subprocess.run('python main.py')

    all_cases_data = pd.read_csv('./saved_cases/all_cases.csv',header=None)
    size_all_cases_data = len(all_cases_data) 

    if os.path.exists('./'+starting_file_name+'.csv'):
        print('\nReading Dataset CSV\n')
        master_data = pd.read_csv(starting_file_name + '.csv',header=None)
        size_master_data = len(master_data)

        print('\nWriting to CSV')
        if size_all_cases_data + size_master_data < max_limit :
            new_master_data = pd.concat([master_data,all_cases_data])
            new_master_data.to_csv(starting_file_name + '.csv',index=False,header=False)
        else:
            file_number = str(int(file_number)+1)
            starting_file_name = starting_file_name[:-(len(file_number))]+file_number
            all_cases_data.to_csv(starting_file_name + '.csv',index=False,header=False)
    else:
        all_cases_data.to_csv(starting_file_name + '.csv',index=False,header=False)

