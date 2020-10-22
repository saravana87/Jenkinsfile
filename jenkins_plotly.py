from pyspark import SparkContext
from pyspark.sql import SQLContext
import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
import requests
import plotly.express as px

sc = SparkContext("local", "First App")
sqlContext = SQLContext(sc)
#requests.packages.urllib3.disable_warnings()
df = sqlContext.read.format("com.databricks.spark.csv") 
     \.options(header='true', inferschema='true').load("births.csv")
df.registerTempTable("births")
df3= sqlContext.sql("SELECT * from births")
df = px.data.iris()
fig = px.scatter(pandf, x=df3.toPandas()['year'], y=df3.toPandas()['births'], color=df3.toPandas()['gender'])
fig.show()
