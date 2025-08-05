# ECAT Prep Platform Documentation

## Table of Contents
1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Backend Architecture](#backend-architecture)
4. [Frontend Architecture](#frontend-architecture)
5. [Data Storage](#data-storage)
6. [Authentication & Authorization](#authentication--authorization)
7. [Key Design Patterns](#key-design-patterns)
8. [External Dependencies](#external-dependencies)
9. [Database Schema](#database-schema)
10. [API Structure](#api-structure)
11. [Deployment](#deployment)

## Overview

The ECAT Prep Platform is a comprehensive web application designed to help students prepare for the Engineering College Admission Test (ECAT). The platform provides an engaging and effective learning experience through various features and modern web technologies.

### Key Features
- **Chapter-wise Practice Questions** - Organized study materials by subject and chapter
- **Mock Tests** - Full-length practice examinations
- **Performance Analytics** - Detailed insights into student progress
- **Gamification Features** - Badges and achievements to motivate learning
- **ML-powered Score Prediction** - Intelligent forecasting based on performance metrics
- **Real-time Analytics** - Live performance tracking and feedback
- **Admin Panel** - Content management system for administrators

### Latest Update
The platform has been restructured into a standard client-server architecture with separate `client/` and `server/` folders for better organization, scalability, and modern development practices.

## System Architecture

The ECAT Prep Platform follows a modern client-server architecture pattern:

```
ECAT-Prep-Platform/
├── client/              # Frontend application
│   ├── src/            # Source code
│   ├── public/         # Static assets
│   └── assets/         # Application assets
└── server/             # Backend application
    ├── models/         # Database models
    ├── routes/         # API endpoints
    └── services/       # Business logic
```

### Architecture Benefits
- **Separation of Concerns** - Clear distinction between frontend and backend responsibilities
- **Scalability** - Independent scaling of client and server components
- **Development Efficiency** - Parallel development workflows
- **Deployment Flexibility** - Independent deployment strategies

## Backend Architecture

### Technology Stack
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Dual system (Sessions + JWT)
- **ML Integration**: Scikit-learn for predictive analytics

### Directory Structure
```
server/
├── app.py              # Application entry point
├── models/             # Database models
├── routes/             # API route handlers
├── services/           # Business logic services
├── ml/                 # Machine learning components
└── config/             # Configuration files
```

### Core Components

#### Database Models
- **User**: Student and admin user management
- **Subject**: Academic subjects (Physics, Chemistry, Math, etc.)
- **Chapter**: Subject subdivisions
- **Question**: Practice questions and answers
- **QuizAttempt**: User quiz session records
- **Badge**: Gamification achievements

#### API Endpoints
RESTful API structure organized by functionality:
- `/api/questions` - Question management
- `/api/analytics` - Performance analytics
- `/api/gamification` - Badges and achievements
- `/api/auth` - Authentication endpoints

#### ML Integration
- **Score Prediction Model**: Uses scikit-learn algorithms
- **Performance Metrics**: Analyzes user quiz attempts
- **Model Persistence**: Joblib for model serialization

## Frontend Architecture

### Technology Stack
- **Build Tool**: Vite.js for development and production builds
- **Language**: Modern vanilla JavaScript (ES6+)
- **Styling**: Bootstrap CSS framework
- **Charts**: Chart.js for data visualization
- **Icons**: Font Awesome icon library

### Directory Structure
```
client/
├── src/
│   ├── components/     # Reusable UI components
│   ├── services/       # API communication services
│   ├── utils/          # Utility functions
│   └── styles/         # Custom CSS styles
├── public/             # Static assets
└── assets/             # Application assets
```

### Key Features
- **Single Page Application (SPA)** - JavaScript-based routing
- **Component Architecture** - ES6 modules for code organization
- **Service Classes** - Centralized API communication
- **Real-time Updates** - Dynamic content loading and progress tracking
- **Responsive Design** - Bootstrap-based mobile-friendly interface

## Data Storage

### Database Configuration
- **Development**: SQLite for rapid development and testing
- **Production**: PostgreSQL for robust production deployment
- **ORM**: SQLAlchemy for database abstraction and migrations

### Session Management
- **Web Interface**: Flask sessions for user state management
- **API Access**: JWT tokens for stateless authentication

### Model Persistence
- **ML Models**: Joblib for saving and loading trained models
- **Performance Data**: Relational database storage for analytics

## Authentication & Authorization

### Multi-tier Authentication System
1. **Session-based Authentication**
   - Used for web interface routes
   - Server-side session management
   - Automatic session cleanup

2. **JWT Token Authentication**
   - Used for API endpoints
   - Stateless authentication
   - Token expiration handling

### Role-based Access Control
- **User Role**: Standard student access
- **Admin Role**: Content management and analytics access
- **Decorator-based Protection**: Route-level authorization

### Security Features
- **Password Hashing**: Werkzeug security utilities
- **Secure Sessions**: Flask session management
- **CORS Handling**: Cross-origin resource sharing configuration

## Key Design Patterns

### MVC Architecture
- **Models**: SQLAlchemy database models
- **Views**: Jinja2 templates and JavaScript components
- **Controllers**: Flask route handlers

### Decorator Pattern
- Authentication decorators for route protection
- Authorization decorators for role-based access
- Logging decorators for request tracking

### Factory Pattern
- Database initialization and configuration
- Application factory for different environments

### Observer Pattern
- Event-driven quiz state management
- Progress tracking and notifications
- Real-time analytics updates

## External Dependencies

### Backend Dependencies
```python
# Core Framework
Flask==2.3.3
SQLAlchemy==2.0.21
Flask-CORS==4.0.0

# Authentication & Security
PyJWT==2.8.0
Werkzeug==2.3.7

# Machine Learning
scikit-learn==1.3.0
numpy==1.24.3
pandas==2.0.3
joblib==1.3.2

# Database
psycopg2-binary==2.9.7  # PostgreSQL adapter
```

### Frontend Dependencies
```json
{
  "devDependencies": {
    "vite": "^4.4.5"
  },
  "dependencies": {
    "bootstrap": "^5.3.0",
    "chart.js": "^4.3.0",
    "axios": "^1.4.0"
  }
}
```

### CDN Resources
- **Font Awesome**: Icon library via CDN
- **Bootstrap**: CSS framework (with option for local build)

## Database Schema

### Core Entities

#### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Subjects Table
```sql
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Questions Table
```sql
CREATE TABLE questions (
    id INTEGER PRIMARY KEY,
    chapter_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    option_a VARCHAR(200) NOT NULL,
    option_b VARCHAR(200) NOT NULL,
    option_c VARCHAR(200) NOT NULL,
    option_d VARCHAR(200) NOT NULL,
    correct_answer CHAR(1) NOT NULL,
    difficulty_level INTEGER DEFAULT 1,
    FOREIGN KEY (chapter_id) REFERENCES chapters (id)
);
```

### Relationships
- Users have many QuizAttempts
- Subjects have many Chapters
- Chapters have many Questions
- Users can earn many Badges

## API Structure

### Authentication Endpoints
```
POST /api/auth/login     # User login
POST /api/auth/register  # User registration
POST /api/auth/logout    # User logout
GET  /api/auth/profile   # Get user profile
```

### Question Management
```
GET    /api/questions           # Get all questions
GET    /api/questions/:id       # Get specific question
POST   /api/questions           # Create new question (admin)
PUT    /api/questions/:id       # Update question (admin)
DELETE /api/questions/:id       # Delete question (admin)
```

### Analytics Endpoints
```
GET /api/analytics/performance  # User performance data
GET /api/analytics/predictions  # ML score predictions
GET /api/analytics/progress     # Learning progress
```

### Gamification
```
GET  /api/badges           # Get available badges
POST /api/badges/award     # Award badge to user
GET  /api/leaderboard      # Get user rankings
```

## Deployment

### Development Setup
```bash
# Backend setup
cd server/
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Frontend setup
cd client/
npm install
npm run dev
```

### Production Deployment
```bash
# Backend production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Frontend build
npm run build
# Serve dist/ folder with nginx or similar
```

### Environment Configuration
```python
# Production settings
DATABASE_URL = "postgresql://user:pass@localhost/ecat_db"
SECRET_KEY = "your-secret-key"
JWT_SECRET_KEY = "your-jwt-secret"
FLASK_ENV = "production"
```

### Database Migration
```bash
# Initialize database
python -c "from app import db; db.create_all()"

# For production with PostgreSQL
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please contact the development team or create an issue in the project repository.
