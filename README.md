# Django-CRM

<img width="1440" alt="Screenshot 2023-09-18 at 1 17 32 PM" src="https://github.com/ahs718/django-crm/assets/101739679/24a96d91-50d4-4942-afa0-32bfa10cdf83" align="left" style="zoom:50%;" />

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

## Image Gallery

### Manage Leads

<img width="1440" alt="Screenshot 2023-09-18 at 1 17 47 PM" src="https://github.com/ahs718/django-crm/assets/101739679/ce1d0fae-5b1c-400b-87e7-8bce752f3f40" align="left" style="zoom:50%;" />

### Manage Agents

<img width="1440" alt="Screenshot 2023-09-18 at 1 18 24 PM" src="https://github.com/ahs718/django-crm/assets/101739679/c51b4fe9-2e3e-43fb-9d13-5e3ba1c97d6c" align="left" style="zoom:50%;" />

### Manage Categories

<img width="1440" alt="Screenshot 2023-09-18 at 1 17 57 PM" src="https://github.com/ahs718/django-crm/assets/101739679/4fb6ab20-d09c-40d9-a021-98f830c6f64a" align="left" style="zoom:50%;" />

### Lead Detail View

<img width="1440" alt="Screenshot 2023-09-18 at 1 18 07 PM" src="https://github.com/ahs718/django-crm/assets/101739679/098a2564-e660-4ee2-b6cb-572f2fa76d82" align="left" style="zoom:50%;" />
