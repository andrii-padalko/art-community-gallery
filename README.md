# Art Community Gallery

Art Community Gallery is a platform where artists can showcase their artwork. 
Users, primarily artists, can register on the platform to upload their paintings, 
specify characteristics of their artwork, and manage genres, styles, and materials associated with their creations.

## Check it out!

[Gallery project deployed to Render] (https://art-community-gallery.onrender.com/)

![img.png](img.png)

## Features

- **User Registration**: Artists can register on the platform to create their accounts.
- **Painting Management**: Artists can upload their paintings, specify details such as title, creation year, genre, style, and materials used.
- **Genre, Style, and Material Management**: Artists can add, edit, and delete genres, styles, and materials to categorize their artwork effectively.
- **User Profiles**: Each artist has a profile page displaying their uploaded paintings and other relevant information.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/art-community-gallery.git

2. Navigate to the project directory:
    ``` bash
   cd art-community-gallery

3. Install dependencies:
    ```bash
   pip install -r requirements.txt

4. Apply database migrations:
    ```bash
   python manage.py migrate

5. Run the development server:
    ```bash
   python manage.py runserver

6. Access the application in your web browser at http://localhost:8000/


Technologies Used:
 - Django: Web framework for building the backend of the application.
 - HTML, CSS, JavaScript: Frontend technologies for building the user interface and interactions.
 - SQLite: Database management system for storing application data during development.