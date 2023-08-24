import matplotlib.pyplot as plt
import seaborn as sns


def upper_and_lower_limit(column):
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)
    amplitude = q3 - q1
    lower_limit = q1 - 1.5 * amplitude
    upper_limit = q3 + 1.5 * amplitude

    return lower_limit, upper_limit


def exclude_outliers(df, name_column):
    qt_lines = df.shape[0]
    lower_limit, upper_limit = upper_and_lower_limit(df[name_column])
    df = df.loc[
        (df[name_column] >= lower_limit) & (df[name_column] <= upper_limit), :
    ]
    excludes_lines = qt_lines - df.shape[0]

    return df, excludes_lines


def heatmap_corr(df):
    plt.figure(figsize=(15, 10))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Greens")
    plt.savefig("imgs/corr.png")


def box_diagram(column, file_name):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)
    sns.boxplot(x=column, ax=ax1)
    ax2.set_xlim(upper_and_lower_limit(column))
    sns.boxplot(x=column, ax=ax2)
    plt.savefig(f"imgs/{file_name}.png")
    plt.close()


def histogram(column, file_name):
    plt.figure(figsize=(15, 5))
    sns.histplot(column, kde=True, stat="density")
    plt.savefig(f"imgs/{file_name}.png")


def bar_graph(column, file_name):
    plt.figure(figsize=(15, 5))
    ax = sns.barplot(x=column.value_counts().index, y=column.value_counts())
    ax.set_xlim(upper_and_lower_limit(column))
    plt.savefig(f"imgs/{file_name}.png")
