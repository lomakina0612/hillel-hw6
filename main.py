
import csv

# with open('student_performance_prediction.csv', mode='r', newline='\n') as file:
#     csv_reader = csv.reader(file, delimiter=' ', quotechar='|')
    
#     for row in csv_reader:
#         print(row)


with open('student_performance_prediction.csv', mode='rt', newline='\n') as file, \
     open('new_student_performance_prediction.csv', mode='wt', newline='\n') as file_to_write:
    
    csv_reader = csv.DictReader(file, delimiter=',', quotechar='|')
    fieldnames = csv_reader.fieldnames
    csv_writer = csv.DictWriter(file_to_write, fieldnames=fieldnames)
    
    csv_writer.writeheader() 
    

    for row in csv_reader:
        try:
        
            row['Study Hours per Week'] = int(float(row['Study Hours per Week']) + 0.5)
            row['Attendance Rate'] = int(float(row['Attendance Rate']) + 0.5)
            row['Previous Grades'] = int(float(row['Previous Grades']) + 0.5)
            
            csv_writer.writerow(row)
            
        except Exception:
            print(f"Line {row['Student ID']} contains gaps. Skipped")
        