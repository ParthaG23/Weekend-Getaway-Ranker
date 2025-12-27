#  Weekend Getaway Ranker  
### A Data Engineering–Based Travel Recommendation System

##  Project Overview
The Weekend Getaway Ranker is a Python-based recommendation system designed to suggest ideal weekend travel destinations in India based on a user-selected source city.  
The system ranks destinations using a combination of proximity (distance approximation using city/state/zone hierarchy), Google review ratings, and popularity (number of Google reviews).

This project focuses on data preprocessing, feature engineering, and ranking logic using Python and Pandas, without relying on external APIs.

---

##  Problem Statement
Develop a recommendation engine for local travel using the **Travel Dataset – India’s Must-See Places**.

**Requirements:**
- Take a Source City as input  
- Rank the top weekend destinations  
- Use distance, rating, and popularity as ranking factors  
- Submit a GitHub repository containing:
  - Python implementation
  - requirements.txt
  - Sample output for at least three cities

---

## Dataset Description
The dataset contains curated information about popular tourist places across India.

**Key attributes used in this project:**
- Zone  
- State  
- City  
- Name  
- time needed to visit in hrs  
- Google review rating  
- Number of google review in lakhs  
- Best Time to visit  

---

##  Dataset Consideration
The dataset does not include latitude or longitude values.  
Therefore, exact geographical distance cannot be calculated.

To address this limitation, a hierarchical proximity-based distance approximation is used to ensure realistic weekend travel recommendations.

---

##  Dataset Source
The dataset used in this project is publicly available on Kaggle:  
**Travel Dataset – Guide to India’s Must-See Places**  
https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places

---

##  Design Decisions
### Distance Approximation Strategy
In the absence of geographical coordinates, proximity is estimated using administrative hierarchy:
1. Same City – Highest priority  
2. Same State  
3. Same Zone  
4. Adjacent Zones  
5. Distant Zones – Lowest priority  

This approach enables practical and location-aware weekend recommendations without external dependencies.

---

##  Ranking Methodology
Each destination is assigned a final ranking score computed as:

Final Score =  
0.45 × Distance Score +  
0.35 × Normalized Rating +  
0.20 × Normalized Popularity  

**Scoring components:**
- Distance Score: Derived from city/state/zone proximity  
- Rating: Normalized Google review rating  
- Popularity: Normalized number of Google reviews (in lakhs)

**Additional filters applied:**
- time needed to visit ≤ 5 hours  
- Google review rating ≥ 4.0  

These constraints improve suitability for weekend trips.

---

## Technologies Used
- Python 3.11.1  
- Pandas  

---

##  Project Structure
Weekend-Getaway-Ranker/  
│  
├── data/  
│   └── travel_dataset.csv  
│  
├── src/  
│   └──weekend_Getaway_ranker.ipynb  
│  
├── requirements.txt  
├── sample_output.txt  
└── README.md  

---

##  How to Execute the Project
1. Install dependencies using:  
   `pip install -r requirements.txt`

2. Run the application from the project root directory:  
   `python src/weekend_Getaway_ranker.ipynb`

3. Provide input:
   - Enter a source city (e.g., Kolkata, Delhi, Mumbai), or  
   - Press Enter to run predefined sample cities

---

##  Sample Output
Sample recommendations for three different cities are provided in `sample_output.txt`.

Each output includes:
- Destination name  
- City  
- Google review rating  
- Popularity  
- Best time to visit  
- Final ranking score  

The output is formatted for easy readability and evaluation.

---

##  Assumptions and Limitations
- Recommendations are limited to destinations present in the dataset  
- Distance is approximated using administrative hierarchy  
- The model is optimized for weekend travel only  
- No real-time or external data sources are used  

---

##  Assignment Compliance
This project fulfills all assignment requirements:
- Input-based recommendation system  
- Implemented using Python and Pandas  
- Distance, rating, and popularity-based ranking  
- Clean data preprocessing and feature engineering  
- Sample outputs for multiple cities  
- GitHub-ready project structure  

---

##  Future Enhancements
- Integrate latitude and longitude for precise distance calculation  
- Add budget and travel-time filters  
- Export results to CSV or Excel  
- Develop a CLI or web-based interface  

---

##  Author
**Partha Gayen**  
GitHub: https://github.com/ParthaG23
LinkedIn: https://linkedin.com/in/partha-gayen  

If you find this project helpful, consider giving the repository a star.