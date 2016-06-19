
***
#### G16 Group Meeting

##### Project #: 16                         
##### Project Title: Parking Prediction

##### Date: June 11, 2016 

##### Members: cc, Rex, Alice


***

####1.修改的proposal：
**精度目标**：93%

**下周任务** ：分析数据和学习模型

| Stage | Start  | End | Goals |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 06/14/16  | 06/20/16  | Knowledge Learning (data analysis and machine learning), Data Preprocessing, Prediction Model Training, Group Discussion, Model Selection and Analysis |


####2.看视频所得想法：
流程是比较基本的预测分析的

数据分析的时间多一些，我的想法是，大概是分四步 比较难的是如何预测好 和如何改进

**分析部分大体流程：**
预处理->提出feature->可视化->预测


####3.分析怎么做：
1. 坏的数据：除了entry大于exit的时间，还有其他
2. 坏的数据怎么处理：可以忽略，如果坏的数据量比较大，还可以修复
3. 构造：每天，每小时，有多少车

4. 控制检验：两种不同的处理方法，结果有多大影响
5. 问问题，作为提取feature的基础：
1.一天内，24小时的分布，每天上班下班这些时候车流不同  2.一周内，曜日的分布，周六日 假日什么的  3.年与年之间的同周同曜日的分布  4.节假日增减

6. 可视化展示内容：
项目要求：预测实际对比
探索式分析：
周末与平日有怎样的区别
某个月
同一天的不同时段

7. 可视化summary；
平均值等，不同角度来提取feature

8. 使用机器学习方法:
数据清洗，提取feature，可视化之后：
PCA，LDA：feature selection的方法，是否相关，相关性，用不同方法考察feature是否好用
Linear Regression等方法，看效果，分析
看假设是否正确：比如周末是否真的有影响，要根据分析结果确定
先用基本模型去做，后续再用比较复杂的模型，尽量查多些模型，看它们的假设，判断这个模型是否可用。
比如naive bayes，
每个模型有个假设，一个句子有几个重要的单词，一封信判断是否为垃圾邮件，假设是每个单词的贡献是独立的，但其实是不独立的，因为前后文是有关系的。

9. 学习资料：主要看这个模型是干什么的
python的常用library
机器学习算法的短视频
深度学习

10. 评测这个模型好不好用：
有很多标准，可以讨论，不同标准考察的地方不一样
比如mean square
sklearn库里很多

**kaggle的两个重要的事情是：**
feature engineering：selection
tuning parameters：怎么调－Cross Validation



####4.其他内容
项目6周的时间安排

工具：
status report
ipython notebook





