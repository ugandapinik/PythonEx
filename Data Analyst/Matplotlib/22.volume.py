from matplotlib.finance import candlestick_ohlc
from matplotlib import ticker as mticker
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from matplotlib import style
from pyparsing import col
import numpy as np
import urllib
import re

MA1 = 10
MA2 = 30

style.use("fivethirtyeight")



def high_minus_low(highs, lows):
    return highs - lows


highs = [11, 12, 15, 14, 13]
lows = [5, 6, 2, 6, 7]

h_l = list(map(high_minus_low, highs, lows))



def moving_average(value, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(value, weights, 'valid')
    return smas



def bytesDateToNum(format, encoding='utf-8'):
    strconverter = mdates.strpdate2num(format)

    def bytesconveter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconveter


def graph_data(stock):

    stock_price_url = 'http://localhost/analysis/' + stock + '.data'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    figure = plt.figure()

    # Plot in axis 1
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)

    # Plot in axis 2
    plt.title(stock)
    plt.ylabel("H-L", fontsize=12)
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1, sharex=ax1)

    # Plot in axis 3
    plt.ylabel("Price", fontsize=12)
    ax2v = ax2.twinx()
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel("MAvgs", fontsize=12)


    # Prepare Data
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        # print(split_line)
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

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2 - 1:])
    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date[-start:], h_l[-start:], '-', linewidth=1)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='lower'))
    ax1.tick_params(labelsize=8)



    # AXIS DISPLAY
    candlestick_ohlc(ax2, ohlc[-start:], width=0.4, colorup='g', colordown='r')



    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
    ax2.tick_params(labelsize=8)
    ax2.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext=(date[-1] + 4, closep[-1]), bbox=bbox_props)

    ax2v.fill_between(date[-start:], 0, volume[-start:], facecolor='#0079a3', alpha=0.5)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.set_ylim(0, 1*volume.max())
    ax2v.grid(False)

    # Plot ax3
    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r',
                     edgecolor='r',
                     alpha=0.5)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g',
                     edgecolor='g',
                     alpha=0.5)


    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    ax3.tick_params(labelsize=8)

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)


    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)

    # plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.87, top=0.90, wspace=0.2, hspace=0)

    plt.show()

graph_data('tsla')