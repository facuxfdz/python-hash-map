## Python practice using hash map
This is a short program in which we use a hash map to count the occurrences of some *function calls* defined into another file.
When we call one of those function, a log is written into a 'out.log' file.  
Then, using ```analize_logs.py``` file, we can show each function call information in JSON format, this information is grouped by the 'func_name' that was called.

***Example***  
```json
"print_decorated": [
        {
            "date": {
                "day": "22",
                "month": "06",
                "year": "2021"
            },
            "message": " Facundo"
        },
        {
            "date": {
                "day": "22",
                "month": "06",
                "year": "2021"
            },
            "message": " Pedro"
        },
        {
            "date": {
                "day": "22",
                "month": "06",
                "year": "2021"
            },
            "message": " Otra vez yo"
        }
    ],
```