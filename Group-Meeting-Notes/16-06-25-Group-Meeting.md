***
#### G16 Group Meeting

##### Project #: 16                         
##### Project Title: Parking Prediction

##### Date: June 25, 2016 

##### Members: cc, Rex，Alice

***



###1.下周任务：

［最好周一完成］
######Rex:
每天parking的车的代码：daily hour count，转化成excel。要在这之上做可视化:

1. 第一个可视化是我想你用python matplotlib（也可以做其他工具）对每一天产生一张直方图。如果能任意选多个时间（不同的天）进行对比是最好不过
2. 第二个是做全部时间的calendar view，参照[这个](http://bl.ocks.org/mbostock/4063318)
3. ＋更多可视化


######Alice 
1. 把之前试过的模型以及得到的参数，用的具体调参方法（譬如cross validation具体是怎样的cv）做个表格
2. ＋继续训练更多模型，采用更多方法，争取精度93%：
试一下[support vector regression](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)，然后学习一下[ensembling](后面会用到，http://scikit-learn.org/stable/modules/ensemble.html)
3. 如果这个做到快，尝试把之前说的time series model做出来。


###2.目前问题 & 解决方案：
######Q：
cc sklearn里那么多模型，你都是怎么学习的呢
######A：
最开始也是一个个学，但是学得后面意识到每个模型都有它的理由。然后就按照类别学了，譬如random forest 是 decision tree 使用 ensembling methods，我并不需要知道每个ensembling methods的细节，我只要把random forest学好，而了解那些模型与rf的区别与联系，在以后做模型的时候能够想起来，到时再看细节就好。

######Q：
现在比较想学一学怎么调参，就比如用linear regression算出score是0.7的时候，怎么去调高呢，这个是需要对所有可以用的算法都有所了解之后才能够有方向的吧？该怎么思考呢，这个有没有相关的材料可以学学呢，还是就是每一个都去试一下呢
######A：
调参数只要你了解这个算法本身，我也给你找些调参的资料。你先看一下[这个](http://scikit-learn.org/stable/modules/grid_search.html)



