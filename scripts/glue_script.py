import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data directly from S3
source_path = "s3://myglue-bucket-83-new/input/sample.csv"
df = spark.read.format("csv").option("header","true").load(source_path)
df.printSchema()  



# Convert to JSON format
json_path = "s3://myglue-bucket-83-new/output/output.json"
df.write.mode("overwrite").format("json").save()

job.commit()
