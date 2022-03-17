import who_is_your_bff_engine as bff
import matplotlib.pyplot as plt

# Define a function to plot word cloud

df_most_common_words, df_counts = bff.most_common_words()


def plot_worldcloud():

    import wordcloud
    # Set figure size
    plt.figure(figsize=(10, 5))
    # Generate word cloud
    wordcloud = wordcloud.WordCloud(width=3000, height=2000, random_state=1, background_color='black',
                                    colormap='Pastel1', collocations=False,
                                    stopwords=wordcloud.STOPWORDS).generate_from_frequencies(bff.remove_short_phrases(
                                        df_counts))

    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off")




def plot_bar():
    df = bff.number_of_words_frame().head(10)
    ax = df.plot(kind='bar', figsize=(10, 5), x='sender', y='words')
    for container in ax.containers:
        ax.bar_label(container)
    plt.tight_layout()


a, b = bff.time_of_messages()


def plot_line_hours(dataframe):

    a = dataframe['Sender name'].iloc[0]
    b = dataframe['User name'].iloc[0]
    figure, axs = plt.subplots()
    axs.plot(dataframe['Time'], dataframe['Sender'], label=a)
    axs.plot(dataframe['Time'], dataframe['User'], label=b)
    axs.legend(loc='best')


def plot_line_days(dataframe):

    a = dataframe['Sender name'].iloc[0]
    b = dataframe['User name'].iloc[0]
    figure, axs = plt.subplots()
    axs.plot(dataframe['Time'], dataframe['Sender'], label=a)
    axs.plot(dataframe['Time'], dataframe['User'], label=b)
    axs.legend(loc='best')

# Plot

plot_line_hours(a)
plot_line_days(b)
plot_worldcloud()


plt.show()













