import allImports

def createSessioni():
  return SparkSession.builder.appName("cicd").setMaster("local[*]").getOrCreate()


