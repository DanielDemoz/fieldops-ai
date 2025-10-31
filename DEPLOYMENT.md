# Deployment Guide

## Local Development

For local development and testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python run_demo.py

# Run dashboard
streamlit run app/dashboard.py
```

## Production Deployment

### Option 1: Streamlit Cloud

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click

### Option 2: Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Option 3: Traditional Server

1. Set up Python environment on server
2. Install dependencies
3. Configure database (PostgreSQL recommended for production)
4. Set up reverse proxy (nginx)
5. Use process manager (systemd, supervisor)
6. Configure SSL certificates

## Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost/fieldops
SECRET_KEY=your-secret-key-here
```

## Database Migration

For production, use Alembic for migrations:

```bash
alembic upgrade head
```

## Security Considerations

- Change default passwords
- Use environment variables for secrets
- Enable HTTPS
- Set up proper authentication
- Regular security updates

