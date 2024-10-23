# DS blog using SQLAlchemy

Welcome to the repository for building a Data Science Blog using Django and Flask from scratch with SQLite3! This project will guide you through creating a simple yet functional blog application where you can share your data science projects, articles, and tutorials.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project is designed to help you learn how to build a full-stack web application using two of the most popular web frameworks, Django and Flask, while leveraging SQLite3 as the database. Whether you're a beginner or an experienced developer, this guide will help you understand the core concepts and implementation details required to create a functional blog.

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete (CRUD) operations for blog posts
- Comment system for each blog post
- Tagging system for categorizing posts
- Simple and clean user interface
- Responsive design

## Tech Stack

- **Backend Framework:** Django & Flask
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)
- **Deployment:** Gunicorn, Nginx, Docker (optional)

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)
- Git

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/data-science-blog.git
   cd data-science-blog
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations and Create Database**

   ```bash
   python manage.py migrate  # For Django
   flask db upgrade  # For Flask (if using Flask-Migrate)
   ```

5. **Run the Development Server**

   - For Django:
     ```bash
     python manage.py runserver
     ```
   - For Flask:
     ```bash
     flask run
     ```

6. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:8000` for Django or `http://127.0.0.1:5000` for Flask.

## Usage

- **Creating an Account:** Register a new user account to start creating blog posts.
- **Writing Posts:** Use the "New Post" feature to write and publish your blog entries.
- **Editing Posts:** Edit or delete your posts from your profile page.
- **Commenting:** Engage with other users by leaving comments on their posts.
- **Tagging:** Use tags to categorize your posts and make them easily searchable.

## Project Structure

The repository is organized as follows:

```
data-science-blog/
├── django_app/                  # Django project files
│   ├── blog/
│   ├── manage.py
│   ├── ... (other Django app files)
├── flask_app/                   # Flask project files
│   ├── app/
│   ├── run.py
│   ├── ... (other Flask app files)
├── requirements.txt             # List of dependencies
├── README.md                    # This readme file
└── ... (other project files)
```

## Contributing

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's coding style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Screenshots

![Screenshot 2024-06-01 at 22-38-14 Screenshot](https://github.com/figo2001/DS-django-blog/assets/78696850/24a8f4d6-eb17-45ce-9cad-f3aab223bf08)





Happy coding!

---

Feel free to customize this README to better fit your project and preferences.
