from matplotlib import pyplot as plt
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import dates as mdates
import numpy as np
import urllib
import re


def bytesDateToNum(format, encoding='utf-8'):
    strconverter = mdates.strpdate2num(format)

    def bytesconveter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconveter


def graph_data(stock):

    figure = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))


    stock_price_url = 'http://localhost/analysis/' + stock
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        print(split_line)
        if len(split_line) == 7:
            if 'Date' not in line and 'Open' not in line:
                stock_data.append(line)



    date, closep, highp, lowp, openp, adjclosep, volume = np.loadtxt(
        stock_data,
        delimiter=',',
        unpack=True,
        converters={0: bytesDateToNum('%Y%m%d')})


    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_item = date[x], closep[x], highp[x], lowp[x], openp[x], adjclosep[x], volume[x]
        ohlc.append(append_item)
        x+=1


    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)


    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)



    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("CWX Weekly Report")
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0)
    plt.legend()



    plt.show()

graph_data('cxw.data')