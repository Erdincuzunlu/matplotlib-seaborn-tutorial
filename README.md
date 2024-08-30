# matplotlib-seaborn-tutorial
“Basic data visualization examples with Python.”

Data Visualization with Matplotlib & Seaborn

This repository contains examples and tutorials on basic data visualization techniques using Python, specifically focusing on Matplotlib and Seaborn libraries.

Table of Contents

	•	Introduction
	•	Installation
	•	Usage
	•	Examples
	•	Categorical Data Visualization
	•	Numerical Data Visualization
	•	Subplots and Multiple Lines
	•	Seaborn Examples
	•	Contributing

 Installation

To run the examples in this repository, you’ll need to have Python installed along with the necessary libraries. You can install the required libraries using pip:
pip install matplotlib seaborn numpy pandas

Usage

You can clone this repository and explore the examples provided. Each section demonstrates different types of visualizations:

git clone https://github.com/your-username/data-visualization-examples.git
cd data-visualization-examples

Open the Jupyter Notebook or run the Python scripts directly to see the visualizations in action.


Examples

Categorical Data Visualization

Visualize categorical data using bar plots and count plots.


df["sex"].value_counts().plot(kind='bar')
plt.show()

sns.countplot(x=df["sex"], data=df)
plt.show()

Numerical Data Visualization

Visualize numerical data using histograms and box plots.

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

Subplots and Multiple Lines

Create subplots and plot multiple lines to compare data.

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("Plot 2")

plt.show()


Seaborn Examples

Explore more advanced visualizations with Seaborn.

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()


Contributing

Contributions are welcome! If you have any improvements or additional examples, feel free to submit a pull request.
