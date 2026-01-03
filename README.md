# 🏥 Medical Insurance Cost Predictor

A Streamlit web application that predicts medical insurance costs based on user input using machine learning.

## ⚠️ Important Disclaimer

**This is a TEST/DEMO project only!**

- Trained on a small dataset (~1,338 records)
- For educational purposes only
- **DO NOT use for real medical insurance decisions**
- Consult qualified professionals for actual insurance quotes
- Predictions may not be accurate or reliable

## ✨ Features

- **User-friendly Interface**: Clean, modern UI with medical-themed design
- **Input Validation**: Proper input types (sliders, dropdowns, number inputs)
- **Real-time Prediction**: Instant cost estimation using ML model
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Elements**: Animations and visual feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository** (if applicable)
2. **Navigate to the project directory**

   ```bash
   cd /path/to/ui
   ```

3. **Create virtual environment**

   ```bash
   python3 -m venv venv
   ```

4. **Activate virtual environment**

   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📊 Input Features

The model predicts insurance costs based on:

- **Age**: Patient's age (18-65+)
- **Sex**: Male/Female
- **BMI**: Body Mass Index (15-50)
- **Children**: Number of dependents (0-5+)
- **Smoker**: Smoking status (Yes/No)
- **Region**: Geographic location (Northeast, Northwest, Southeast, Southwest)

## 🛠️ Technologies Used

- **Streamlit**: Web app framework
- **Scikit-learn**: Machine learning library
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **Python**: Programming language

## 📁 Project Structure

```
ui/
├── app.py                 # Main Streamlit application
├── medical_insurance_model.pkl  # Trained ML model
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created)
```

## 🌐 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select repository and set main file path to `ui/app.py`
5. Deploy!

### Other Platforms

- Heroku
- AWS
- Google Cloud
- Any platform supporting Python/Streamlit

## 🤝 Contributing

This is an educational project. Feel free to:

- Report bugs
- Suggest improvements
- Submit pull requests

## 📄 License

This project is for educational purposes only.

## 📞 Contact

For questions or feedback about this demo project, please create an issue in the repository.

---

**Remember: This is not a real insurance prediction tool. Always consult with licensed insurance professionals for accurate quotes and advice.**
