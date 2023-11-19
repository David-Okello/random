import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'(0?[1-9]|1[0-2]):([0-5][0-9]) (AM|PM) to (0?[1-9]|1[0-2]):([0-5][0-9]) (AM|PM)'

    match = re.search(pattern,s)

    if match:
        hours_dict = {
            "12 AM": "00",
            "1 AM" : "01",
            "2 AM": "02",
            "3 AM" : "03",
            "4 AM": "04",
            "5 AM" : "05",
            "6 AM": "06",
            "7 AM" : "07",
            "8 AM": "08",
            "9 AM" : "09",
            "10 AM": "10",
            "11 AM" : "11",
            "12 PM": "12",
            "1 PM" : "13",
            "2 PM": "14",
            "3 PM" : "15",
            "4 PM": "16",
            "5 PM" : "17",
            "6 PM": "18",
            "7 PM" : "19",
            "8 PM": "20",
            "9 PM" : "21",
            "10 PM": "22",
            "11 PM" : "23"
        }

        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

        if (start_time := match.group(1) + " " + match.group(3)) in hours_dict and (end_time := match.group(4) + " " + match.group(6)) in hours_dict:
            start_hours = hours_dict[start_time]
            end_hours = hours_dict[end_time]
            converted_start_time = f"{start_hours}:{match.group(2)}"
            converted_end_time = f"{end_hours}:{match.group(5)}"
            return f"{converted_start_time} to {converted_end_time}"
    else:
        raise ValueError("Invalid time format. Please enter time in the format 'hh:mm AM/PM to hh:mm AM/PM'.")


if __name__ == "__main__":
    main()
