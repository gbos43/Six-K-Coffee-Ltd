# Build React app
FROM node:20-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Build Flask app and serve React build as static
FROM python:3.11-slim
WORKDIR /app
COPY server/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY server/ ./server/
COPY --from=build /app/build ./build

WORKDIR /app/server
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]