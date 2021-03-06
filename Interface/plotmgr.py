import matplotlib.pyplot as p;
p.switch_backend("SVG")
import mpld3
import seaborn as sns; sns.set()

def Axis_FactorPlot(data, x, y=None, hue=None, row=None, col=None, kind="point"):
    sns.set(style="ticks")
    ax = sns.factorplot(x=x, y=y, hue=hue, data=data, kind=kind, row=row, col=col)
    d = mpld3.fig_to_dict(ax.fig)
    return d

def Axis_LMPlot(data, x, y=None, hue=None):
    sns.set(color_codes=True)
    ax = sns.lmplot(x=x, y=y, hue=hue, data=data)
    d = mpld3.fig_to_dict(ax.fig)

    return d

def Axis_PairPlot(data, vars=None, hue=None):
    g = sns.pairplot(data, hue=hue, vars=vars)
    d = mpld3.fig_to_dict(g.fig)
    return d

def Axis_JointPlot(data, x, y, kind="scatter"):
    sns.set(style="white", color_codes=True)
    g = sns.jointplot(x, y, data, kind)
    d = mpld3.fig_to_dict(g.fig)

    return d

def Cat_StripPlot(data, x, y, hue=None, jitter=False):
    sns.set_style("whitegrid")
    g = sns.stripplot(x, y, data, hue=hue, jitter=jitter)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_SwarmPlot(data, x, y=None, hue=None):
    sns.set_style("whitegrid")
    g = sns.swarmplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_BoxPlot(data, x, y=None, hue=None):
    sns.set_style("whitegrid")
    g = sns.boxplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_ViolinPlot(data, x, y=None, hue=None):
    sns.set_style("whitegrid")
    g = sns.violinplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_LVPlot(data, x, y=None, hue=None):
    sns.set_style("whitegrid")
    g = sns.lvplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_PointPlot(data, x, y, hue=None):
    sns.set_style("whitegrid")
    g = sns.pointplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_BarPlot(data, x, y, hue=None):
    sns.set_style("whitegrid")
    g = sns.barplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Cat_CountPlot(data, x, y, hue=None):
    sns.set_style("whitegrid")
    g = sns.countplot(x, y, data, hue=hue)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Reg_RegPlot(data, x, y):
    sns.set_style("whitegrid")
    g = sns.regplot(x, y, data)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Reg_KDEPlot(data, x, y):
    sns.set_style("whitegrid")
    dx = data[x]
    dy = data[y]
    g = sns.kdeplot(dx, dy)
    d = mpld3.fig_to_dict(g.figure)
    return d

def Reg_RugPlot(data, x):
    sns.set_style("whitegrid")
    dx = data[x]
    g = sns.rugplot(dx)
    d = mpld3.fig_to_dict(g.figure)
    return d
