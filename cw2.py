#Code developed by Jason Shawn D' Souza

import json
import pandas as pd
import os.path
import sys
import json
import pandas as pd
import os.path

from tkinter import *

import jsonhandler
import guitest
import data
import argparse
#setting up jsonfile
dataframe = jsonhandler.jsonreader("data.json")

if (len(sys.argv) <= 1):
    #Use gui if 1 or more args on python promt/ MEANING: py cw2.py opens gui -----  py cw2.py blah blah opens CLI
    #Cant do <1 cause 3a 3b dont take additional args so py cw2.py 3a open gui instead of cli
    gui = guitest.gui(dataframe)
else :
    #use cli
    command = argparse.ArgumentParser(description='F20SC CW2 Data Analysis with issuu dataset')
    command.add_argument('-u', '--user_uuid',
                     help='Enter the uuid of a user.')
    command.add_argument('-f', '--file_name',
                         help='Enter the file name of the json.')
    command.add_argument('-d', '--doc_uuid',
                     help='Enter the document_id of the document.\n used for Task 2a, 2b and 4d')
    command.add_argument('-t', '--task_id',
                         help='Enter a tasks id to run these can be one of \n 2a 2b 3a 3b 4d 5')
    # managing incoming arguments and sending them to their related functions
    command_args = command.parse_args()
    if command_args.task_id == '2a':
        if command_args.doc_uuid is not None:
            if command_args.file_name == None:
                dataframe = jsonhandler.jsonreader("data.json")
                data.bycountry(dataframe, command_args.doc_uuid)
            else:
                dataframe = jsonhandler.jsonreader(command_args.file_name)
                data.bycountry(dataframe, command_args.doc_uuid)
        else:
            print('Enter valid document id with -d docidhere')
    elif command_args.task_id == '2b':
        if command_args.doc_uuid is not None:
            if command_args.file_name == None:
                dataframe = jsonhandler.jsonreader("data.json")
                data.bycontinent(dataframe, command_args.doc_uuid)
            else:
                dataframe = jsonhandler.jsonreader(command_args.file_name)
                data.bycontinent(dataframe, command_args.doc_uuid)
        else:
            print('Enter valid document id with -d docidhere')
    elif command_args.task_id == '3a':
        if command_args.file_name == None:
            dataframe = jsonhandler.jsonreader("data.json")
            data.verbosehisto(dataframe)
        else:
            dataframe = jsonhandler.jsonreader(command_args.file_name)
            data.verbosehisto(dataframe)
    elif command_args.task_id == '3b':
        if command_args.file_name == None:
            dataframe = jsonhandler.jsonreader("data.json")
            data.properhisto(dataframe)
        else:
            dataframe = jsonhandler.jsonreader(command_args.file_name)
            data.verbosehisto(dataframe)

            #elif command_args.task_id == 'Task4d':
        #data.also_liketop10(dataframe)
    elif command_args.task_id == '5':
        if command_args.user_uuid is not None and command_args.doc_uuid is not None:
            if command_args.file_name == None:
                dataframe = jsonhandler.jsonreader("data.json")
                data.task5(dataframe, command_args.doc_uuid, command_args.user_uuid)
            else:
                dataframe = jsonhandler.jsonreader(command_args.file_name)
                data.task5(dataframe, command_args.doc_uuid, command_args.user_uuid)
        elif command_args.user_uuid is None and command_args.doc_uuid is not None:
            if command_args.file_name == None:
                dataframe = jsonhandler.jsonreader("data.json")
                data.task5(dataframe, command_args.doc_uuid)
            else:
                dataframe = jsonhandler.jsonreader(command_args.file_name)
                data.task5(dataframe, command_args.doc_uuid)
        else:
            print('Enter valid document id with -d docidhere. Document id is mandatory whereas user id is optional')


    else:
        print('Invalid argument. Use  -h to see help')

