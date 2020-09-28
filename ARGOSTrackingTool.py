#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Krista Erdman (kae23@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# Create a variable pointing to data file
file_name = "./data/raw/sara.txt"

# Create a file object from the file
file_object = open(file_name, "r")

# Read contents of file into a list 
line_list = file_object.readlines()

# Close the file
file_object.close()

# Create two empty dictionary objects
date_dict = {}
coord_dict = {}


# Iterate through all lines in the line_list
for lineString in line_list:
    if lineString[0] == "#" or lineString[0] == "u": continue 

    # could also write for lineString in line_list[17:]:
    # OR if lineString[0] in ("#", "u"): continue

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]             # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]                 # Observation Location Class
   # if obs_lc not in ("1", "2", "3"):
      #  continue
    obs_lat = lineData[6]               # Observation Latitude
    obs_lon = lineData[7]               # Observation Longitude
    
    # Print information of sara if lc is 1, 2, 3
    if obs_lc in ("1", "2", "3"): 
        print (f"Record {record_id} indicates Sara was seen at lat:{obs_lat}N and lon:{obs_lon}W on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)
    
