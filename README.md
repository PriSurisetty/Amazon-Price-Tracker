# Amazon Price Tracker

This Python script tracks the price of a product on Amazon and sends an email alert when the price drops below a specified threshold.

## Features

- **Price Monitoring**: Checks the price of an Amazon product.
- **Email Alerts**: Sends an email when the price is below your target.
- **Customizable**: Set your own product URL and target price.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
2. **Navigate to the Project Directory**:
   ```bash
   cd amazon-price-tracker
3. **Install Required Packages**:
   '''bash
   pip install beautifulsoup4 requests
4. **Set Up Environment Variables**:
   - LINK=your_amazon_product_url
   - USERNAME=your_email_address
   - PASSWORD=your_email_password
5. **Run the script with**:
   python main.py

## How It Works
- Scrapes the product price from Amazon using BeautifulSoup.
- Compares the current price with the target price.
- Sends an email alert if the price is below the target.


