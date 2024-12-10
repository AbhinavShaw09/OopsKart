#!/bin/bash
export PATH="/opt/poetry-venv/bin:$PATH"

# Wait for PostgreSQL to be ready
while ! nc -z postgres 5432; do
    echo "Waiting for PostgreSQL to start..."
    sleep 1
done
echo "postgres started"

# Apply database migrations
python core/manage.py migrate

python core/manage.py collectstatic

# Start the Django application with Gunicorn
exec gunicorn --chdir core --bind 0.0.0.0:8000 core.wsgi:application