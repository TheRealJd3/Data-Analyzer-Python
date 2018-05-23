import matplotlib.pyplot as plt
#Reference :https://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py
def plothistogram(title, x_axis, y_axis, orientation='vertical'):
    #Checks for orientation by def. vertiacal histograms more pleasing to the eye
    #Slides was additional resoource
    if orientation=='vertical':
        histogram = plt.bar
        histogramlabel = plt.ylabel
        histogramticks = plt.xticks
    elif orientation=='horizontal':
        histogram = plt.barh
        histogramlabel = plt.xlabel
        histogramticks = plt.yticks
    else:
        raise Exception ('plot_histo: Invalid orientation')

    length = len(x_axis)
    histogramticks(range(length), x_axis)
    histogram(range(length), y_axis, align='center',alpha=0.4)
    histogramlabel('Number of times document is accessed')
    plt.title(title)
    plt.show()
