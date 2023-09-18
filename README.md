# Django-CRM

This repository holds the source code for a CRM developed using Django.

## Tech Stack

-   HTML, [TailwindCSS](https://tailwindcss.com/)
-   [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)

-   [PostgreSQL](https://www.postgresql.org/)

## Run this project

### Clone the repository

```bash
git clone https://github.com/ahs718/django-crm
cd django-crm
```

### Creating and activating the python virtual environment

bash/zsh:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

fish shell:

```bash
python3 -m venv .venv
source .venv/bin/activate.fish
```

### Install dependencies

````bash
pip install -r requirements.txt

pnpm install
pnpm apply_style
````

### Add .env variables

Inside the `djcrm/` directory, there is a `.env.example` file with the required environment variables. Rename `.env.example` to `.env` and add the required secrets.

### Run the server

```bash
python3 manage.py runserver
```
