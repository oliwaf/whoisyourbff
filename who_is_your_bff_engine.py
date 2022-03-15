import re
import json
import collections
import pandas
import os
from functools import partial

# path = r'C:\Users\oliwa\IdeaProjects\messages\inbox'
path = r'C:\Users\oliwa\IdeaProjects\messages\test'
path1 = r'C:\Users\oliwa\IdeaProjects\messages\test\adrianwereta_wr-jay0fea'


fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))


def read_text_file(file_path):
    with open(file_path, 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
    data = json.loads(repaired.decode(), strict=False)

    return data


# www.google/pl -> www google pl = 3x
# def words(s):
#     return re.findall(r'\w+', s)
def words(s):
    regex = r'\w+'
    return re.findall(regex, s)


# iterate through all files and returning most common words from conversation
# received by words divided by special character.
def most_common_words():
    dataframe1 = pandas.DataFrame(columns=['word', 'times'])

    for file in os.listdir(path1):

        if file.endswith(".json"):
            file_path = fr"{path1}\{file}"
            message_variable = read_text_file(file_path)['messages']
            counts = collections.Counter((w.lower() for e in message_variable for w in words(e.get('content', ''))))
            counts1 = sum(collections.Counter((w.lower() for e in message_variable for w in words(e.get('content', '')))
                                              ).values())
            most_common = counts.most_common()
            dataframe = pandas.DataFrame(most_common, columns=['word', 'times'])
            dataframe1 = pandas.concat([dataframe, dataframe1])
            dataframe1 = pandas.concat(
                [dataframe1, pandas.DataFrame(data={'word': ['Sum_of_Words'], 'times': [counts1]})])

            # print(tuple(w.lower() for e in message_variable for w in words(e.get('content', ''))))

    dataframe1 = dataframe1.groupby(['word']).sum()
    dataframe1 = dataframe1.sort_values(['times'], ascending=False).reset_index()

    return dataframe1, counts


# data frame with sum of words every friend
def number_of_words_frame():
    dataframe1 = pandas.DataFrame(columns=['words', 'sender'])

    for directories in os.listdir(path):

        path2 = fr"{path}\{directories}"
        for file in os.listdir(path2):
            total = 0
            if file.endswith(".json"):
                file_path = fr"{path2}\{file}"
                participants = (len(read_text_file(file_path)["participants"]))
                if participants == 2:
                    for i in read_text_file(file_path)["messages"]:
                        if i.get('content') is not None:
                            a = len(i.get('content').split())
                            total = total + a

                    friend = read_text_file(file_path)["participants"][0]['name']
                    final_df = pandas.DataFrame([[total, friend]], columns=['words', 'sender'])
                    dataframe1 = pandas.concat([final_df, dataframe1])

    # SORTING DATAFRAME
    dataframe1 = dataframe1.groupby(['sender']).sum()
    dataframe1 = dataframe1.sort_values(['words'], ascending=False).reset_index()

    return dataframe1


def frame_cleaner_from_letters(dataframe):
    dataframe1 = dataframe
    dataframe1 = dataframe1[dataframe1['word'].str.contains(r'\b.\b') == False]
    dataframe1 = dataframe1[dataframe1['word'].str.contains(r'\b..\b') == False]
    dataframe1 = dataframe1[dataframe1['word'].str.contains(r'\b...\b') == False]

    return dataframe1


# deleting from counter short words.

def remove_short_phrases(df_with_frequencies):
    for i in list(df_with_frequencies):
        if len(i) <= 2:
            del df_with_frequencies[f'{i}']
    return df_with_frequencies


x = number_of_words_frame()
z = most_common_words()

print(z)
