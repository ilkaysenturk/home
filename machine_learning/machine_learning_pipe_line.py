from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
import pyspark.sql.types as tp
import pyspark.sql.functions as f
from pyspark.ml.feature import StringIndexer#, OneHotEncoderEstimator
sc = SparkContext('local')
spark = SparkSession(sc)


# read a csv file
df = spark.read.csv('ind-ban-comment.csv',header=True)

# see the default schema of the dataframe
df.printSchema()

#Define the schema
# define the schema
df = tp.StructType([
    tp.StructField(name= 'Batsman',      dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Batsman_Name', dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Bowler',       dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Bowler_Name',  dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Commentary',   dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Detail',       dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Dismissed',    dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Id',           dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Isball',       dataType= tp.BooleanType(),   nullable= True),
    tp.StructField(name= 'Isboundary',   dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Iswicket',     dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Over',         dataType= tp.DoubleType(),    nullable= True),
    tp.StructField(name= 'Runs',         dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Timestamp',    dataType= tp.TimestampType(), nullable= True)
])

# read the data again with the defined schema
df = spark.read.csv('ind-ban-comment.csv',schema= df,header= True)

# print the schema
df.printSchema()

# drop the columns that are not required
df = df.drop(*['Batsman', 'Bowler', 'Id',])
df.columns

#show me the dimensions of the data
(df.count() , len(df.columns))

# get the summary of the numerical columns
df.select('Isball', 'Isboundary', 'Runs').describe().show()

# null values in each column
df_agg = df.agg(*[f.count(f.when(f.isnull(c), c)).alias(c) for c in df.columns])

df_agg.show()

# value counts of Batsman_Name column
df.groupBy('Batsman_Name').count().show()

# create object of StringIndexer class and specify input and output column
SI_batsman = StringIndexer(inputCol='Batsman_Name',outputCol='Batsman_Index')
SI_bowler = StringIndexer(inputCol='Bowler_Name',outputCol='Bowler_Index')

# transform the data
df = SI_batsman.fit(df).transform(df)
df = SI_bowler.fit(df).transform(df)

# view the transformed data
df.select('Batsman_Name', 'Batsman_Index', 'Bowler_Name', 'Bowler_Index').show(10)
