from re import match,search
import json

def separate_date_fields(date):
    day = date[:2]
    month = date[3:5]
    year = date[6:10]
    date_set = {'day': day,'month': month,'year': year}
    return date_set

def parse_line(line):

    # Define my patterns to search the occurrences
    func_name_pattern = r'[a-z]+_[a-z]+'
    date_pattern = r'\d\d/\d\d/\d\d\d\d'
    content_pattern1 = r': .*'
    content_pattern2 = r'[\w\s]+'

    # Getting the info that match my patterns defined above
    func_name = match(func_name_pattern,line).group(0)
    date = separate_date_fields(search(date_pattern,line).group(0))
    content = search(content_pattern1,line).group(0)
    message = search(content_pattern2,content).group(0) # Filter twice, first to get the content with the ': ' string, second to remove it

    return {
        'func_name': func_name,
        'date': date,
        'message': message,
    } # This set structure allows me to get more easily to each info 

        

func_names_occurrences = {}

with open('out.log','r') as f:
    line = f.readline()
    while line != "":
        parsed_line = parse_line(line)
        func_name = parsed_line['func_name']
        if func_name in func_names_occurrences:
            del parsed_line['func_name']
            func_obj = parsed_line
            func_names_occurrences[ func_name ].append(func_obj)
        else:
            del parsed_line['func_name']
            func_obj = parsed_line
            func_names_occurrences[ func_name ] = [func_obj]

        line = f.readline()
    print(json.dumps(func_names_occurrences, sort_keys=True,indent=4))