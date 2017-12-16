import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
import pandas as pd
import numpy as np
import scipy as sc
import random

students_math = pd.read_csv("dataset/student/student-mat.csv", sep=';')

# Rug plot
sns.stripplot(x="school", y="studytime", data=students_math, jitter=True)
sns.violinplot(x="school", y="studytime", data=students_math, hue="school")
# Scatter Plot
sns.jointplot(x="studytime", y="age", data=students_math, size=5)
# Histogram Plot
plt.hist('studytime', data=students_math)
sns.distplot(students_math['studytime'])
# Box plot
sns.boxplot(data=students_math)

# information about ages
students_math["age"].value_counts()

# Statistical description for data
students_math.describe()
students_mean = students_math.mean()
students_std = students_math.std()

# Generate 50 random samples
for i in range(0, 50):
    # 10 observation per sample
    sample = students_math.sample(n=10)
    sample_mean = sample.mean()
    sample_std = sample.std()

# Correlation
students_math.corr()

sns.pairplot(students_math, hue="school", size=3, kind='scatter', diag_kind='kde').add_legend()
