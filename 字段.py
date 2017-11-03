#Import geoprocessing
import arcpy

#Set workspace
arcpy.env.workspace = r'C:\Data\Garbo.gdb'

#Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() #get a list of feature classes
for fc in fcList:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name.lower() == 'elev':  #look for the name elev
            arcpy.AlterField_management(fc, field.name, 'ELEVATION', 'Elevation in Metres')

			




#Import geoprocessing
import arcpy

#Set local variables
fc = "C:/Data/Garbo.gdb/trails" #Note:empty feature class
field = "condition_rating" #short int, non nullable field
new_name = "notes"
new_alias = "Comments on Trail Condition"
new_type = "TEXT"
new_length = "60"
new_is_nullable = "NULLABLE"
clear_alias = "FALSE"

#Alter the properties of a non nullable, short data type field to become a text field
arcpy.AlterField_management(fc, field, new_name, new_alias, new_type, new_length, new_is_nullable, clear_alias)
			