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

# Scatter Plot
#sns.jointplot(x="Medu", y="G3", data=students_math)
sns.jointplot(x="G2", y="G3", data=students_math)
sns.jointplot(x="failures", y="G3", data=students_math)
sns.jointplot(x="absences", y="G3", data=students_math)

sns.jointplot(x="age", y="G3", data=students_math)
sns.jointplot(x="traveltime", y="G3", data=students_math)
sns.jointplot(x="failures", y="absences", data=students_math)
sns.jointplot(x="studytime", y="G3", data=students_math)

# Histogram Plot
plt.hist(x='G3', data=students_math)
plt.hist2d(x="G2", y="G3", data=students_math)
plt.hist2d(x="failures", y="G3", data=students_math)
# sns.distplot(students_math['studytime'])
# Box plot
sns.boxplot(x="paid", y="G3", data=students_math)
sns.boxplot(x="paid", y="studytime", data=students_math)
sns.boxplot(x="internet", y="G3", data=students_math)
sns.boxplot(x="guardian", y="G3", data=students_math)
sns.boxplot(data=students_math)

# information about ages
students_math["age"].value_counts()

# Statistical description for data
students_math.describe()
students_mean = students_math.mean()
students_std = students_math.std()

# Generate 50 random samples
total_sample_mean = {}
total_sample_std = {}
# Generate 50 random samples
for i in range(0, 50):
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

for key in total_sample_mean:
    total_sample_mean[key] /= 50
    total_sample_std[key] /= 50


# Correlation
students_math.corr()

sns.pairplot(students_math, hue="school", size=3, kind='scatter', diag_kind='kde').add_legend()
