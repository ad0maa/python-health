# Health & Fitness Tracking App - Development Context

## Project Overview
A comprehensive health and fitness tracking application with macro tracking, recipe suggestions, fitness integrations, and unit conversions. Built with FastAPI backend and Vue.js frontend.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy ORM, PostgreSQL, Alembic migrations
- **Authentication**: JWT tokens with python-jose
- **Background Tasks**: Celery + Redis
- **Frontend**: Vue 3 + Composition API, Nuxt.js, Pinia state management
- **Mobile**: TBD (Vue options vs Expo + React Native)
- **Testing**: pytest, pytest-asyncio

## Development Commands
```bash
# Backend Development
uvicorn main:app --reload                    # Start development server
pytest                                       # Run tests
alembic revision --autogenerate -m "msg"     # Create migration
alembic upgrade head                         # Apply migrations

# Environment Setup
pip install -r requirements.txt             # Install dependencies
```

## Environment Variables (.env)
```
# Database
DATABASE_URL=postgresql://user:pass@localhost/health_db

# JWT
SECRET_KEY=your-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis
REDIS_URL=redis://localhost:6379

# External APIs
SPOONACULAR_API_KEY=your-key
EDAMAM_APP_ID=your-id
EDAMAM_APP_KEY=your-key
USDA_API_KEY=your-key
STRAVA_CLIENT_ID=your-id
STRAVA_CLIENT_SECRET=your-secret
```

## External Integrations
- **Nutrition Data**: USDA FoodData Central, Edamam Nutrition API, Spoonacular API
- **Fitness Platforms**: Strava API, Apple HealthKit, Google Fit API, Garmin Connect

## Database Models
- **Users**: Profile, goals, dietary restrictions, macro targets
- **Foods**: Nutritional information, serving sizes
- **Meals**: User meal logs with timestamp and portions
- **Recipes**: Instructions, ingredients, nutritional info
- **Activities**: Fitness activities from external integrations

## API Structure
- `/api/v1/auth/*` - Authentication endpoints
- `/api/v1/users/*` - User management
- `/api/v1/nutrition/*` - Food and meal tracking
- `/api/v1/recipes/*` - Recipe management
- `/api/v1/activities/*` - Fitness activity tracking

## Development Workflow
1. Work on backend endpoints first (Phase 1)
2. Test with FastAPI's automatic Swagger docs at `/docs`
3. Create comprehensive test suite
4. Move to Vue.js frontend (Phase 2)
5. Decide on mobile framework after web completion (Phase 3)

## Key Features to Implement
- Unit conversions (calories ↔ kJ, lbs ↔ kg, etc.)
- Macro calculation engine based on user goals
- External API integrations for food and fitness data
- Background sync tasks for fitness platforms
- Recipe suggestions based on macro targets

## Git & GitHub Workflow
**Feature Branch Development:**
1. Create a new feature branch for each feature: `git checkout -b feature/feature-name`
2. Work on the feature implementation and tests
3. Run all tests to ensure they pass (`pytest`)
4. Commit changes with descriptive messages
5. Push feature branch to GitHub: `git push -u origin feature/feature-name`
6. Create Pull Request with comprehensive description of changes
7. Wait for PR approval before merging

**Pull Request Guidelines:**
- **Title**: Clear, concise description of the feature/change
- **Description**: Include:
  - Summary of changes made
  - Key features implemented
  - Test coverage added
  - Any breaking changes or considerations
- **Important**: Do NOT include Claude credits or generation notices in commit messages or PR descriptions

## Development Session Rules
**On each new Claude Code session:**
1. Read CLAUDE.md and PROJECT_PLAN.md first
2. Check git status to understand recent work
3. Focus on next unchecked item in Phase 1

**When completing tasks:**
1. Create feature branch for the task
2. Implement the feature/endpoint completely (or use TDD approach)
3. Write comprehensive tests for the feature
4. Run tests to ensure they pass (`pytest`)
5. Test functionality manually (run server, check /docs endpoint)
6. Update PROJECT_PLAN.md to tick the completed checkbox
7. Commit changes and create PR for review
8. Move to next logical task after PR approval

**Session boundaries:**
- Focus on 1-3 related checklist items per session
- Always create PR for completed work before ending
- Use clear commit messages and PR descriptions for context