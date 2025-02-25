# Password Generator Backend

This is the backend for a Password Generator application built with **Flask** and deployed on **Railway**. It provides an API endpoint to generate random passwords based on user-defined parameters.

---

## Features

- Generate random passwords with customizable length.
- Include/exclude numbers, symbols, uppercase, and lowercase letters.
- Exclude similar characters for better readability.
- Simple and lightweight API.

---

## Tech Stack

- **Backend:** Flask (Python)
- **Deployment:** Railway

---

## Installation

### Prerequisites
- Python 3.x installed
- Pip (Python package manager)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/password-generator-backend.git
   cd password-generator-backend
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and set the following environment variables:
   ```sh
   FLASK_APP=app.py
   FLASK_ENV=production
   ```

5. Run the application locally:
   ```sh
   flask run
   ```

---

## API Endpoints

### Generate Password
**Endpoint:** `GET /generate-password`

**Query Parameters:**
- `length` (int) - Length of the password.
- `numbers` (bool) - Include numbers.
- `symbols` (bool) - Include symbols.
- `uppercase` (bool) - Include uppercase letters.
- `lowercase` (bool) - Include lowercase letters.
- `exclude_similar` (bool) - Exclude similar-looking characters.

**Example Request:**
```sh
GET /generate-password?length=12&numbers=true&symbols=true&uppercase=true&lowercase=true&exclude_similar=false
```

**Example Response:**
```json
{
  "Password": "A1!bC2@dE3#"
}
```

---

## Live Demo

You can access the live version of the app here:
[Live Demo](https://password-generator-ten-beryl.vercel.app/)

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Umeen Rathnayake**.
