import pandas as pd
import plotly.express as px
import plotly
import matplotlib.pyplot as plt
from FPT.vo.pd_mapping_vo import PDMappingVO

def plot_base_date(df : pd.DataFrame) -> None:
    plt.figure()
    for col in df.columns:
        if col == PDMappingVO.DATE_COLUMN:
            continue
        plt.plot(df[PDMappingVO.DATE_COLUMN], df[col], label = col)
        
    plt.legend(loc=PDMappingVO.UPPER_LEFT)
    plt.xticks(range(0,len(df)+10,5),rotation=90)
    plt.show()

def plot_plotly_date(df : pd.DataFrame,title :str = "") -> None:
    fig = px.line(df, x="date", y=df.columns, title=title)
    fig.update_layout(xaxis=dict(tickformat="%d-%m-%Y"))
    fig.show()
    # plotly.offline.plot(fig)

def plot_plotly(df : pd.DataFrame,title :str = "") -> None:
    fig = px.line(df, x=df.index, y=df.columns, title=title)
    # plotly.offline.plot(fig)
    fig.show()

    