# fastapi-celery-sample

This is simple example of how to use FastAPI with Celery and DB connection

## Preparation

- Rename `.env.sample` to `.env`
- Start `docker-compose.yml` with command  
```bash
docker-compose up --build
```
- Enter `http://localhost:8000/docs/` to see swagger docs
- Enter `http://localhost:5556/` to see Celery dashboard
