# Recipe Review Analysis: Topic Modeling & Keyword Extraction

## Group Project
* Project Type: CS 6140 Data Mining Group Project
* Team Members: Danny Park, Christina Le, Tinh Nguyen
* My Specific Contributions: Implemented web scraper, Data Cleaning, K-grams, PCA, and UMAP

## Project Goal
Analyze unstructured recipe reviews to extract quality metrics and satisfaction drivers that are not captured by star ratings.

## Data & Tech
* Data Source: Allrecipes.com (approximately 6,000 user reviews)
* Programming: Python
* Libraries: Pandas, NLTK, Scikit-learn, Sentence_transformers, KeyBERT

## Methodology
* Keyword Extraction: Identification of key terms using KeyBERT and TF-IDF.
* Dimensionality Reduction: Noise reduction and visualization using PCA and UMAP.
* Topic Modeling: Classification of user feedback into latent topics using LDA.

## Key Finding
* Identification of specific feedback clusters, including ease of cooking and recipe reliability
* Visualization of review data to identify user sentiment and feedback patterns.

<img width="600" height="474" alt="Screenshot 2026-02-06 at 10 44 38 AM" src="https://github.com/user-attachments/assets/2458bcdd-9475-46d7-a471-0b7d999426ec" />

3D UMAP visualization of sentence embeddings to capture semantic themes. By applying non-linear dimensionality reduction to high-demensional KeyBERT embeddings, the model identifies subtle clusters drien by semantic content rather than just word frequency.
