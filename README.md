
# 🎬 Content-Based Movie Recommendation System  

## 📌 About the Project  

The **Content-Based Movie Recommendation System** suggests movies to users based on their interests and preferences. This system leverages **movie metadata**, such as **genres, plot summaries, and other textual descriptions**, to find similar movies.  

### 🎯 How It Works  
- **Feature Extraction**: The system extracts features from movie descriptions, genres, and other metadata.  
- **Similarity Computation**: It calculates the similarity between movies using techniques like **TF-IDF (Term Frequency-Inverse Document Frequency)** and **cosine similarity**.  
- **Personalized Recommendations**: Based on user input (e.g., a favorite movie), the system suggests movies with the most similar content.  

## 🗂️ Project Structure  

### 🔹 `MovieRecommendationSystem.ipynb`  
- Contains the **core logic** for the recommendation system.  
- Uses **TF-IDF vectorization** and **cosine similarity** for movie recommendations.  
- Processes a dataset of movies to extract important features.  

### 🔹 `ml_api.py`  
- Implements an **API using FastAPI** to serve recommendations.  
- Loads the trained recommendation model using **Pickle**.  
- Provides an endpoint for users to **upload audio files**, but this part is currently not implemented for recommendations.  

## 🛠️ Tech Stack  

- **Programming Language**: Python  
- **Frameworks & Libraries**:  
  - **FastAPI** (for API development)  
  - **scikit-learn** (for TF-IDF vectorization & similarity computation)  
  - **pandas & NumPy** (for data processing)  
  - **pickle** (for model saving & loading)  
- **Data Processing**: Movie metadata dataset  
- **Deployment**: Local server 


