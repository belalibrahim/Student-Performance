import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
import pandas as pd
import numpy as np
import scipy as sc
import random

students_math = pd.read_csv("dataset/student/student-mat.csv", sep=';')

# Rug plot
sns.stripplot(x="Pstatus", y="G3", data=students_math, jitter=True)
sns.stripplot(x="paid", y="failures", data=students_math, jitter=True)
sns.stripplot(x="nursery", y="G3", data=students_math, jitter=True)
sns.stripplot(x="internet", y="G3", data=students_math, jitter=True)
sns.stripplot(x="internet", y="absences", data=students_math, jitter=True)
sns.stripplot(x="higher", y="G3", data=students_math, jitter=True)
sns.stripplot(x="famrel", y="G3", data=students_math, jitter=True)

# Scatter Plot
sns.jointplot(x="G2", y="G3", data=students_math)
sns.jointplot(x="failures", y="G3", data=students_math)
sns.jointplot(x="absences", y="G3", data=students_math)

sns.jointplot(x="age", y="G3", data=students_math)
sns.jointplot(x="Medu", y="G3", data=students_math)
sns.jointplot(x="traveltime", y="G3", data=students_math)
sns.jointplot(x="studytime", y="G3", data=students_math)

# Histogram Plot
sns.distplot(students_math['G3'])
sns.distplot(students_math['age'])
sns.distplot(students_math['studytime'])
sns.distplot(students_math['traveltime'])
sns.distplot(students_math['absences'])
sns.distplot(students_math["health"])
sns.distplot(students_math["goout"])
plt.hist2d(x="G2", y="G3", data=students_math)
plt.hist2d(x="failures", y="G3", data=students_math)
# Box plot
sns.boxplot(x="paid", y="G3", data=students_math)
sns.boxplot(x="paid", y="studytime", data=students_math)
sns.boxplot(x="sex", y="G3", data=students_math)
sns.boxplot(x="schoolsup", y="G3", data=students_math)
sns.boxplot(x="internet", y="G3", data=students_math)
sns.boxplot(x="guardian", y="G3", data=students_math)
sns.boxplot(x="activities", y="G3", data=students_math)
sns.boxplot(x="freetime", y="G3", data=students_math)

# Statistical description for data
students_math.describe()
students_mean = students_math.mean()
students_std = students_math.std()

# Generate 50 random samples
total_sample_mean = pd.Series()
total_sample_std = pd.Series()
# Generate 50 random samples
for i in range(50):
    # 10 observation per sample
    sample = students_math.sample(n=10)
    sample_mean = sample.mean()
    sample_std = sample.std()

    for j in range(len(sample_mean)):
        key = sample_mean.keys()[j]
        if i == 0:
            total_sample_mean[key] = sample_mean[key]
            total_sample_std[key] = sample_std[key]
        else:
            total_sample_mean[key] += sample_mean[key]
            total_sample_std[key] += sample_std[key]


total_sample_mean /= 50
total_sample_std /= 49
mean_compare = pd.DataFrame([students_mean.values, total_sample_mean.values], columns=students_mean.keys(), index=['Dataset Mean', 'Sample Mean'])
print(mean_compare)
print("\n\n")
std_compare = pd.DataFrame([students_std.values, total_sample_std.values], columns=students_mean.keys(), index=['Dataset STD', 'Sample STD'])
print(std_compare)

# Correlation
students_math.corr()

sns.pairplot(students_math, hue="paid", size=3, kind='scatter').add_legend()
sns.heatmap(students_math.corr())
