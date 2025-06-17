import re
import pandas as pd

def preprocess(data):
    from datetime import datetime

    # Regex pattern that supports both 24-hour and 12-hour time with AM/PM
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s[APap][Mm])?\s-\s'

    # Sample input: '06/05/25, 12:40 AM -' or '06/05/25, 00:40 -'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Clean up whitespace and dash
    dates = [d.strip(" -") for d in dates]

    # Convert to datetime using multiple formats
    def parse_date(date_str):
        for fmt in ['%d/%m/%y, %I:%M %p', '%d/%m/%Y, %I:%M %p',  # 12-hour
                    '%d/%m/%y, %H:%M', '%d/%m/%Y, %H:%M']:  # 24-hour
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None  # or raise an error/log if needed

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = df['message_date'].apply(parse_date)

    # Optional: drop rows where parsing failed
    df.dropna(subset=['message_date'], inplace=True)

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        # Convert to 24-hour format if needed
        if isinstance(hour, str) and ('AM' in hour or 'PM' in hour):
            hour = pd.to_datetime(hour, format='%I %p').hour

        # Your original logic
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df