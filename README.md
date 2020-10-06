# SocialNetwork
Assessment project to StarNavi.

## How to run
1. Download repository `git clone https://github.com/Velx/SocialNetwork.git`
2. Choose which config you want to run:
   - For production version with PostgreSQL add `.env` file to root and define  environment variables:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - SQL_HOST
      - SQL_PORT
      - REDIS_HOST
      - REDIS_POST
      - DEBUG
      - SECRET_KEY
   - For development version with SQLite3 go to the next step
3. Run it with docker-compose `docker-compose up -d` or start redis service with default settings and run server with `python manage.py runserver`
4. Now server is running on port 8000

## Endpoints and documentation
https://documenter.getpostman.com/view/5958867/TVRg8AQv
