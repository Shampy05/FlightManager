# Airlines Flight Database Management System

This project is a Flight Database Management System designed for an Airlines company. It allows you to manage information about flights, aircraft, pilots, and provides various functionalities for adding, updating, searching, and viewing flight data. The system also offers statistics on flights per week and flights to specific destinations per month.

The application is built using Python and utilizes the SQLAlchemy ORM for interacting with a SQLite database. It follows a modular structure, separating database models, services, utilities, and views into distinct directories.

## Features

- Add, update, and delete flights, aircraft, and pilots.
- View all flights, aircraft, and pilots.
- Calculate summary statistics on flights per week and flights to specific destinations per month.
- Search data based on specific attributes.
- User-friendly console-based interface.
- Error handling and data validation.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/airlines-flight-db-management.git
   ```

2. Navigate to the project directory:

```
cd airlines-flight-db-management
```

3. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Set up the database:

- The database is already set up with an SQLite database file (database.db) included in the project.
- If you want to start with a fresh database, delete the existing database.db file.
- Run the following command to create a new empty database:

```
python db/base.py
```
- This will create the necessary tables based on the defined models.

6. Start the application:

```
python main.py
```

7. Follow the on-screen menu options to interact with the Flight Database Management System.

## Usage
- Upon running the application, you will be presented with a main menu offering different options for managing flights, aircraft, pilots, and statistics.
- Select an option by entering the corresponding number and follow the prompts to perform the desired action.
- The application will provide feedback and display results as necessary.
- Use the options to add, update, or delete records, view existing records, and access statistics.

## Contact
For any inquiries or feedback, please contact Shampy05 at sharmapranshu317@gmail.com