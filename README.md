# Smarking-G16
Smarking Challenge Project: Parking Prediction, Group 16

***
# Parking Prediction (Smarking Challenge)

## Description
This is a [micro Bittiger project](https://www.bittiger.io/microproject/jEaqRv4rurDJ6BhNm) provided by Smarking Inc, and it's part of the application for their software engineering position. We will use the given data set to build prediction models and provide an interactive web application for users to observe predicted results, upload actual data, compare the real and predicted data, and check the accuracy.


## Plan

### Todo List
- [ ] Data Analysis
- [ ] Prediction Model Building
- [ ] Interactive Web Visulization

### Time Schedule


| Stage | Start  | End | Goals |
| ------------- | ------------- | ------------- | ------------- |
| s | 06/07/16  | 06/13/16  | GitHub-Repo-Team, Proposal Writing, Video Learning, Group Discussion |
| 1 | 06/14/16  | 06/20/16  | Knowledge Learning (data analysis and machine learning), Data Preprocessing, Prediction Model Training, Group Discussion, Model Selection and Analysis  |
| 2 | 06/21/16  | 06/27/16  | Accuracy Improvement, Knowledge Learning(web page), Web Page Design, Interactive Web Page Prototyping  |
| 3 | 06/28/16  | 07/04/16  | Accuracy Improvement, Visualization and Application Idea Generation |
| 4 | 07/05/16  | 07/11/16  | Web Page Refinement |
| e | 07/12/16  | 07/18/16  | Project Report Writing, Demo Video Making |



## Resource

- [太阁x直播7 实战Data Science全栈项目](https://www.bittiger.io/classpage/FKdk6888kdkij6Rqh)
- [Coursera Machine Learning] (https://www.coursera.org/learn/machine-learning)
- [Interactive Data Visualization] (http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/)
- [Project Requirements](https://www.bittiger.io/microproject/jEaqRv4rurDJ6BhNm)
- [Proposal Template](https://github.com/hackjustu/Handbook-GitHub-Projects/blob/master/proposal_template.md)
+ Source Code
   + [HuangFang](https://github.com/fanghuang/Parking-Prediction)
+ D3 & Dimple: Useful Examples
   + [Data Visualization on Dashboard](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/)
   + [Comparison of Multiple Lines](http://dimplejs.org/examples_viewer.html?id=lines_horizontal_stacked)
   + [Calendar View](http://bl.ocks.org/mbostock/4063318)


## License
This project is distributed under the [MIT license](http://choosealicense.com/licenses/mit/).

## Project Information
- category: data science, machine learning
- team: Smart
- description: Predict the parking transaction and visualize data and the model accuracy.
- stack: python, r, html, css, javascript, d3.js



### Weekly Report
***
#####2016/6/7 - 2016/6/13

**Plan**

| # | DDL | Task | Results |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 05/30/16  | Team Building | Introduction of every member, team leader selected |
| 2 | 06/04/16  | Team Meeting  | Held first meeting, cc shared some experience and resources about this project, and answered many questions for our team. Built Trello, Google Drive for team to management project and share docs |
| 3 | 06/06/16  | GitHub | Built Repo on GitHub, added team members  |
| 4 | 06/07/16  | Proposal | Finished simple proposal |
| 5 | 06/10/16  | Video Learning | Watched the video about how to do full stack data science ananlysis shared by Bittiger. Wrote some basic codes  |

**Do**

| Content | DT |  | Description |
| ------------- | ------------- | ------------- | ------------- |
| ToDo | 06/11/16  | Weekly Meeting on Sat. | After learning the video, each member shares opinion on the process of prediction analysis and web building. Make next week schedule. Pains and gains last week. Problems to overcome.  |
| **Problems Encountered** | 06/10/16  |  | One of our team members Yuhan finds it hard to keep up our project because of her personal reason in this two weeks. Therefore, our group has only 2 members and the difficulty of finishing the project will be increased.  |
| **Lessons Learned & Strategies to address Problems** | 06/10/16  |  | During the self-learning, we have a deeper understanding of our project and what to do next. Since we only have 2 persons to work on the project in this two weeks, we need to spend more time on learning and working. |

***
#####2016/6/14 - 2016/6/20

**Plan**

| # | DDL | Task | Results |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 06/17/16  | Knowledge Learning | Knowledge Learning (data analysis and machine learning), Data Preprocessing, Prediction Model Training  |
| 2 | 06/18/16 | Team Meeting  | Group Discussion: Model Selection and Analysis |
| 3 | 06/19/16  | Weekly Report | Update Weekly Progress to Bittiger blog docs, push codes to Repo  |

**Do**

| Content | DT |  | Description |
| ------------- | ------------- | ------------- | ------------- |
| **Problems Encountered** | 06/16/16  |  | Not familiar with Python to do visulization and statics analysis, coding speed is slow. For Rex, he has little experience in data analysis and he is working as well. Therefore, the learning pace is quite slow. He needs to spend more time to learn and work. |
| **Lessons Learned & Strategies to address Problems** | 06/18/16  |  | We have started the data analysis process and our group member Alice has updated the code. We will move on model selection to improve our analysis. However, more discussion is needed to improve the learning efficiency and  work distribution.  |

**Check List**

- [ ] Knowledge Learning (data analysis and machine learning)
- [x] Data Preprocessing
- [ ] Prediction Model Training
- [x] Group Discussion
- [ ] Model Selection and Analysis
- [x] Update Weekly Progress
- [x] push codes to Repo


***
#####2016/6/21 - 2016/6/27

**Plan**

| # | DDL | Task | Results |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 06/27/16  | Knowledge Learning | Knowledge Learning (data analysis and machine learning) from Coursera |
| 2 | 06/22/16 | Feature Selection  | Create features list |
| 3 | 06/23/16 | Models Training  | Train first model to see basic result |
| 4 | 06/24/16 | Models Training  | Train more models to incresse score |
| 5 | 06/25/16 | Team Meeting  | Next week to do list & problems met this week |
| 6 | 06/26/16  | Weekly Report | Update Weekly Progress to Bittiger blog docs, push codes to Repo  |


**Do**

| Content | DT |  | Description |
| ------------- | ------------- | ------------- | ------------- |
| **Problems Encountered** | 06/21/16  |  | 1. Not familiar with Feature Engineering & Parameters Tuning. 2. Seems a little difficult to learn all algorithms in Sklearn in a short time.  |
| **Lessons Learned & Strategies to address Problems** | 06/25/16  |  | 1. Firstly, generate a score table to compare, then try SVR和ensembling. 2. cc shares a leaning method.  |

**Check List**

- [x] Knowledge Learning (data analysis and machine learning)
- [x] Prediction Model Training
- [x] Group Meeting
- [ ] Model Selection and Analysis
- [x] Update Weekly Progress
- [x] push codes to Repo


***
#####2016/6/28 - 2016/7/4

**Plan**

| # | DDL | Task | Results |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 06/28/16  | Web & Accuracy | Rex is responsible for 2 visulization graphs. Alice is to create score table, train SVR, and learn ensembling  |
| 2 | 06/29/16 | Web & Accuracy  | Rex: more visulization graphs. Alice: time series model |
| 3 | 06/30/16 |   |  |
| 4 | 07/01/16 |  |  |
| 5 | 07/02/16 |   |  |
| 6 | 07/03/16 | Team Meeting  | Next week to do list & problems met this week |
| 7 | 07/04/16  | Weekly Report | Update Weekly Progress to Bittiger blog docs, push codes to Repo  |

**Do**

| Content | DT |  | Description |
| ------------- | ------------- | ------------- | ------------- |
| **Done** | 07/03/16  |  | 1. Combined daily data into weekly data and fitted by polynomial.   2.  Modified by outlier. |
| **Problems Encountered** | 07/02/16  |  | 1. Project pace is relatively slow. 2. Rex still had trouble finishing his task. 3. The score is still not high enough.  |
| **Lessons Learned & Strategies to address Problems** | 06/25/16  |  | 1. Need to try more modified method to improve the score. 2. Everyone should show their strength to work on the project.  |

**Check List**

- [ ] Web visulization
- [x] Increase Accuracy
- [ ] Group Meeting
- [x] Update Weekly Progress
- [x] push codes to Repo

***
#####2016/7/3 - 2016/7/10

**Plan**

| # | DDL | Task | Results |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 07/09/16  | Web & Accuracy | Web visulization  |
| 2 | 07/08/16 | Web & Accuracy  | Improve the accuracy |
| 3 | 07/10/16 | Team Meeting  | Next week to do list & problems met this week |
| 7 | 07/11/16  | Weekly Report | Update Weekly Progress to Bittiger blog docs, push codes to Repo  |

**Check List**

- [ ] Web visulization
- [ ] Increase Accuracy
- [ ] Group Meeting
- [ ] Update Weekly Progress
- [ ] push codes to Repo
