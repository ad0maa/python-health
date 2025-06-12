# Health & Fitness Tracking App - Backend

A comprehensive health and fitness tracking application built with FastAPI that integrates nutrition tracking, macro management, recipe suggestions, and fitness data from multiple sources.

## 🎯 Project Goals

- Track food intake and calculate macronutrients (protein, carbs, fats, calories)
- Provide goal-based recipe suggestions based on user health objectives
- Integrate with fitness platforms (Apple Health, Strava, Fitbit)
- Generate smart meal plans that hit macro targets
- Provide analytics and progress tracking
- Support multiple client applications (web frontend, React Native mobile app)

## 🏗️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens
- **Background Tasks**: Celery with Redis
- **Caching**: Redis
- **Testing**: pytest
- **Documentation**: Automatic OpenAPI/Swagger

## 📋 Development Phases

### Phase 1: Complete Backend Implementation 🚧
- [x] Create project plan and CLAUDE.md context
- [x] FastAPI project structure with proper dependencies
- [x] Database models (Users, Foods, Meals, Recipes, Activities)
- [x] JWT authentication system setup
- [ ] **Complete all API endpoint implementations**
  - [x] Authentication endpoints (register, login, refresh)
  - [x] User management endpoints (profile, goals, preferences)
  - [ ] Nutrition endpoints (food search, meal logging, daily summary)
  - [ ] Recipe endpoints (search, create, suggestions)
  - [ ] Activity endpoints (sync, history, analytics)
- [ ] **Unit conversion utilities**
  - [ ] Calories ↔ Kilojoules converter
  - [ ] Pounds ↔ Kilograms converter
  - [ ] Imperial ↔ Metric measurements
  - [ ] Serving size standardization
- [ ] **External API integrations**
  - [ ] USDA FoodData Central API integration
  - [ ] Edamam Nutrition API integration
  - [ ] Spoonacular API integration
  - [ ] Strava API integration
  - [ ] Apple Health/Google Fit API research
- [ ] **Backend testing suite**
  - [ ] Unit tests for all endpoints
  - [ ] Integration tests for external APIs
  - [ ] Authentication/authorization tests
  - [ ] Database transaction tests
- [ ] **Macro calculation engine**
  - [ ] TDEE calculation based on user profile
  - [ ] Goal-based macro distribution
  - [ ] Progress tracking algorithms

### Phase 2: Vue.js Web Frontend Development 🎯
- [ ] **Project setup**
  - [ ] Vue 3 + Vite project initialization
  - [ ] Nuxt.js configuration for SSR/SSG
  - [ ] Pinia state management setup
  - [ ] Tailwind CSS or Vue component library
- [ ] **Authentication system**
  - [ ] Login/register forms
  - [ ] JWT token management
  - [ ] Protected routes and navigation guards
  - [ ] User session persistence
- [ ] **Dashboard and macro tracking**
  - [ ] Daily macro progress visualization
  - [ ] Calorie intake vs. target charts
  - [ ] Meal timeline and food diary
  - [ ] Goal setting and progress tracking
- [ ] **Recipe and meal planning**
  - [ ] Recipe browser with search and filters
  - [ ] Meal planning calendar interface
  - [ ] Shopping list generation
  - [ ] Custom recipe creation
- [ ] **Fitness integration**
  - [ ] Activity data visualization
  - [ ] Workout logging interface
  - [ ] Progress charts and analytics
  - [ ] Integration with fitness APIs
- [ ] **Responsive design**
  - [ ] Mobile-first responsive layouts
  - [ ] PWA capabilities for offline usage
  - [ ] Touch-friendly interfaces

### Phase 3: Mobile App Development 📱
**Framework Decision Point** (Evaluate after Phase 2):
- **Vue Options**: Quasar Framework, Ionic Vue, NativeScript-Vue
- **React Native Options**: Expo + React Native (more familiar)

**Core Mobile Features**:
- [ ] Food logging with barcode scanning
- [ ] Camera integration for meal photos
- [ ] Device health data integration (Apple Health/Google Fit)
- [ ] Push notifications for meal reminders
- [ ] Offline sync capabilities
- [ ] Native performance optimizations

### Phase 4: Advanced Features & Intelligence 🚀
- [ ] **AI-powered recommendations**
  - [ ] Meal suggestion algorithm based on preferences
  - [ ] Recipe recommendations for macro targets
  - [ ] Habit analysis and improvement suggestions
- [ ] **Social features**
  - [ ] User challenges and competitions
  - [ ] Shared meal plans and recipes
  - [ ] Progress sharing and motivation
- [ ] **Advanced analytics**
  - [ ] Trend analysis and insights
  - [ ] Predictive modeling for goal achievement
  - [ ] Custom reporting and data export
- [ ] **Wearable integrations**
  - [ ] Garmin Connect API
  - [ ] Fitbit API integration
  - [ ] Apple Watch complications
  - [ ] Real-time heart rate and activity sync

## 🗄️ Database Schema

### Core Models
- **Users**: Profile, goals, dietary restrictions, preferences
- **Foods**: Nutritional information, serving sizes
- **Meals**: User meal logs with timestamp and portions
- **Recipes**: Instructions, ingredients, nutritional info
- **Activities**: Fitness activities from external integrations
- **Goals**: User-defined health/fitness objectives

### Relationships
- Users have many Meals, Recipes, Activities, Goals
- Meals contain many Foods (many-to-many)
- Recipes contain many Foods (many-to-many)
- Activities belong to Users

## 🔌 External Integrations

### Nutrition Data
- USDA FoodData Central API
- Edamam Nutrition API
- Spoonacular API

### Fitness Platforms
- Apple HealthKit
- Strava API
- Fitbit API
- Google Fit API

## 📱 API Endpoints Structure

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/refresh` - Token refresh

### User Management
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile
- `POST /users/goals` - Set health goals

### Nutrition
- `GET /foods/search` - Search food database
- `POST /meals` - Log a meal
- `GET /meals` - Get meal history
- `GET /nutrition/daily` - Get daily nutrition summary

### Recipes
- `GET /recipes` - Get recipe suggestions
- `POST /recipes` - Create custom recipe
- `GET /recipes/{id}` - Get recipe details

### Fitness
- `GET /activities` - Get activity history
- `POST /integrations/sync` - Sync external data
- `GET /analytics/progress` - Get progress analytics

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables
4. Run database migrations
5. Start the development server: `uvicorn main:app --reload`

## 🧪 Testing Strategy

- Unit tests for business logic
- Integration tests for API endpoints
- Mock external API calls
- Database transaction testing
- Authentication/authorization testing

## 📈 Future Enhancements

- AI-powered meal recommendations
- Social features (sharing meals, challenges)
- Wearable device integrations
- Barcode scanning for food logging
- Machine learning for habit prediction