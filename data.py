import Plot
import pandas as pd
from collections import Counter
from graphviz import Digraph
from pprint import pprint
#import jsonhandler
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/' #path to dot.exe for running graph
#PLEASE EDIT THE ABOVE PATH FOR GRAPHVIZ TO SHOW :D
#dataframe = jsonhandler.jsonreader("data.json")
#task2a
#Takes documentid and finds countries of viewers of a document
#Check for doc id
def bycountry(data, document_id):
    mid = data['subject_doc_id'] == document_id
    data = data[mid]
    grouped = data.groupby('visitor_country')
    #Group by country
    pprint(grouped)
    #print pandas object
    xdata =[]
    ydata = []
    for key ,item in grouped:
        xdata.append(key)      #append country
        ydata.append(len(item)) # append count
    Plot.plothistogram('Countries Histogram', xdata,ydata,'vertical')

#task2b
# Takes documentid and finds viewers of the document but by continent
def bycontinent(data, document_id):

    # First take data from the previous task(bycountry)

    mid = data['subject_doc_id'] == document_id
    data = data[mid]
    grouped = data.groupby('visitor_country')
    pprint(grouped)
    xdata =[]
    ydata = []
    for key,item in grouped:
        xdata.append(key)
        ydata.append(len(item))
    pprint(xdata)
    pprint(ydata)
    #change countries to continents
    xdata2 = []
    ydata2 = []
    index = 0   #python indexes start at 0 SOURCE : -  accessing index in python for loops will be referenced
    for x in xdata:
        #make sure country exists in the countrytocontinentdict,
        #countrytocontinent dictionary is taken from the HW MACS site
        if xdata[index] in countrytocontinent:  #from country count compare to dict.
            xdata2.append(countrytocontinent[x])
            ydata2.append(ydata[index])
        index = index +1
    for index1 in range(0, len(xdata2)):
        for index2 in range(index1, len(xdata2)):
            if not index1 == index2:
                if xdata2[index1] == xdata2[index2]:
                    ydata2[index1] = ydata2[index1] + ydata2[index2]
                    xdata2[index2]= 'remove'             # The countries get removed along with count temp. / they still will exist on graph unless a new list is made
    #making a final new list that will be used for plotting
    xdatafinal =[]
    ydatafinal = []
    for index3 in range(0, len(xdata2)):
        if xdata2[index3] == 'remove':     #finally will be removed
            continue
        xdatafinal.append(xdata2[index3])  #final lists
        ydatafinal.append(ydata2[index3])
    Plot.plothistogram('Histogram of continents', xdatafinal, ydatafinal,'vertical')



#Dictionary of countries to continents taken from
#https://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py
countrytocontinent= {
  'AF' : 'AS',
  'AX' : 'EU',
  'AL' : 'EU',
  'DZ' : 'AF',
  'AS' : 'OC',
  'AD' : 'EU',
  'AO' : 'AF',
  'AI' : 'NA',
  'AQ' : 'AN',
  'AG' : 'NA',
  'AR' : 'SA',
  'AM' : 'AS',
  'AW' : 'NA',
  'AU' : 'OC',
  'AT' : 'EU',
  'AZ' : 'AS',
  'BS' : 'NA',
  'BH' : 'AS',
  'BD' : 'AS',
  'BB' : 'NA',
  'BY' : 'EU',
  'BE' : 'EU',
  'BZ' : 'NA',
  'BJ' : 'AF',
  'BM' : 'NA',
  'BT' : 'AS',
  'BO' : 'SA',
  'BQ' : 'NA',
  'BA' : 'EU',
  'BW' : 'AF',
  'BV' : 'AN',
  'BR' : 'SA',
  'IO' : 'AS',
  'VG' : 'NA',
  'BN' : 'AS',
  'BG' : 'EU',
  'BF' : 'AF',
  'BI' : 'AF',
  'KH' : 'AS',
  'CM' : 'AF',
  'CA' : 'NA',
  'CV' : 'AF',
  'KY' : 'NA',
  'CF' : 'AF',
  'TD' : 'AF',
  'CL' : 'SA',
  'CN' : 'AS',
  'CX' : 'AS',
  'CC' : 'AS',
  'CO' : 'SA',
  'KM' : 'AF',
  'CD' : 'AF',
  'CG' : 'AF',
  'CK' : 'OC',
  'CR' : 'NA',
  'CI' : 'AF',
  'HR' : 'EU',
  'CU' : 'NA',
  'CW' : 'NA',
  'CY' : 'AS',
  'CZ' : 'EU',
  'DK' : 'EU',
  'DJ' : 'AF',
  'DM' : 'NA',
  'DO' : 'NA',
  'EC' : 'SA',
  'EG' : 'AF',
  'SV' : 'NA',
  'GQ' : 'AF',
  'ER' : 'AF',
  'EE' : 'EU',
  'ET' : 'AF',
  'FO' : 'EU',
  'FK' : 'SA',
  'FJ' : 'OC',
  'FI' : 'EU',
  'FR' : 'EU',
  'GF' : 'SA',
  'PF' : 'OC',
  'TF' : 'AN',
  'GA' : 'AF',
  'GM' : 'AF',
  'GE' : 'AS',
  'DE' : 'EU',
  'GH' : 'AF',
  'GI' : 'EU',
  'GR' : 'EU',
  'GL' : 'NA',
  'GD' : 'NA',
  'GP' : 'NA',
  'GU' : 'OC',
  'GT' : 'NA',
  'GG' : 'EU',
  'GN' : 'AF',
  'GW' : 'AF',
  'GY' : 'SA',
  'HT' : 'NA',
  'HM' : 'AN',
  'VA' : 'EU',
  'HN' : 'NA',
  'HK' : 'AS',
  'HU' : 'EU',
  'IS' : 'EU',
  'IN' : 'AS',
  'ID' : 'AS',
  'IR' : 'AS',
  'IQ' : 'AS',
  'IE' : 'EU',
  'IM' : 'EU',
  'IL' : 'AS',
  'IT' : 'EU',
  'JM' : 'NA',
  'JP' : 'AS',
  'JE' : 'EU',
  'JO' : 'AS',
  'KZ' : 'AS',
  'KE' : 'AF',
  'KI' : 'OC',
  'KP' : 'AS',
  'KR' : 'AS',
  'KW' : 'AS',
  'KG' : 'AS',
  'LA' : 'AS',
  'LV' : 'EU',
  'LB' : 'AS',
  'LS' : 'AF',
  'LR' : 'AF',
  'LY' : 'AF',
  'LI' : 'EU',
  'LT' : 'EU',
  'LU' : 'EU',
  'MO' : 'AS',
  'MK' : 'EU',
  'MG' : 'AF',
  'MW' : 'AF',
  'MY' : 'AS',
  'MV' : 'AS',
  'ML' : 'AF',
  'MT' : 'EU',
  'MH' : 'OC',
  'MQ' : 'NA',
  'MR' : 'AF',
  'MU' : 'AF',
  'YT' : 'AF',
  'MX' : 'NA',
  'FM' : 'OC',
  'MD' : 'EU',
  'MC' : 'EU',
  'MN' : 'AS',
  'ME' : 'EU',
  'MS' : 'NA',
  'MA' : 'AF',
  'MZ' : 'AF',
  'MM' : 'AS',
  'NA' : 'AF',
  'NR' : 'OC',
  'NP' : 'AS',
  'NL' : 'EU',
  'NC' : 'OC',
  'NZ' : 'OC',
  'NI' : 'NA',
  'NE' : 'AF',
  'NG' : 'AF',
  'NU' : 'OC',
  'NF' : 'OC',
  'MP' : 'OC',
  'NO' : 'EU',
  'OM' : 'AS',
  'PK' : 'AS',
  'PW' : 'OC',
  'PS' : 'AS',
  'PA' : 'NA',
  'PG' : 'OC',
  'PY' : 'SA',
  'PE' : 'SA',
  'PH' : 'AS',
  'PN' : 'OC',
  'PL' : 'EU',
  'PT' : 'EU',
  'PR' : 'NA',
  'QA' : 'AS',
  'RE' : 'AF',
  'RO' : 'EU',
  'RU' : 'EU',
  'RW' : 'AF',
  'BL' : 'NA',
  'SH' : 'AF',
  'KN' : 'NA',
  'LC' : 'NA',
  'MF' : 'NA',
  'PM' : 'NA',
  'VC' : 'NA',
  'WS' : 'OC',
  'SM' : 'EU',
  'ST' : 'AF',
  'SA' : 'AS',
  'SN' : 'AF',
  'RS' : 'EU',
  'SC' : 'AF',
  'SL' : 'AF',
  'SG' : 'AS',
  'SX' : 'NA',
  'SK' : 'EU',
  'SI' : 'EU',
  'SB' : 'OC',
  'SO' : 'AF',
  'ZA' : 'AF',
  'GS' : 'AN',
  'SS' : 'AF',
  'ES' : 'EU',
  'LK' : 'AS',
  'SD' : 'AF',
  'SR' : 'SA',
  'SJ' : 'EU',
  'SZ' : 'AF',
  'SE' : 'EU',
  'CH' : 'EU',
  'SY' : 'AS',
  'TW' : 'AS',
  'TJ' : 'AS',
  'TZ' : 'AF',
  'TH' : 'AS',
  'TL' : 'AS',
  'TG' : 'AF',
  'TK' : 'OC',
  'TO' : 'OC',
  'TT' : 'NA',
  'TN' : 'AF',
  'TR' : 'AS',
  'TM' : 'AS',
  'TC' : 'NA',
  'TV' : 'OC',
  'UG' : 'AF',
  'UA' : 'EU',
  'AE' : 'AS',
  'GB' : 'EU',
  'US' : 'NA',
  'UM' : 'OC',
  'VI' : 'NA',
  'UY' : 'SA',
  'UZ' : 'AS',
  'VU' : 'OC',
  'VE' : 'SA',
  'VN' : 'AS',
  'WF' : 'OC',
  'EH' : 'AF',
  'YE' : 'AS',
  'ZM' : 'AF',
  'ZW' : 'AF'
}


#bycontinent(dataframe,'140227080132-c038e5546d578cf4895a66e6fd8d2dc0')

#Task 3a
def verbosehisto(data):
    #only need data no documentid
    grouped = data.groupby('visitor_useragent')
    xdata= []
    ydata = []
    for key, item in grouped:
        xdata.append(key)
        ydata.append(len(item))  #item.index
    # note: too many columns mean that user has to zoom in
    Plot.plothistogram('Verbose useragents', xdata, ydata, 'horizontal')
    #The lines below are for CLI plotting first then show data
    pprint('-------verbose useragents--------')
    pprint(xdata)
    pprint(ydata)
    pprint('-------verbose useragents done ---------')


#Task 3b
#only need data no documentid
#Popular browsers - Chrome Safari Mozilla Opera, surprised no internet explorer
def properhisto(data):
    grouped = data.groupby('visitor_useragent')
    browser_name = ['Dalvik', 'Mozilla', 'UCWEB', 'Opera', 'LG-E610']  # Should use regex to get these !
    browser_count = [0, 0, 0, 0, 0]
    for k, group in grouped:
        for index in range(0, len(browser_name)):
            if browser_name[index] in k:
                browser_count[index] = browser_count[index] + len(group.index)
    Plot.plothistogram('Popular Browsers', browser_name, browser_count, 'vertical')
    #For CLI plt first then show
    pprint('-------popular browsers--------')
    pprint(browser_name)
    pprint(browser_count)
    pprint('----------popular browsers done--------')


#Task 4a
def getvisitors(data, document_id='130601015527-c1e2993d8290975e7ef350f078134390'):
    readers = []
    newreaders = []

    data = data.loc[(data['subject_doc_id'] == document_id) & (data['event_type'] == "read")]
    grouped = data.groupby('subject_doc_id')
    pprint(grouped)
    for k, group in grouped:
        if k == document_id:
            # convert group's column to a list
            readers = data['visitor_uuid'].tolist()
            for i in readers:
                if i not in newreaders:
                    newreaders.append(i)
            break
    df = pd.DataFrame(newreaders, columns=["col"])
    print(df["col"].value_counts())
    # returning list of visitors
    return (readers, newreaders)
#a=getvisitors(dataframe,'130601015527-c1e2993d8290975e7ef350f078134390')


#Task 4b
def getdocbyvisitor(data, visitor_uuid ='f69c153f95c96fa7'):
    docs = []
    newdocs = []
    data = data.loc[(data['visitor_uuid'] == visitor_uuid)& (data['event_type'] == "read")]
    grouped = data.groupby('visitor_uuid')
    pprint(grouped)
    for k, group in grouped:
        if k == visitor_uuid:
            # From a column to list
            docs = data['subject_doc_id'].tolist()
            for i in docs:
                if i not in newdocs:
                    newdocs.append(i)
            break
    df = pd.DataFrame(newdocs, columns=["col"])
    print(df["col"].value_counts())
    # returning list of visitors
    return (docs, newdocs)
#a=getdocbyvisitor(dataframe,'1f891eb0b573e42c')



#Task 4c
def also_like(data,document_id='100806162735-00000000115598650cb8b514246272b5', visitor_uuid =None):
    #Optional uuid
    if visitor_uuid ==None:
        data2 =getvisitors(data,document_id)
        newlist = []
        for k in data2[0]:
            data3 = getdocbyvisitor(data,k)
            newlist.append(data3)
        pprint(newlist)
        res_list = [x[0] for x in newlist]
        #print(type(res_list))
        #print(res_list)
        a=Counter(x for sublist in res_list for x in sublist) #works
        print(a)

        #pprint(data2)

#User id given
    if visitor_uuid !=None:
        data2 = getvisitors(data, document_id)
        newlist = []
        secondlist = []
        for k in data2[0]:
                data3 = getdocbyvisitor(data, k)
                newlist.append(data3)
                if k == visitor_uuid:
                    test = getdocbyvisitor(data,k)
                    secondlist.append(test)

        #print(secondlist)
        count = [x[0] for x in secondlist]
        #print(type(count))
        #print(count)
        b = Counter(x for sublist in count for x in sublist) # for the particular userid
        print(b)
        res_list = [x[0] for x in newlist]
        test=[]
        a = Counter(x for sublist in res_list for x in sublist) # For all the docs gotten from the uid
        print(a)
        list2=[]
        for k in res_list:
            if k in count:
                list2.append(k)
        pprint(list2)
        res_list2 = [i for i in res_list if i in list2]
        f = Counter(x for sublist in res_list2 for x in sublist)
        #print(found)
        print(f)#The final but the joint readers numbering is wrong need to fix
#task 4d
#Not done
def also_liketop10(data,document_id='130601015527-c1e2993d8290975e7ef350f078134390', visitor_uuid ='1f891eb0b573e42c'):
    dataneeded = also_like(data,document_id,visitor_uuid)

#Task 5
def task5(data,document_id,visitorid=None):
    print("Doc Id" +document_id)
    #b = also_liketop10(dataframe, '130601015527-c1e2993d8290975e7ef350f078134390')
    if visitorid ==None:
        data2 =getvisitors(data,document_id)
        newlist = []
        for k in data2[0]:
            data3 = getdocbyvisitor(data,k)
            newlist.append(data3)
        res_list = [x[0] for x in newlist]
        listfinal=[]
        for i in res_list:
            if i not in listfinal:
                listfinal.append(i)
            break
        dot = Digraph(format='png')
        for x in data2[0]: # for all visitors
            for y in listfinal[0]: # for docs
                dot.node(x) # vis
                dot.node(y) # doc
                dot.edge(x,y) # edge between them
                if y == document_id: # if same doc. id as input green
                    dot.attr('node', shape='box', style='filled', fillcolor='green')
                else:
                    dot.attr('node',  style='filled', fillcolor='white')
        print(dot.source)
        filename = dot.render(filename='img/g1', view=True) # render and view but still store it separately
        print(filename + "has been created")
    else:
        data2 = getvisitors(data, document_id)
        newlist = []
        secondlist = []
        for k in data2[0]:
            data3 = getdocbyvisitor(data, k)
            newlist.append(data3)
            if k == visitorid:
                test = getdocbyvisitor(data, k)
                secondlist.append(test)

        # print(secondlist)
        count = [x[0] for x in secondlist]#only docs of given uid
        # print(type(count))
        # print(count)
        res_list = [x[0] for x in newlist]#list with all docs from docid
        test = []
        list2 = []
        for k in res_list:
            if k in count:
                list2.append(k)
        #pprint(list2)
        res_list2 = [i for i in res_list if i in list2]#final required list
        dot = Digraph(format='png')
    for x in data2[0]:
        for y in res_list2[0]:
            dot.node(x)
            dot.node(y)
            dot.edge(x, y)
            if y == document_id and x == visitorid:
                dot.attr('node', shape='box', style='filled', fillcolor='green')
            else:
                dot.attr('node', style='filled', fillcolor='white')
    print(dot.source)
    filename = dot.render(filename='img/g1', view=True)
    print(filename + " has been created")








