# AcademiX Pro - Project Structure Guide

## Directory Organization

```
AcademiX-Pro/
│
├── 📄 index.html                 # Main application entry point
├── 📄 settings.html             # Settings & preferences page
├── 📄 README.md                 # Project documentation
├── 📄 USER_MANUAL.md            # User guide
├── 📄 BACKEND_README.md         # Backend documentation
├── 📄 requirements.txt          # Python dependencies
├── 📄 LICENSE                   # MIT License
│
├── 📁 css/
│   ├── style.css                # Main stylesheet
│   ├── animations.css           # Animation definitions
│   └── responsive.css           # Mobile responsive styles
│
├── 📁 js/
│   ├── app.js                   # Core application logic
│   ├── storage.js               # Local storage management
│   ├── three-scene.js           # 3D visualization
│   ├── analytics.js             # Analytics engine (coming)
│   └── utils.js                 # Utility functions
│
├── 📁 python/
│   ├── backend.py               # Flask API server
│   ├── database.py              # Database models
│   ├── analytics.py             # Analytics engine
│   ├── auth.py                  # Authentication (future)
│   └── config.py                # Configuration
│
├── 📁 assets/
│   ├── images/
│   │   ├── logo.png
│   │   ├── icons/
│   │   └── screenshots/
│   ├── data/
│   │   ├── subjects.json
│   │   ├── papers.json
│   │   └── resources.json
│   └── fonts/
│
├── 📁 tests/
│   ├── test_backend.py
│   ├── test_frontend.js
│   └── test_storage.js
│
└── 📁 docs/
    ├── API_REFERENCE.md
    ├── DEVELOPMENT.md
    ├── CONTRIBUTING.md
    └── CHANGELOG.md
```

## File Descriptions

### Frontend Files

#### HTML Files
- **index.html** - Main application with all sections and interactive components
- **settings.html** - User settings, preferences, and data management

#### CSS Files
- **style.css** - Main stylesheet with component styles
- **animations.css** - Keyframe animations and transitions
- **responsive.css** - Mobile-first responsive design

#### JavaScript Files
- **app.js** - Core application logic, subject data, event handlers
- **storage.js** - Local storage management and data persistence
- **three-scene.js** - Three.js 3D scene initialization
- **analytics.js** - User analytics and tracking
- **utils.js** - Utility functions and helpers

### Backend Files

#### Python
- **backend.py** - Flask API server with all endpoints
- **database.py** - Database models and queries
- **analytics.py** - Analytics calculations and insights
- **auth.py** - Authentication and authorization (planned)
- **config.py** - Configuration management

### Data Files

#### JSON Data
- **subjects.json** - Subject definitions
- **papers.json** - Research papers metadata
- **resources.json** - Learning resources

### Documentation

- **README.md** - Project overview and quick start
- **USER_MANUAL.md** - Comprehensive user guide
- **BACKEND_README.md** - Backend API documentation
- **API_REFERENCE.md** - Detailed API endpoints (coming)
- **DEVELOPMENT.md** - Developer setup guide (coming)
- **CONTRIBUTING.md** - Contribution guidelines (coming)

## Getting Started with Project Structure

### For Beginners
1. Start with `README.md` for overview
2. Open `index.html` in browser
3. Read `USER_MANUAL.md` for usage

### For Developers
1. Review project structure (this file)
2. Read `DEVELOPMENT.md` for setup
3. Check `BACKEND_README.md` for API details
4. Start with `js/app.js` for frontend logic

### For Contributions
1. Read `CONTRIBUTING.md`
2. Check open issues
3. Create feature branch
4. Test changes
5. Submit pull request

## Key Components

### Frontend Architecture
- **Entry Point**: `index.html`
- **Core Logic**: `js/app.js`
- **Storage Layer**: `js/storage.js`
- **Visualization**: `js/three-scene.js`
- **Styling**: `css/style.css`

### Backend Architecture
- **API Server**: `python/backend.py`
- **Database**: `python/database.py`
- **Analytics**: `python/analytics.py`
- **Config**: `python/config.py`

## Data Flow

```
User Browser
    ↓
    ├→ index.html (UI)
    ├→ js/app.js (Logic)
    ├→ js/storage.js (Local Storage)
    ├→ js/three-scene.js (3D)
    ├→ css/style.css (Styling)
    └→ python/backend.py (API) → Database
```

## Development Workflow

1. **Frontend Changes**: Modify `js/` and `css/` files
2. **Data Changes**: Update `assets/data/` JSON files
3. **Backend Changes**: Modify `python/` files
4. **Testing**: Run tests in `tests/` directory
5. **Documentation**: Update relevant markdown files

## File Size Reference

- **index.html**: ~15 KB
- **settings.html**: ~8 KB
- **js/app.js**: ~12 KB
- **js/storage.js**: ~5 KB
- **js/three-scene.js**: ~4 KB
- **css/style.css**: ~18 KB
- **css/animations.css**: ~3 KB
- **python/backend.py**: ~10 KB

## Total: ~75 KB (Frontend)

## Adding New Files

When adding new files:
1. Follow naming conventions (kebab-case for files)
2. Place in appropriate directory
3. Update this structure document
4. Document in README or relevant guide
5. Add to `requirements.txt` if Python package

## Best Practices

- Keep files modular and focused
- Use meaningful names
- Document complex logic
- Follow style guides
- Test before committing
- Update documentation

---

**Last Updated**: June 2024
