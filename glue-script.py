import allImports
import sessionCreation

spark = createSession()

input_path = "s3://my-bucket-2024-05-30-new/input/emp.txt"
output_path = "s3://my-bucket-2024-05-30-new/output/emp.json"

df = spark.read.format("csv").load(input_path)

df.coalesce(1).write.mode("overwrite").format("json").save(output_path)
