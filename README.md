# Quote Search Application

## Overview

This Python application enables users to search for quotes by author name or tag, drawing upon a database of inspiring and thought-provoking quotes. It offers a command-line interface for efficient interaction. To enhance performance, it incorporates caching using Redis.

## Features

- Search for quotes by author name, allowing for partial matches.
- Search for quotes by tag, allowing for single or multiple tags.
- Display search results in a clear and concise format.
- Cache frequently accessed quotes to improve response times.

## Installation

**Prerequisites:**

- Python 3.11 or later
- MongoDB database (cloud or Docker)
- Redis instance (Docker recommended)

**Steps:**

1. **Set up MongoDB:**
   - Choose a cloud-based MongoDB service or deploy a local instance using Docker.
2. **Set up Redis:**
   - Download Redis: 
   ```bash
   docker pull redis/redis-stack
   ```
   - Start a Redis instance using Docker: 
   ```bash
   docker run --name quote-redis -p 6379:6379 -p 8001:8001 -d redis
   ```
3. **Install dependencies:**
   - **Install dependencies using Poetry:**
   ```bash
   poetry install --no-root
   ```
   - **Activate the virtual environment:**
     ```bash
     poetry shell
     ```
4. **Create a .env file:**
   - In the project's root directory, create a file named `.env`.
   - Add the following lines, replacing the placeholders with your actual MongoDB credentials:

     ```
     DB_USER = your_mongodb_username
     DB_PASSWORD = your_mongodb_password
     DB_HOST = your_mongodb_host
     ```
5. **Seed the database with sample data:**
   - Run the following command to populate the database with sample authors and quotes from `authors.json` and `quotes.json`:
     ```bash
     python seed.py
     ```

## Usage

1. Run the application: 
   ```bash
   python app.py
   ```
2. Enter commands as prompted:
   - `name:<author_name>` to search by author (e.g., `name:Einstein`, `name:st` for partial matches)
   - `tag:<tag_name>` to search by tag (e.g., `tag:li` for partial matches)
   - `tags:<tag1>,<tag2>` to search by multiple tags (e.g., `tags:life,live`)
   - `help` for a list of commands
   - `exit` to quit

## Project Structure

- **app.py:** Main application file with command-line interface and search logic
- **models.py:** Defines MongoEngine models for Author and Quote
- **authors.json:** Sample author data for seeding the database
- **quotes.json:** Sample quote data for seeding the database
- **seeds.py:** Script to populate the database with sample data
- **pyproject.toml:** Poetry configuration file for managing dependencies

## Technologies Used

- Python
- MongoDB
- MongoEngine (MongoDB ODM)
- Redis
- redis-lru (Redis LRU cache library)
- Python-dotenv (for managing environment variables)
