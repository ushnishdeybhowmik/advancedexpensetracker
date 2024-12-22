# Spend.AI - Advanced Expense Tracker

Spend.AI is a cutting-edge expense tracking application designed to simplify personal finance management. Built with Python, SQLite3, and powered by Tesseract OCR, Spend.AI extracts transaction details directly from UPI app screenshots (e.g., Google Pay), processes the data, and provides actionable insights such as spending categories, averages, and anomalies.

## Key Features

- **OCR-Powered Data Extraction**:
  - Automatically extract transaction details from UPI app screenshots.
  - Supports screenshots from Google Pay (GPAY) with OCR technology powered by Tesseract.

- **Data Storage**:
  - Securely stores extracted transaction data using SQLite3.

- **Spending Insights**:
  - Categorizes transactions into user-defined categories.
  - Calculates spending averages over custom time periods.
  - Detects anomalies in transaction patterns.

- **User-Friendly Analysis**:
  - Displays spending insights through clear, interactive dashboards.
  - Allows export of data to CSV for external analysis.

## How It Works

1. **Upload Screenshots**:
   - Add UPI app screenshots directly into Spend.AI.
   
2. **OCR Processing**:
   - Pytesseract extracts transaction details such as date, amount, and merchant from the screenshots.
   
3. **Data Categorization**:
   - Automatically or manually categorize transactions into predefined categories like Food, Travel, Utilities, etc.
   
4. **Insight Generation**:
   - View dashboards displaying monthly spending, average expenses, and unusual transactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spendai.git
   cd spendai
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Download and install Tesseract OCR:
   - [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract)
   - Update `pytesseract.tesseract_cmd` in the code with the path to `tesseract.exe`.

4. Run the application:
   ```bash
   python spendai.py
   ```

## Dependencies

- Python 3.x
- SQLite3
- Pytesseract
- Pillow

## Screenshots
![Spend.AI Dashboard](https://github.com/user-attachments/assets/4fc55ba0-8821-4507-a6f7-da82c323e422)

## Changelog

### v1.0.0

- Added OCR support for Google Pay (GPAY) screenshots.
- Integrated SQLite3 database for transaction storage.
- Implemented spending insights, including:
  - Spending categorization.
  - Average expense calculation.
  - Anomaly detection in transactions.

## Future Features

- Support for additional UPI apps (e.g., PhonePe, Paytm).
- Automated report generation.
- Cloud storage for synced access across devices.
- Enhanced AI-driven anomaly detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions.

## Contact

For queries or support, reach out to [your email] or create an issue on the GitHub repository.


