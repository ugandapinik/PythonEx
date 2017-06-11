from matplotlib import pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytesDateToNum(format, encoding='utf-8'):
    strconverter = mdates.strpdate2num(format)

    def bytesconveter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconveter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))




    stock_price_url = 'http://localhost/' + stock
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' not in line and 'Open' not in line:
                stock_data.append(line)

    print(stock_data)

    date, closep, highp, lowp, openp, adjclosep, volume = np.loadtxt(
        stock_data,
        delimiter=',',
        unpack=True,
        converters={0: bytesDateToNum('%Y%m%d')}
        )


    ax1.plot_date(date, highp, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='grey')


    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Tesla Company Selling")
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0 )
    plt.legend()



    plt.show()

graph_data('tsla.data')