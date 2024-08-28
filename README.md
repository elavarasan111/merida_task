# merida_task
Banking Application with JWT Authentication
Project Overview
This project is a Django-based web application that simulates a banking system where users can create and manage multiple bank accounts. It includes user authentication and authorization using JSON Web Tokens (JWT), and supports account operations like deposit, withdrawal, and account closure. The application also maintains detailed user login/logout history and transaction history, which is accessible to bank employees even after an account has been closed.

Features
User Authentication: Users can sign up, log in, and log out. JWT is used for secure authentication.
Bank Account Management: Users can create accounts with different banks (SBI, ICICI Bank, KTK Bank), deposit and withdraw money, and close accounts.
User Dashboard: After logging in, users can view their account details, make deposits and withdrawals, and close their accounts.
History Tracking: The application tracks and stores user login/logout history and transaction history. This data remains even after the account is closed and is viewable only by bank employees.
Role Management: Users can be regular customers or bank employees, with different access levels.
Technology Stack
Backend: Django, Django REST Framework
Authentication: JWT (JSON Web Tokens)
Database: MySQL
Serialization: Django REST Framework serializers
