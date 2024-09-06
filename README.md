# Crypto Portfolio Manager

## Project Description

Crypto Portfolio Manager is a Django-based web application designed to help users manage their cryptocurrency portfolios. The app integrates with various external APIs to fetch real-time cryptocurrency prices and other relevant market data. It provides a comprehensive dashboard for users to track their investments, view detailed asset information, and analyze portfolio performance.

Key features include:
- Real-time price updates from multiple sources.
- Portfolio management with detailed asset tracking.
- Custom API endpoints for accessing portfolio data.
- User-friendly admin interface for managing assets and portfolios.

## Quick Start Guide

Follow these steps to get the project up and running locally.

### Prerequisites

- **Python**: Ensure you have Python 3.8+ installed on your system. [Download Python](https://www.python.org/downloads/)
- **Pip**: Make sure you have pip installed for managing Python packages.

### Setup

1. **Clone the Repository**

   First, clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/crypto-portfolio-manager.git
   cd crypto-portfolio-manager
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to isolate the project dependencies:
   ```
   python -m venv venv
   ```

3. Activate the Virtual Environment

    On Windows:
     ```
     venv\Scripts\activate
     ```
    
    On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Dependencies**

    Install the project dependencies from requirements.txt:
    ```
    pip install -r requirements.txt
    ```

5. **Apply Migrations**

    Run the database migrations to set up the initial schema:
    ```
    python manage.py migrate
    ```

6. **Create a Superuser**

    Create a superuser to access the Django admin interface:
    ```
    python manage.py createsuperuser
    ```

7. **Run the Development Server**

    Start the development server to run the application locally:
    ```
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

## Project Structure

- crypto_portfolio_manager/: Main project directory.
- market_data/: App for handling asset and market data.
- portfolio/: App for managing user portfolios and holdings.
- api/: App for managing and configuring the Rest API.
- manage.py: Django's command-line utility for administrative tasks.
- requirements.txt: File listing the project's dependencies.

## API Endpoints

- GET /api/assets/: Retrieve a list of all assets.
- GET /api/assets/{id}/: Retrieve details for a specific asset.
- GET /api/portfolios/: Retrieve a list of all portfolios.
- GET /api/portfolios/{id}/: Retrieve details for a specific portfolio.


## Contributing
Contributions are welcome! Please follow the contribution guidelines if you’d like to contribute to this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please contact your email.









