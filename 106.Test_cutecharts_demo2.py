from cutecharts.charts import Radar
from cutecharts.faker import Faker

chart = Radar("Radar-基本示例")
chart.set_options(labels=Faker.choose())
chart.add_series("series-A", Faker.values())
chart.add_series("series-B", Faker.values())
chart.render()
