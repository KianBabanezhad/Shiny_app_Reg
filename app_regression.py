import pandas as pd
import plotly.express as px
from shiny.express import input, render, ui
from shiny import reactive
from shinywidgets import render_widget # type: ignore
from matplotlib import pyplot as plt
import seaborn as sb
 
ui.page_opts(title="2D Regression:", fillable=True)
 
with ui.sidebar():
    ui.input_file("file_upload", "Choose CSV File", accept=[".csv"], multiple=False)
    ui.input_select("x", "X", choices=[])
    ui.input_select("y", "Y", choices=[])
    ui.input_select("n_order", "Regression Order", choices=[1,2,3,4,5])
    ui.input_action_button("action_button", "Run", style="color: #fff; background-color: #337ab7; border-color: #2e6da4")
 
with ui.navset_card_underline(title="Result"):
    with ui.nav_panel("Table"):
        @render.data_frame
        def show_table():
            file = input.file_upload()
            if file:
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                return df
             
    with ui.nav_panel("Plot"):
        @render.plot()
        def plot():
            file = input.file_upload()
            if file and input.action_button():
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                with reactive.isolate():
                    x = df[input.x()]
                    y = df[input.y()]
                    n = int(input.n_order())
                sb.regplot(data=df,x=x,y=y,order=n)
 
 
        @reactive.effect
        def _():
            file = input.file_upload()
            if file:
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                ui.update_select("x",choices=df.columns.tolist())
                ui.update_select("y",choices=df.columns.tolist())