# ECAT-Preprator
ECAT Prep Platform
Overview
The ECAT Prep Platform is a comprehensive web application designed to help students prepare for the Engineering College Admission Test (ECAT). The platform provides chapter-wise practice questions, mock tests, performance analytics, and gamification features to enhance the learning experience. Built with Flask backend and modern vanilla JavaScript frontend using Vite.js, it features ML-powered score prediction, real-time analytics, and an admin panel for content management.

Latest Update: Restructured into standard client-server architecture with separate client/ and server/ folders for better organization, scalability, and modern development practices.

User Preferences
Preferred communication style: Simple, everyday language.

System Architecture
Backend Architecture (server/)
Framework: Flask with SQLAlchemy ORM for database operations
Authentication: Dual authentication system using both session-based authentication for web routes and JWT tokens for API endpoints
Database Schema: Relational database design with User, Subject, Chapter, Question, QuizAttempt, and Badge entities
ML Integration: Scikit-learn based prediction model for ECAT score forecasting using user performance metrics
API Structure: RESTful endpoints organized by functionality (questions, analytics, gamification)
Location: All backend files organized in /server/ directory
Frontend Architecture (client/)
Technology Stack: Modern vanilla JavaScript with Vite.js build tool, Bootstrap for styling and Chart.js for data visualization
Component Structure: ES6 modules with service classes for API communication, authentication, and state management
Build System: Vite.js for development server, hot reload, and production optimization
Template System: Single-page application with JavaScript-based routing and dynamic content rendering
Real-time Features: Dynamic question loading, timer functionality, and progress tracking
Location: All frontend files organized in /client/ directory with proper src/, public/, and assets/ structure
Data Storage Solutions
Primary Database: SQLite for development with PostgreSQL support configured for production
Session Management: Flask sessions for user state management
Model Persistence: Joblib for saving and loading trained ML models
Authentication and Authorization
Multi-tier Authentication: Session-based for web interface, JWT for API access
Role-based Access: User and admin roles with corresponding decorators for route protection
Security Features: Password hashing with Werkzeug, secure session management
Key Design Patterns
MVC Architecture: Clear separation between models (SQLAlchemy), views (Jinja2 templates), and controllers (Flask routes)
Decorator Pattern: Extensive use of decorators for authentication and authorization
Factory Pattern: Database and application initialization using factory methods
Observer Pattern: Event-driven quiz state management and progress tracking
External Dependencies
Core Framework Dependencies
Flask: Web framework with SQLAlchemy integration for database operations
SQLAlchemy: ORM for database interactions with support for multiple database backends
Flask-CORS: Cross-origin resource sharing support for API endpoints
Frontend Libraries
Bootstrap: CSS framework for responsive UI design
Chart.js: JavaScript charting library for analytics visualization
Font Awesome: Icon library for enhanced UI elements
Axios: HTTP client for API communication
Machine Learning Stack
Scikit-learn: Machine learning library for score prediction models
NumPy & Pandas: Data manipulation and numerical computing
Joblib: Model serialization and persistence
Security and Authentication
PyJWT: JSON Web Token implementation for API authentication
Werkzeug: Password hashing and security utilities
Development and Deployment
Flask-CORS: Development server CORS handling
ProxyFix: Middleware for handling reverse proxy headers in production environments
Database Support
SQLite: Default development database
PostgreSQL: Production database support through SQLAlchemy database URI configuration
