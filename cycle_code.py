from datetime import date, timedelta
import csv


def iterate_days_of_year():
    from_date = date(2024, 1, 1)
    to_date = date(2025, 12, 31)

    delta = timedelta(days=1)
    current_date = from_date

    data: list = [['date','cycle_code']]
    while current_date <= to_date:
        cycle_code: str = get_cycle_code(current_date)
        data.append([current_date, cycle_code])
        current_date += delta

    with open('./cp99-date-encoding-py.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def get_cycle_code(datetime_date) -> str:
    """
    Returns the IRS Cycle Code (YYYYCC) for the specified date.
    If the specified date is a weekday, CC will be a 2-digit week number (zero-padded if necessary).
    If the specified date is a weekend, CC will be "XX".
    """
    week_num_padded: str = "XX"
    day_id = {"Friday": "01", "Monday": "02", "Tuesday": "03", "Wednesday": "04", "Thursday": "05"}
    # Determine the day of the week (Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=5, Sun=6)
    dayOfTheWeek: int = datetime_date.weekday()
    dayStr: str = datetime_date.strftime("%A")
    if dayOfTheWeek < 5:
        # Calculate week number for a weekday
        week_num: int = datetime_date.isocalendar()[1]
        # Increase week number if it is a Friday
        if dayOfTheWeek == 4:
            week_num += 1
        if week_num==53: week_num = 1
        # Zero-pad week number if not 2-digits
        week_num_padded: str = "0"+str(week_num) if week_num < 10 else str(week_num)
    if dayStr in ["Saturday", "Sunday"]: return f"{datetime_date} is not a weekday"
    if datetime_date.month==12 and week_num_padded == "01": 
        return f"{datetime_date.year+1}{week_num_padded}{day_id[dayStr]}"
    else: return f"{datetime_date.year}{week_num_padded}{day_id[dayStr]}"


if __name__ == "__main__":
    #iterate_days_of_year()
    print(get_cycle_code(date(2024, 3, 7)))