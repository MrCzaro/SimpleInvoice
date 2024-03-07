# SimpleInvoice

SimpleInvoice is a web application built with Django, Tailwind CSS, and FPDF, designed to simplify the process of creating, managing, and downloading invoices.

## Features

- **User Authentication**: Users can create accounts, log in, and enjoy a personalized experience.

- **Invoice Management**: Easily create, update, and manage your invoices within the application.

- **Create Similar Invoice**: Duplicate an existing invoice effortlessly to save time on repetitive tasks.

- **Download Invoice**: Generate invoices in PDF format and download them for your records.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.

- **Tailwind CSS**: A utility-first CSS framework for designing modern and responsive user interfaces.

- **FPDF**: A powerful library for creating PDF documents in Python.

## Installation

1. Clone the repository: `git clone https://github.com/MrCzaro/SimpleInvoice.git`

2. Install dependencies: `pip install -r requirements.txt`

3. Apply database migrations: `python manage.py makemigrations && python manage.py migrate`

4. Run the development server: `python manage.py runserver`

5. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

1. Create an account and log in.

2. Use the "Create New Invoice" button located in The Navbar menu on the right side to create an invoice.

3. Check your existing invoices in the Dashboard, where you can access detail pages for each invoice and perform actions like update, create similar, download, and delete.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

---

**MIT License**

Copyright (c) 2024 Mr.Czaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
