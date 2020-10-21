# Bioinformatics and data sciences for life sciences

### Jesús Urtasun Elizari - University of Milan - 2020/21

Course on R and Python programming, statistics and Machine Learning for life sciences. Roadmap of the course is organized as follows:

## Chapter 1

#### Installing Dependencies
Working under the assumption that most participants have either a MacOS or a Windows operating system, it is crucial for each user to have access to the same software. For this we have decided to use Anaconda, a package manager deployable across Windows, Mac & Linux systems. The first week of the Workshop will be dedicated to making sure each participant has a fully working version of Anaconda. 

A tutorial on how to install Anaconda is available [here](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Getting%20started/Installing%20Anaconda_and_R.md). 

#### Creating a Github account
Github is a free website where users can access code repositories, and create their own repositories to store code, notes and small files of data (max 100MB). As the workshop is being conducted via github, we strongly encourage participants to create a github account. 

A guide on how to set up a Github account, navigate the website and workshop repository is available [here](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Getting%20started/GitHub%20Basics.md). 

#### Linux Subsystem (Windows Users)
A late addition to the workshop, we have decided to cover UNIX shell scripting in week 7. Participants with Linux or Mac OS systems will not need to follow this installation step, as both systems are derivatives of UNIX, sharing core libraries and applications like GNU tools. 

For **windows 10** users, you can install Windows Sub-system for Linux (WSL). This distribution consists of a Linux environment compiled through Windows and enables most native command-line tools, utilities and binaries from Linux to run on Windows: the users can now run Bash scripts and all popular Linux command-line tools like sed, awk, grep, sort, apt, ssh and others. This will allow most participants to engage with week 7 shell scripting exercises. 

A tutorial for windows users to install WSL has been prepared [here](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Getting%20started/wsl_installation.md)

If you don't have windows 10, an alternative installation of Cygwin is offered [here](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Getting%20started/Cygwin%20installation.md)



## Chapter 2

#### Introduction to R (part 1)
A gentle introduction to R Studio and the R programming language, covering the basic syntax of R. Topics covered include data structures in R, creating + calling variables, logical operators, conditional statements, vectors, functions, for loops, while loops and loading packages in R. 


#### Introduction to Python (part 1)
A gentle introduction to Spyder GUI and the Python programming language, covering the basic syntax of Python. Topics covered include data structures in Python, creating + calling variables, logical operators, conditional statements, for loops,and  while loops. 



## Chapter 3

#### Introduction to R (part 2)
Working with matrices in R, reading text/csv files into dataframes and performing maniuplations, operations and subsetting using base `R` functions. 

#### Introduction to Python (part 2)
Working with dataframes in Python using `numpy` and `pandas` libraries. Perform operations and tasks on the dataframes and write to files. 



## Chapter 4

#### Introduction to R (part 3)
This tutorial covers creating plots using base R and is extended to cover the `ggplot` package. Further packages for visualizations are provided in the teaching materials. 

#### Introduction to Python (part 3)
This tutorial covers creating plots in Python, using the popular `matplotlib` library and the increasingly popular `seaborn` library. 



## Chapter 5

#### Math and Statistics (R)
This tutorial has 3 parts:

**1)** Descriptive statistics for single variable and multivariable datasets including measures of central tendency, variability and quantiles, along with distributions, the Central Limit Theorem and confidence interval for the mean.

**2)** Hypothesis testing in the form of 2-samples comparison (the t-test, non-parametric test) and correlation tests (parametric and non-parametric)

**3)** Linear regression analysis

#### Math and Statistics (Python)
This tutorial is split into 3 parts and covers:

**1)** Descriptive statistics for single variable and multivariable datasets including measures of central tendency, variability and quantiles, along with distributions, the Central Limit Theorem and confidence interval for the mean.

**2)** Hypothesis testing in the form of 2-samples comparison (the t-test, non-parametric test) and correlation tests (parametric and non-parametric)

**3)** Linear regression analysis



## Chapter 6

#### Machine Learning (R) 
Distance metrics, clustering methods in unsupervised machine learning, visualised as dendograms and heatmaps. Dimensionality reduction using PCA, visualising Principal components in bi plots. Supervised machine learning covering data pre-processing and cleaning, creating training and test sets and implementing KNN, RF and Elastic net machine learning models. 

#### Machine Learning (Python)
Introductory course on Python Machine Learning libaries (e.g. TensowFlow and Keras), linear regression and Neural Networks.
For a mor specific course about Machine Learning visit [https://github.com/JesusUrtasun/MLcourse](https://github.com/JesusUrtasun/MLcourse)
