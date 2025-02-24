# IPL Win Predictor

The IPL Win Predictor is a Streamlit-based web application that predicts the winning probability of an IPL match based on the current match situation. The application uses a pre-trained machine learning pipeline (saved as `pipe.pkl`) to generate predictions.

## Features

- **User-Friendly Interface:** Input match details such as batting team, bowling team, target score, current score, overs completed, and wickets lost.
- **Real-Time Predictions:** Get win probabilities instantly with just one click.
- **Modern UI:** Sleek design with inputs in the sidebar for a cleaner look.
- **Interactive:** Easily adjust match parameters to see how the win probability changes.

## Requirements

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [pickle](https://docs.python.org/3/library/pickle.html) (for model persistence)
- [numpy](https://numpy.org/)

You can install the necessary Python packages using pip:

```bash
pip install streamlit pandas scikit-learn numpy
