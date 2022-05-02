-------------------
    join Module
-------------------

def join(argv):
 --------------------------------------------------------------------------------------------------------------------------------------------------------
    argv - list of arguments given to the program via terminal
    argv[1] - first file path
    argv[2] - second file path
    argv[3] - column name to join files on
    argv[4] - join type, if not specified default type is inner join
    Main part of the program that calls other functions.
 --------------------------------------------------------------------------------------------------------------------------------------------------------

 def validate_arguments(argv):
 --------------------------------------------------------------------------------------------------------------------------------------------------------
    Function that is validating parameters given to join(). It calls files_fine() function and returns True 
    if parameters are valid or False if they are not.
 --------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def files_fine(first_file, second_file, column_name):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Functions that checks with valid_csv() function if files given:
    -exist
    -are valid csv files
    -have column you want to join files on
    Returns True or False depending on check result for both files.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def valid_csv(file_name, column_name):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Function that checks if column number in every row is constant, column name you want to join on is present in
    file header and file exists. It calls column_exist() function.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def column_exist(file_header, column_name):
 --------------------------------------------------------------------------------------------------------------------------------------------------------
    Function that checks if column name you want to join files on is present in the file header.
 --------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def right_join(left_csv: str, right_csv: str, column_name: str):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Implementation of right join. Prints every joined row.
    If no row was matched to the row of right file it calls fill_missing() function.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def left_join(left_csv: str, right_csv: str, column_name: str):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Implementation of left join. Prints every joined row.
    If no row was matched to the row of left file it calls fill_missing() function.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def fill_missing(left_file_row, right_file_row, join_type, column_name):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Generating joined row filled with nulls on side specified with join_type parameter.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def inner_join(first_csv: str, second_csv: str, column_name: str):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Implementation of inner join. Prints every joined row.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
def generate_header(first_csv: str, second_csv: str, column_name: str):
--------------------------------------------------------------------------------------------------------------------------------------------------------
    Generating header of new csv file.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
 
 
 
