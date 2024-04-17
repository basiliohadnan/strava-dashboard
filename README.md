# My Strava Dashboard

My Strava Dashboard is a web application that fetches data from the Strava API and provides insights and statistics about your athletic activities.

## Features

- **Authentication**: Log in securely with your Strava account.
- **Activity Insights**: View insights and statistics about your activities, such as total distance, average speed, etc.
- **Interactive Dashboards**: Visualize your activity data with interactive charts and graphs.
- **Personalized Experience**: Get personalized recommendations and insights based on your activity history.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/my-strava-dashboard.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Strava API credentials:

    - Go to [Strava Developers](https://www.strava.com/settings/api) and create a new application.
    - Note down the Client ID and Client Secret.
    - Set the Redirect URI to `http://localhost:5000/strava_callback`.

4. Update `config.py` with your Strava API credentials:

    ```python
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000`.
3. Click on "Login with Strava" to authenticate with your Strava account.
4. Explore your Strava dashboard!

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/my-new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
