# HR-Management-Django-Angular-App-
Branch and Employee Management System
![image](https://github.com/ReemAbdelghany/HR-Management-Django-Angular-App-/assets/127961912/4d2c8762-c29c-479a-ac43-dd9db2523636)
![image](https://github.com/ReemAbdelghany/HR-Management-Django-Angular-App-/assets/127961912/158ef9c1-f722-41aa-bdc8-6ad6650ac14a)

# Project Title

HR Management System

## Description

This project is a web-based HR Management System that allows users to manage branches and employees. The system provides functionality to create, update, and delete branches and employees. It includes a user-friendly interface for easy data entry and management.

The HR Management System consists of a frontend implemented using Angular, a backend developed using Django, and a MySQL database managed using phpMyAdmin.

## Features

- **Manage Branches:** Create, update, and delete branches with fields such as name, building number, street, area, city, country, and manager.
- **Manage Employees:** Create, update, and delete employees with fields such as name, age, email, phone number, and branch.
- **Form Validation:** Input fields in the frontend forms are validated to ensure required fields are filled and correct data types are entered.
- **Data Relationships:** Employees are associated with branches through a foreign key relationship.
- **RESTful API:** The backend provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on branches and employees.
- **Data Persistence:** Branches and employees data are stored and managed in a MySQL database.
- **Responsive Design:** The frontend interface is designed to be responsive and compatible with various screen sizes.

## Technologies Used

- Angular
- Django
- MySQL
- phpMyAdmin

## Installation and Setup

1. Clone the repository: `git clone https://github.com/your-username/repository.git`
2. Install Angular dependencies: `npm install`
3. Install Django dependencies: `pip install -r requirements.txt`
4. Set up MySQL database using phpMyAdmin or any other MySQL management tool.
5. Update the database configuration in the Django settings file.
6. Run the Django development server: `python manage.py runserver`
7. Run the Angular development server: `ng serve`
8. Access the application in a web browser: `http://localhost:4200`

## Usage

1. Open the application in a web browser.
2. Use the provided forms to create, update, and delete branches and employees.
3. The tables display existing branches and employees with options to edit or delete records.

## API Endpoints

- `GET /branches/`: Get all branches
- `POST /branches/`: Create a new branch
- `GET /branches/:id/`: Get a specific branch by ID
- `PUT /branches/:id/`: Update a specific branch by ID
- `DELETE /branches/:id/`: Delete a specific branch by ID
- `GET /employees/`: Get all employees
- `POST /employees/`: Create a new employee
- `GET /employees/:id/`: Get a specific employee by ID
- `PUT /employees/:id/`: Update a specific employee by ID
- `DELETE /employees/:id/`: Delete a specific employee by ID

## Contributors

- [Reem Abdelghany](https://github.com/ReemAbdelghany)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

