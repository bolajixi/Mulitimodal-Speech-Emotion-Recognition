'''
    utility
'''
import os
import csv


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
