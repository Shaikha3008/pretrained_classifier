#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Shaikha AlRaeesi
# DATE CREATED: 24/01/2022                                 
# REVISED DATE: 25/01/2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
"""
# Retrieve the filenames from folder pet_images/
    filename_list = listdir("pet_images/")
    
# Print 10 of the filenames from folder pet_images/
    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
    
    # initiate enmty dic && # create empty dictionary for results_dic   
    pet_labels = []
    results_dic = dict()
    
    # go through the file and save each name
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx][0] != ".":
            pet_label = ''
            pet_image_filename = filename_list[idx]
            word_pet_image = pet_image_filename.lower().split('_')
            pet_name = ''
            
            for word in word_pet_image:
                if word.isalpha():
                    pet_name += word + " "
            
            pet_name = pet_name.strip()
            print('Filename = ', pet_image_filename, '    label = ', pet_name)
   
            # empty dictionary
            num_empty_dic = len(results_dic)
            print('\nEmpty dictionary has {} items'.format(num_empty_dic))
 # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
# a List that contains only one item - the pet image label
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_name]
            else:
                print('\nWARNING: key =' , filenames[idx],  'already exists in results_dic with value =', results_dic[filenames[idx]])
          
    print('\nPrinting all key-value pairs in dictionary results_dic:')
    for key in results_dic:
          print('\nfilename = ', key, '    pet label = ', results_dic[key][0])
            

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
