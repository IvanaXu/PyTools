from cutecharts.charts import Line

chart = Line("某商场销售情况")
chart.set_options(
    labels=["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"],
    x_label="I'm xlabel",
    y_label="I'm ylabel",
)
chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])
chart.render()
