from pyspark import SparkContext
from pyspark.sql import SQLContext
import plotly.graph_objs as go
import pandas as pd
import requests
import plotly.express as px

sc = SparkContext("local", "First App")
sqlContext = SQLContext(sc)
#requests.packages.urllib3.disable_warnings()
pandf = pd.read_csv("births.csv", header=0)
df = sqlContext.read.format("com.databricks.spark.csv") \
     .options(header='true', inferschema='true').load("births.csv")
df.registerTempTable("births")
df3= sqlContext.sql("SELECT * from births")
fig1 = px.scatter(df3.toPandas(), x=df3.toPandas()['year'], y=df3.toPandas()['births'], color=df3.toPandas()['gender'])
fig1.show()
fig2= px.histogram(y=df3.toPandas()['births'],x=df3.toPandas()['year'])
fig2.show()
