# ECAT Prep Platform - Project Structure

## Overview

The ECAT Prep Platform has been restructured into a standard client-server architecture for better maintainability, scalability, and development workflow.

## Directory Structure

```
ecat-prep-platform/
├── client/                 # Frontend application
│   ├── public/            # Static assets and entry HTML
│   │   └── index.html     # Main HTML entry point
│   ├── src/               # Source code
│   │   ├── css/           # Custom stylesheets
│   │   ├── js/            # JavaScript modules
│   │   └── main.js        # Main application entry point
│   ├── components/        # Reusable UI components
│   ├── assets/           # Images, icons, and other assets
│   ├── dist/             # Built production files (generated)
│   ├── package.json      # Node.js dependencies and scripts
│   ├── vite.config.js    # Vite build configuration
│   ├── README.md         # Client documentation
│   └── .gitignore        # Client-specific gitignore
├── server/                # Backend application
│   ├── static/           # Server-side static files
│   ├── templates/        # Jinja2 templates
│   ├── *.py              # Python modules
│   │   ├── main.py       # Flask app entry point
│   │   ├── app.py        # Flask application factory
│   │   ├── models.py     # Database models
│   │   ├── api.py        # API endpoints
│   │   ├── auth.py       # Authentication logic
│   │   └── ...           # Other Python modules
│   ├── requirements.txt  # Python dependencies
│   ├── pyproject.toml    # Python project configuration
│   ├── start.sh          # Server startup script
│   └── README.md         # Server documentation
├── main.py               # Root entry point for Replit
├── replit.md             # Project documentation and preferences
└── PROJECT_STRUCTURE.md  # This file
```

## Technology Stack

### Client (Frontend)
- **Build Tool**: Vite.js for modern development and building
- **UI Framework**: Bootstrap 5 with dark theme
- **JavaScript**: Vanilla ES6+ modules, no framework dependencies
- **Charts**: Chart.js for analytics visualization
- **Icons**: Font Awesome for consistent iconography
- **HTTP Client**: Axios for API communication

### Server (Backend)
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL (production) / SQLite (development)
- **Authentication**: Session-based + JWT tokens
- **ML**: Scikit-learn for score prediction
- **API**: RESTful endpoints with proper error handling
- **Server**: Gunicorn for production deployment

## Development Workflow

### Client Development
```bash
cd client
npm install          # Install dependencies
npm run dev          # Start development server (port 3000)
npm run build        # Build for production
npm run preview      # Preview production build
```

### Server Development
```bash
cd server
pip install -r requirements.txt    # Install dependencies
python main.py                     # Development server
# OR
gunicorn --bind 0.0.0.0:5000 --reload main:app  # Production server
```

### Full Stack Development
1. Start the backend server (port 5000)
2. Start the frontend dev server (port 3000)
3. Frontend proxies API calls to backend via Vite configuration

## Key Benefits of This Structure

### Separation of Concerns
- **Client**: Focused purely on user interface and experience
- **Server**: Focused on business logic, data, and API endpoints
- **Clear boundaries**: Each side has distinct responsibilities

### Development Benefits
- **Independent development**: Frontend and backend teams can work separately
- **Technology flexibility**: Each side can use optimal tools and frameworks
- **Build optimization**: Separate build processes for optimal performance
- **Testing**: Easier to unit test business logic and UI components separately

### Deployment Benefits
- **Scalability**: Can scale frontend and backend independently
- **CDN optimization**: Frontend assets can be served from CDN
- **API reusability**: Backend API can serve multiple clients (web, mobile, etc.)
- **Version control**: Cleaner git history with separated concerns

## API Communication

The client communicates with the server via:
- **Base URL**: `http://localhost:5000` (development)
- **Authentication**: JWT tokens for API endpoints
- **Error handling**: Consistent error response format
- **CORS**: Configured for cross-origin requests during development

## Environment Configuration

### Development
- Client runs on port 3000 with hot reload
- Server runs on port 5000 with auto-restart
- Vite proxy forwards `/api/*` requests to backend

### Production
- Client builds to static files in `dist/`
- Server serves API and can optionally serve client files
- Environment variables for database and secrets

## Migration from Monolithic Structure

The original monolithic Flask application has been reorganized:

1. **Templates and static files**: Remain in server for Jinja2 rendering
2. **Client-side JavaScript**: Extracted to modern ES6 modules
3. **API endpoints**: Maintained in server with proper CORS
4. **Authentication**: Hybrid approach (sessions + JWT)
5. **Build process**: Added Vite.js for modern frontend tooling

This structure maintains backward compatibility while enabling modern development practices and future scalability.