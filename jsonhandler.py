import pandas as pd
import json
#Reference for dataframes :https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
#Reading JSON file line by line and storing as dataframe object
def jsonreader(json_file_name='data.json'):
    arr = []
    json_file = open(json_file_name)
    for line in json_file:
        json_object = json.loads(line)       #jsonline stored in json_object
        arr.append(json_object)              #empty list add this object(line by line)
    df = pd.DataFrame(arr, columns=['ts', 'visitor_uuid', 'visitor_username', 'visitor_source',
                                                  'visitor_device', 'visitor_useragent', 'visitor_ip',
                                                  'visitor_country', 'visitor_referrer', 'env_type', 'env_doc_id',
                                                  'env_adid', 'event_type', 'event_readtime', 'subject_type',
                                                  'env_type', 'subject_doc_id', 'subject_page', 'cause'])
    return df

#Store in dframe and return




