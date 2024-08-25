# Word Cloud

This collection of scripts yields a word cloud super-imposed on a background image. 
The first step is to provide a text file and background image. 
The next step is to process those assets.
Here, we remove stopwords from the text and blank space from the background image.
Finally, we use the cleaned assets to generate the wordcloud.
All tooling is provided by Andreas Mueller's wordcloud library. 

## Installation

The primary dependency is wordcloud. You can install it using the following commands:

PIP
```
pip install wordcloud
```

CONDA
```
conda install -c conda-forge wordcloud
```

## Examples
This example uses the full text of the [Bhagavad Gita](https://sanskritdocuments.org/sanskrit/bhagavadgita/) and the James Webb [rendition](https://webbtelescope.org/contents/media/images/2023/128/01H449193V5Q4Q6GFBKXAZ3S03) of the Rho Ophiuchi cloud complex.

![webb](https://github.com/user-attachments/assets/41ae4f23-dd73-499e-b2b2-e76b8db2b321)
