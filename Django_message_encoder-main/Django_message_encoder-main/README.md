# Message Encoder Django Application

This Django application encodes messages based on whether the day is odd or even. On odd days, each letter is encoded with a two-digit number (A=01, B=02, ..., Z=26). On even days, each letter is encoded with a three-digit number prefixed by 5 (A=501, B=502, ..., Z=526).

## Features

- Encode messages based on odd or even days.
- Simple web interface to input messages and select the day type.
- Display encoded messages.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required packages:**

   ```bash
   pip install django

4. **Run database migrations:**

   ```bash
   python manage.py migrate

5. **Run the development server:**

    ```bash
    python manage.py runserver

6. Open your web browser and navigate to http://127.0.0.1:8000/ to use the application.

## Usage
1. Open the application in your web browser:
   Navigate to http://127.0.0.1:8000/.

2. Enter your message:
   Type the message you want to encode in the message input box.

3. Select the day type:
   Choose whether it is an odd or even day.

4. Submit the form:
   Click the "Encode" button to see the encoded message.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Django documentation and
GitHub for hosting the repository





