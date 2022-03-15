import who_is_your_bff_engine as bff
import matplotlib.pyplot as plt

# Define a function to plot word cloud

df_most_common_words, df_counts = bff.most_common_words()

def plot_cloud():

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
    #df.plot(kind='bar', figsize=(10, 5), x='sender', y='words')
    ax = df.plot(kind='bar', figsize=(10, 5), x='sender', y='words')
    for container in ax.containers:
        ax.bar_label(container)
    plt.tight_layout()

# Plot
plot_cloud()
plot_bar()
plt.show()











