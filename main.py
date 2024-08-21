
import csv

with open('student_performance_prediction.csv', mode='rt', newline='\n') as file, \
     open('new_student_performance_prediction.csv', mode='wt', newline='\n') as file_to_write:
    
    csv_reader = csv.DictReader(file, delimiter=',')
    fieldnames = csv_reader.fieldnames
    csv_writer = csv.DictWriter(file_to_write, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    numeric_columns = ['Study Hours per Week', 'Attendance Rate', 'Previous Grades']

    for row in csv_reader:
        try:
            for column in numeric_columns:
                row[column] = int(float(row[column]) + 0.5)
                
            csv_writer.writerow(row)
        
        except ValueError:
            print(f"Line {row['Student ID']} contains gaps. Skipped")
            