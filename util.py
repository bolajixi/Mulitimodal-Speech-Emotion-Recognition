'''
    utility
'''
import os
import pickle


def file_search(dirname, sub_files, skip_dir=[]):
    '''
    Returns the number of files in the given directory.

        Parameters:
            dirname (string): File path to be searched
            sub_files (list): Subfiles in the directory
            skip_dir (list): dirnames need to be skipped

        Returns:
            None
    '''

    filenames = os.listdir(dirname)

    for filename in filenames:
        full_filename = os.path.join(dirname, filename)

        if os.path.isdir(full_filename):  # check if file path is in dir
            if full_filename.split('/')[-1] in skip_dir:
                continue
            else:
                file_search(full_filename, sub_files, skip_dir)

        else:
            sub_files.append(full_filename)


def create_folder(dirname):
    '''
    Creates a folder with the given file path.

        Parameters:
            dirname (string): File path to be created i.e, full path name

        Returns:
            None
    '''
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    else:
        print(f"File path --> '{dirname}' already exists")


def save_as_csv(file_name, data):
    '''
    Save extracted features as CSV file.

        Parameters:
            file_name (string): Name to save file as e.g 'foo.csv'
            data (DataFrame): Data to be saved in file

        Returns:
            None
    '''
    data.to_csv(file_name)
    print(f"'{file_name}' successfully saved")


def save_as_pickle(file_name, data):
    '''
    Save data as pickle file.

        Parameters:
            file_name (string): Name to save file as e.g 'foo.pkl'
            data (DataFrame): Data to be saved in file

        Returns:
            None
    '''
    data.to_pickle(file_name)
    print(f"'{file_name}' successfully saved")


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row
