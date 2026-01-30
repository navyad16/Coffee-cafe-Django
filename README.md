# ☕ Coffee Cafe Management System (Django)

A full-featured Coffee Cafe web application built using **Django**.  
Users can browse the menu, add items to cart, manage quantity, checkout, and view order history.

---

## 🚀 Features

- User authentication (Signup / Login / Logout)
- Menu categories (Hot Coffee, Cold Coffee, Snacks, Desserts)
- Add to Cart with quantity increase/decrease
- Dynamic cart total calculation
- Checkout system (without payment gateway)
- Order history for users
- Admin panel for menu & order management
- Responsive and modern UI

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Auth
- **Static Files:** Django Static & Media

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/coffee-cafe-django.git
cd coffee-cafe-django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
