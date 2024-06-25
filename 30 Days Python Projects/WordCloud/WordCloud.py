import sys
import numpy as np
from PIL import Image 
import wikipedia 

# We will import WordCloud and STOPWORDS from wordcloud library
# to extract information
from wordcloud import WordCloud, STOPWORDS 

# We will import STOPWORDS to remove common words 
a = str(input("Enter the name of which you want to make word cloud: ")) 

# We will import wikipedia library
# Search for the title from Wikipedia 
title = wikipedia.search(a)[0] 

# We will import wikipedia library
# Search the page related to the given topic on Wikipedia 
page = wikipedia.page(title) 

# We will import wikipedia library
# Extract the content of that topic 
text = page.content 
print(text) 
bg = np.array(Image.open("abcd.jpg")) 

# We will import STOPWORDS to remove common words
# Set of unwanted words 
unwanted_words = set(STOPWORDS) 

# We will import WordCloud and STOPWORDS from wordcloud library
# Generate word cloud 
wordcloud = WordCloud(background_color="black", max_words=400, mask=bg, 
stopwords=unwanted_words) 
wordcloud.generate(text) 

# We will import matplotlib.pyplot as plt
# Save the word cloud 
wordcloud.to_file("sample.png")