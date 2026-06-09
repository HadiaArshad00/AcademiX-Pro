# AcademiX Pro - Python Backend API

Flask-based backend server for AcademiX Pro platform with advanced features.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python backend.py
```

Server will run on `http://localhost:5000`

## API Endpoints

### Subjects
- `GET /api/subjects` - Get all subjects
- `GET /api/subjects/<id>` - Get subject details
- `GET /api/subjects/<id>/resources` - Get subject resources

### Search
- `GET /api/search?q=<query>` - Search all resources
- `GET /api/search?type=<type>&year=<year>` - Advanced filtering

### User Progress
- `POST /api/progress` - Save progress
- `GET /api/progress` - Get user progress
- `GET /api/analytics` - Get analytics

### Resources
- `GET /api/resources` - Get all resources
- `POST /api/resources/bookmark` - Bookmark resource
- `GET /api/resources/recommendations` - Get AI recommendations

## Database Schema

### Subjects Table
```sql
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    icon VARCHAR(10),
    description TEXT,
    resources_count INTEGER,
    papers_count INTEGER
);
```

### Resources Table
```sql
CREATE TABLE resources (
    id INTEGER PRIMARY KEY,
    subject_id INTEGER,
    title VARCHAR(200),
    type VARCHAR(50),
    year INTEGER,
    url VARCHAR(500),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
```

## Features

- 📚 Resource management
- 🔍 Advanced search
- 📊 Analytics engine
- 💾 Data persistence
- 🔄 Cloud sync
- 🤖 AI recommendations

## Testing

```bash
python -m pytest tests/
```

## Documentation

Full API documentation available at `/api/docs` when server is running.
