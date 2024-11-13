# 📊 Matplotlib and Seaborn Cheat Sheet

## 🔍 Introduction

**Matplotlib** and **Seaborn** are powerful Python libraries for data visualization:

- **Matplotlib**: The foundational plotting library in Python, offering extensive customization for creating static, animated, and interactive visualizations.
- **Seaborn**: Built on top of Matplotlib, it provides a higher-level interface for creating attractive and informative statistical graphics with less code.

---

## 🛠️ Installation

```bash
pip install matplotlib seaborn
```

Or, if using Anaconda:

```bash
conda install matplotlib seaborn
```

---

## 📦 Importing Libraries

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 🎨 Matplotlib Basics

### Line Plot

```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
```

### Scatter Plot

```python
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### Bar Plot

```python
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='green')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

### Histogram

```python
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Customization

- **Figure Size**: `plt.figure(figsize=(width, height))`
- **Title and Labels**:

  ```python
  plt.title('Title')
  plt.xlabel('X-axis Label')
  plt.ylabel('Y-axis Label')
  ```

- **Grid**: `plt.grid(True)`
- **Legends**:

  ```python
  plt.legend(['Label 1', 'Label 2'])
  ```

- **Saving Figures**:

  ```python
  plt.savefig('filename.png', dpi=300, bbox_inches='tight')
  ```

---

## 🎨 Seaborn Basics

### Setting Style

```python
sns.set_style('whitegrid')  # Options: darkgrid, whitegrid, dark, white, ticks
sns.set_palette('pastel')   # Set color palette
```

### Histogram

```python
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='column_name', bins=20, kde=True)
plt.title('Histogram with Seaborn')
plt.show()
```

### KDE Plot

```python
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='column_name', shade=True)
plt.title('Kernel Density Estimate Plot')
plt.show()
```

### Box Plot

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='categorical_column', y='numerical_column', data=df)
plt.title('Box Plot')
plt.show()
```

### Violin Plot

```python
plt.figure(figsize=(10, 6))
sns.violinplot(x='categorical_column', y='numerical_column', data=df)
plt.title('Violin Plot')
plt.show()
```

### Bar Plot

```python
plt.figure(figsize=(10, 6))
sns.barplot(x='categorical_column', y='numerical_column', data=df)
plt.title('Bar Plot with Seaborn')
plt.show()
```

### Count Plot

```python
plt.figure(figsize=(10, 6))
sns.countplot(x='categorical_column', data=df)
plt.title('Count Plot')
plt.show()
```

### Scatter Plot with Regression Line

```python
plt.figure(figsize=(10, 6))
sns.regplot(x='x_column', y='y_column', data=df, scatter_kws={'alpha':0.5})
plt.title('Scatter Plot with Regression Line')
plt.show()
```

### Heatmap

```python
plt.figure(figsize=(10, 6))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```

### Pair Plot

```python
sns.pairplot(df, hue='categorical_column')
plt.show()
```

---

## 🔧 Customization and Styling

### Change Color Palette

```python
sns.set_palette('Set1')  # Other options: 'Set2', 'Set3', 'Blues', 'BuGn', etc.
```

### Adjusting Aesthetics

```python
sns.set_context('talk')  # Options: paper, notebook, talk, poster
```

### Adding Annotations

```python
plt.annotate('Text', xy=(x_point, y_point), xytext=(x_text, y_text),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
```

---

## 🗂️ Subplots

### Creating Multiple Plots in One Figure

```python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plot in the first subplot
axes[0, 0].plot(x, y)
axes[0, 0].set_title('First Plot')

# Plot in the second subplot
axes[0, 1].bar(categories, values)
axes[0, 1].set_title('Second Plot')

# Adjust layout
plt.tight_layout()
plt.show()
```

---

## 📑 Additional Tips

- **Rotate X-axis Labels**:

  ```python
  plt.xticks(rotation=45)
  ```

- **Log Scale Axis**:

  ```python
  plt.yscale('log')
  ```

- **Handling Missing Data in Seaborn**:

  ```python
  sns.heatmap(df.isnull(), cbar=False)
  ```

- **Faceting with Seaborn**:

  ```python
  g = sns.FacetGrid(df, col='categorical_column')
  g.map(plt.hist, 'numerical_column')
  plt.show()
  ```

---

## 🐍 Example Workflow

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('your_dataset.csv')

# Set style
sns.set_style('whitegrid')

# Create a figure
plt.figure(figsize=(10, 6))

# Plot data
sns.histplot(data=df, x='Age', bins=30, kde=True)

# Customize plot
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show plot
plt.show()
```

---

## 📚 References

- **Matplotlib Documentation**: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- **Seaborn Documentation**: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)