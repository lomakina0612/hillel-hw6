
import csv

class MissingValueError(Exception):
    pass

with open('student_performance_prediction.csv', mode='rt', newline='\n') as file, \
     open('new_student_performance_prediction.csv', mode='wt', newline='\n') as file_to_write:
    
    csv_reader = csv.DictReader(file, delimiter=',')
    fieldnames = csv_reader.fieldnames
    csv_writer = csv.DictWriter(file_to_write, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    numeric_columns = ['Study Hours per Week', 'Attendance Rate', 'Previous Grades']
    yes_no_columns = ['Participation in Extracurricular Activities', 'Passed']

    for row in csv_reader:
        try:
            if any(row[column] in ("", None) or row[column].strip().lower() == 'nan' for column in row):
                raise MissingValueError(f"Line {row['Student ID']} contains gaps. Skipped")
            
            for column in numeric_columns:
                row[column] = int(float(row[column]) + 0.5)
            
            for column in yes_no_columns:
                row[column] = row[column].upper()
             
            csv_writer.writerow(row)
        
        except MissingValueError as e:
            print(e)
            