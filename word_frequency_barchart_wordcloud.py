"""Word Frequency Bar Chart and Word Cloud from Shakespeare’s Hamlet"""

# import libraries
import matplotlib.pyplot as plt
from textblob import TextBlob
from pathlib import Path
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import textblob.utils as tbu


# read and tokenize text
text = Path('Input/Hamlet.txt').read_text()
blob = TextBlob(text)
stops = stopwords.words('english')

# count words
items = tbu.lowerstrip(blob).word_counts.items()
items = [item for item in items if item[0] not in stops]
sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# create list of Top20 words and bar chart
top20 = sorted_items[1:21]
df = pd.DataFrame(top20, columns=['word', 'count'])
print(df)
plt.cla()
axes = df.plot.bar(x='word', y='count', legend=False)
plt.show()


# create Word Cloud using mask
import imageio
mask_image = imageio.v2.imread('Input/mask_oval.png')
from wordcloud import WordCloud
wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file('Output/Hamlet-oval.png')
