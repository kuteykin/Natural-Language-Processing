"""Analysis of documents similarity using SpaCy"""

# import of libraries and models
import spacy
nlp = spacy.load("en_core_web_sm")
from pathlib import Path

# list of files to compare
files = ['Input/Romeo_Juliett.txt', 
         'Input/Bacon.txt', 
         'Input/Hamlet.txt', 
         'Input/Pride_and_Prejudice.txt'
        ]

# parsing of files
documents = [nlp(Path(file).read_text()) for file in files]

# calculation of pairwise similarity
for i in range(len(files)-1):
    for j in range(i+1, len(files)):
        similarity = documents[i].similarity(documents[j])      
        print(f'Similarity between "{files[i]}" and "{files[j]}" is {similarity:.0%}')