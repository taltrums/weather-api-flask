### Weather API Flask App
This Flask web application retrieves current weather data for a specified city and provides it in either JSON or XML format. It uses the RapidAPI service for weather data.

## Prerequisites
Before running the application, make sure you have the following:

- Python 3.x installed on your system.
- A RapidAPI account and API key. You can sign up for an account and obtain your API key from the RapidAPI website.

## Setup
1. Clone this repository to your local machine:
```bash
git clone https://github.com/taltrums/weather-api-flask.git
```
2.  Navigate to the project directory:
```bash
cd weather-api-flask
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
4. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```
5. Install the required Python packages:
```bash
pip install -r requirements.txt
```
6. Create an .env file in the project root directory and add your RapidAPI API key as follows:
```makefile
API_KEY=your_api_key_here
```
Replace your_api_key_here with your actual RapidAPI API key.

### Running the Application
To run the Flask application, execute the following command from the project root directory:
```bash
python run.py
```
The application will start, and you should see output indicating that the server is running. By default, the server runs on http://127.0.0.1:5000/.

### Using the API
You can access the API by sending a POST request to http://127.0.0.1:5000/getCurrentWeather with a JSON payload containing the "city" and "output_format" fields. For example:

```json
{
    "city": "Bangalore",
    "output_format": "json"
}
```
Replace "Bangalore" with the city you want to get weather data for.
Set "output_format" to either "json" or "xml".
The API will respond with weather data in the specified format.

### Stopping the Application
To stop the Flask application, press Ctrl + C in the terminal where the application is running.