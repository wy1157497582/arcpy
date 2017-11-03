import csv
import arcpy
 
def export_csv(feature_class, csv_filename, field_names, new_field_names=None):
    """Export a feature class's attribute table to a csv file.
 
    Parameters:
        feature_class   - The feature class to export.
        csv_filename    - The path to the CSV file to create.
        field_names     - The list of field names to export.
        new_field_names - An optional list of output field names.
    """
    if new_field_names and len(new_field_names) != len(field_names):
        raise ValueError('field_names and new_field_names must be the same length.')
    with open(csv_filename, 'wb') as fp:
        writer = csv.writer(fp)
        writer.writerow(new_field_names or field_names)
        with arcpy.da.SearchCursor(feature_class, field_names) as rows:
            writer.writerows(rows)
			
			
			
			
			
			
			
			
			
			
			
			export_csv('D:/Temp/test_shapefile.shp', 'D:/Temp/test_export.csv',
           ['Id', 'POINT_X', 'POINT_Y'], ['id', 'x', 'y'])