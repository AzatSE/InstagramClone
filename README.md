<div align="center">

# InstagramClone

**Instagram на Django — учебный проект в активной разработке**

[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-in%20development-yellow)]()

</div>

---

### ✅ Готово
Профили • Лента постов • Лайки • Загрузка фото

### 🚧 В работе
Комментарии • Подписки • Поиск • Уведомления

---

## Быстрый старт

\`\`\`bash
git clone https://github.com/username/InstagramClone.git
cd InstagramClone

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py runserver
\`\`\`

Открыть: \`http://127.0.0.1:8000/\`

---

## Структура

\`\`\`
InstagramClone/
├── config/     # настройки Django
├── posts/      # посты, лайки, лента
├── media/      # загруженные файлы
└── .env.example
\`\`\`

---

<div align="center">

**Django** · **SQLite** · **python-dotenv**

</div>