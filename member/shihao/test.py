#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 24
menMeans = (43,41,38,39,58,195,767,1586,2141,2318,2353,2373,2339,2336,2309,2237,2018,1390,680,280,150,114,98,78)


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='g', yerr=0.01)



# add some text for labels, title and axes ticks
ax.set_ylabel('2014-06-30')
ax.set_title('daily parking number in different hours')
ax.set_xticks(ind + width)
ax.set_xticklabels(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'))

ax.legend((rects1,), ('parking number',))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.002*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)


plt.show()
