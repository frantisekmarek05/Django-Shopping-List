# 🛒 Nákupní Seznam v Django

Moderní webová aplikace pro správu nákupního seznamu vytvořená v Django frameworku. Aplikace nabízí intuitivní uživatelské rozhraní s příjemným designem a kompletní správou položek nákupního seznamu.


## 🏗 Architektura

Projekt využívá standardní Django architekturu s rozdělením na projekt a aplikaci:

```
django-shopping-list/
│
├── shopping_project/          # Hlavní projekt
│   ├── settings.py           # Nastavení projektu
│   ├── urls.py               # Hlavní URL konfigurace
│   └── wsgi.py              # WSGI konfigurace
│
├── shopping_list/            # Hlavní aplikace
│   ├── models.py            # Databázové modely
│   ├── views.py             # View logika
│   ├── urls.py              # URL patterns aplikace
│   ├── templatetags/        # Vlastní template tagy
│   ├── management/          # Management příkazy
│   ├── static/              # Statické soubory
│   └── templates/           # HTML šablony
│
├── templates/                # Globální šablony
│   ├── base.html           # Základní šablona
│   └── registration/       # Autentizační šablony
│
├── media/                    # Uploadované soubory
├── venv/                     # Virtuální prostředí
├── requirements.txt          # Python závislosti
├── manage.py                # Django CLI
└── db.sqlite3               # SQLite databáze
```

## 💾 Databázový model

- **ShoppingItem**
  - `itemname`: název položky
  - `completed`: stav dokončení
  - `date_added`: datum přidání
  - `category`: kategorie položky
  - `image`: obrázek položky (volitelné)
  - `user`: vazba na uživatele

## 🚀 Instalace a spuštění

### Požadavky
- Python 3.8 nebo vyšší
- pip (Python package manager)
- Virtuální prostředí (doporučeno)

### 1. Klonování repozitáře
```bash
git clone https://github.com/frantisekmarek05/Django-Shopping-List.git
cd django-shopping-list
```

### 2. Vytvoření virtuálního prostředí
```bash
# Vytvoření
python3 -m venv venv

# Aktivace na macOS/Linux
source venv/bin/activate

# Aktivace na Windows
venv\Scripts\activate
```

### 3. Instalace závislostí
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Konfigurace prostředí
```bash
# Vytvoření a aplikace migrací
python manage.py makemigrations
python manage.py migrate

# Vytvoření superuživatele
python manage.py createsuperuser
```

### 5. Spuštění vývojového serveru
```bash
python manage.py runserver
```

Aplikace bude dostupná na http://127.0.0.1:8000
