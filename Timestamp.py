import re
import json
import pandas
import os
from functools import partial
from datetime import datetime
import timeit
import matplotlib.pyplot as plt

tic = timeit.default_timer()
# path = r'C:\Users\oliwa\IdeaProjects\messages\inbox'

path1 = r'C:\Users\oliwa\IdeaProjects\messages\test'
path = r'C:\Users\oliwa\IdeaProjects\messages\inbox\przemekwozniak_alao0wckwg'

fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))


def read_text_file(file_path):
    with open(file_path, 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
    data = json.loads(repaired.decode(), strict=False)

    return data

dataframe = pandas.DataFrame()
dataframe1 = pandas.DataFrame()
dataframe2 = pandas.DataFrame()

def time_of_messages():

    dataframe = pandas.DataFrame()
    dataframe1 = pandas.DataFrame()

    for file in os.listdir(path):
        if file.endswith(".json"):
            file_path = fr"{path}\{file}"
            for i in read_text_file(file_path)["messages"]:
                z = datetime.fromtimestamp(i.get('timestamp_ms')/1000.0)
                date = z.strftime("%A")
                time = z.strftime('%H')
                sender_name = i.get('sender_name')
                dataframe1 = pandas.DataFrame([[sender_name, date, time]], columns=['Sender', 'Date', 'Time'])
                dataframe = pandas.concat([dataframe, dataframe1])

            sender_df = dataframe[dataframe['Sender'].str.contains(read_text_file(file_path)["participants"][0]['name'])]
            sender_df = sender_df.reset_index(drop=True)

            user_df = dataframe[dataframe['Sender'].str.contains(read_text_file(file_path)["participants"][1]['name'])]
            user_df = user_df.reset_index(drop=True)

    return sender_df, user_df


#
a, b = time_of_messages()

for i in range(24):
    dataframe = pandas.DataFrame([[str(i).zfill(2), a[a.Time == str(i).zfill(2)].shape[0], a['Sender'].iloc[0],
                                    b[b.Time == str(i).zfill(2)].shape[0], b['Sender'].iloc[0]]],
                                  columns=['Time', 'Sender', 'Sender name', 'User', 'User name'])
    dataframe1 = pandas.concat([dataframe1, dataframe])

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(dataframe1)

for i in days:
    dataframe = pandas.DataFrame([[i, a[a.Date == f'{i}'].shape[0], a['Sender'].iloc[0], b[b.Date == f'{i}'].shape[0],
                                    b['Sender'].iloc[0]]], columns=['Time', 'Sender', 'Sender name', 'User', 'User name'])
    dataframe2 = pandas.concat([dataframe2, dataframe])

print(dataframe2)
#
# plot, axs = plt.subplots(2, sharey='all')
# axs[0].plot(dataframe1['Time'], dataframe1['Sender'])
# axs[1].plot(dataframe1['Time'], dataframe1['User'])
#
# plot, axs = plt.subplots(2, sharey='all')
# axs[0].plot(dataframe2['Time'], dataframe2['Sender'])
# axs[1].plot(dataframe2['Time'], dataframe2['User'])

plt.show()

print(time_of_messages())


toc = timeit.default_timer()

print(toc - tic)
