import re
import json
import pandas
import os
from functools import partial
from datetime import datetime
import timeit

tic = timeit.default_timer()
# path = r'C:\Users\oliwa\IdeaProjects\messages\inbox'

path1 = r'C:\Users\oliwa\IdeaProjects\messages\test'
path = r'C:\Users\oliwa\IdeaProjects\messages\inbox\\adamferchichi_c9g_s2qqfq'

fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))


def read_text_file(file_path):
    with open(file_path, 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
    data = json.loads(repaired.decode(), strict=False)

    return data


def time_of_messages():

    dataframe1 = pandas.DataFrame()

    for file in os.listdir(path):
        if file.endswith(".json"):
            file_path = fr"{path}\{file}"
            for i in read_text_file(file_path)["messages"]:
                z = datetime.fromtimestamp(i.get('timestamp_ms')/1000.0)
                date = z.strftime("%A %m %d %Y")
                time = z.strftime('%H:%M')
                sender_name = i.get('sender_name')
                dataframe = pandas.DataFrame([[sender_name, date, time]], columns=['Sender', 'Date', 'Time'])
                dataframe1 = pandas.concat([dataframe1, dataframe])

        sender_df = dataframe1[dataframe1['Sender'].str.contains(read_text_file(file_path)["participants"][0]['name'])]
        sender_df = sender_df.reset_index(drop=True)
        user_df = dataframe1[dataframe1['Sender'].str.contains(read_text_file(file_path)["participants"][1]['name'])]
        user_df = user_df.reset_index(drop=True)

    return sender_df, user_df


print(time_of_messages())


toc = timeit.default_timer()

print(toc - tic)
