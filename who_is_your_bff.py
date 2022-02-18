import re
import json
import collections
import pandas
import os
from functools import partial

#liczba słów wysłanych

#path = r'C:\Users\Kacper\IdeaProjects\messages\inbox'
path = r'C:\Users\oliwa\IdeaProjects\messages\test'

fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))

# dzieli na ciągi znaków
def words(s):
    return re.findall('\w+', s)


def read_text_file(file_path):
    with open(file_path, 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
    data = json.loads(repaired.decode(), strict=False)

    return data


# iterate through all directories and files displaying most common word
def frame_creator():

    dataframe1 = pandas.DataFrame(columns=['sender', 'words'])


    for dick in os.listdir(path):
        path1 = f"{path}\{dick}"
        for file in os.listdir(path1):
            total = 0
            if file.endswith(".json"):
                file_path = f"{path1}\{file}"
                for i in read_text_file(file_path)["messages"]:
                    if i.get('content') is not None:
                        #print(i.get('content'))
                        a = len(i.get('content').split())
                        total = total + a

                friend = read_text_file(file_path)["participants"][0]['name']
                final_df = pandas.DataFrame([[total,friend]], columns=['words', 'sender'])
                dataframe1 = dataframe1.append(final_df)


    return dataframe1


    #             message_variable = read_text_file(file_path)['messages']
    #             counts = collections.Counter((w.lower() for e in message_variable for w in words(e.get('content', ''))))
    #             most_common = counts.most_common()
    #             dataframe = pandas.DataFrame(most_common, columns=['words', 'times'])
    #             dataframe1 = dataframe1.append(dataframe)
    #             total1 = dataframe1['times'].sum()
    #
    #             dataframe1 = pandas.DataFrame(data = {'words' : [total1], 'sender': [read_text_file(file_path)["participants"][0]['name']]})
    #             dataframe2 = dataframe2.append(dataframe1)
    #
    # return dataframe2


def words_sorting_engine(dataframe):

    dataframe1 = dataframe
    dataframe1 = dataframe1.groupby(['sender']).sum()
    dataframe1 = dataframe1.sort_values(['words'], ascending=False).reset_index()

    return dataframe1


z = words_sorting_engine(frame_creator())
x = frame_creator()

print(z.tail(10), z.head(5))

