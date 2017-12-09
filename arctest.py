import arcpy
arcpy.env.workspace = "C:/Data"
myresult = arcpy.annalysisi.Clip("","","")
print(myresult)