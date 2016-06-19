
***

#### G16 Group Meeting

##### Project #: 16                         
##### Project Title: Parking Prediction

##### Date: June 18, 2016 

##### Members: cc, Rex, Alice

***

###1.下周任务：
根据文档做更加细致的分析

###2.目前问题：
现在分析过程就是分开，自己做的比较慢，大家没有基础，是来学习。
是python的函数不熟悉，还是统计的流程不熟悉？
分析的思路可以自己做，能够协同的就一起做，分工更细致。

###3.下周解决方案：
1. 在群里有问题直接问
2. 更细化的任务分工
3. 三个人一起写一本书：
这个项目会用到的，常用的命令，都可以更新上去
形式：
1.提纲，更新，目录
2.正文
4. 电子书：硅谷进阶之路

###4.实际中的问题 & 解答& To Do
![分析遇到问题](http://upload-images.jianshu.io/upload_images/1667471-2f8249379b3635c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1. 2012年的数据不需要用
2. 一天24小时的形状，看起来像正态分布，偏正态分布，这个偏移有一定规律的
3. 一周内，周二周四会比其他多一些，这个属于 Feature Engineering 的，可以融合到模型里 （Feature Engineering的入门基础资料分享）
4. part-3: 1-week-7-day，这个图里，现在做的每一天合计了24小时的，也可以看平均值，中值的比较
5. holiday，比较这些假期和美国实际的假期是否一致
6. Feature Selection的方法：PCA，ICA
现在主要是时间Feature
Markov链，可以用于有隐含条件的模型，现有的是时间，隐含的因素比如经济危机等，是可以从时间去预测的
7. 提高精度方法：
提高相关度，例如，AC差异大，BD差异大，直接把AB，CD归为一类。
或者观察数据，看哪些feature比较重要。
具体分析时再看怎么做才能提高。
8. cross validation是用来调参数的：
但是在时间序列数据里，最好是不要随机分，分的方法，最好是用过去的数据去预测未来的数据。
9. 除了mean square score
10. 除了正态分布，停车这件事可以用possion模型去做
总体形状一样，但是具体参数不一样
可以把这个参数当作对象，去做预测
可以用Markov，time series，RNN等去做
11. 调参：cross validation本身就是在调参了，还有其他的方法再看







