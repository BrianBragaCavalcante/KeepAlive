
# KeepAlive

**KeepAlive** is a simple Flask application designed to keep websites alive by regularly sending HTTP requests. It is ideal for platforms that deactivate site instances due to inactivity.

## 🚀 Features

- Sends periodic requests (ping) to keep websites alive.
- Checks the status of websites and returns the HTTP status code.

## 🛠️ Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework for building the server.
- **Requests**: Library for sending HTTP requests.
- **JSON**: Format for storing the list of websites.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/KeepAlive.git
   cd KeepAlive
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the `sites.json` file with the following structure:
   ```json
   {
     "sites": [
       "https://example.com",
       "https://anothersite.com"
     ]
   }
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## 🌐 Routes

- **`/`**: Returns the HTTP status of the websites configured in the `sites.json` file.
- **`/turnon`**: Waits 5 minutes before sending a request to reactivate the site (feature in development).

## 📝 How It Works

KeepAlive reads the websites to be monitored from a `sites.json` file and sends periodic requests to ensure the websites are not deactivated due to inactivity.

## 📄 License

This project is licensed under the MIT License. Feel free to contribute and adapt as needed.
