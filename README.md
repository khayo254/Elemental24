# Elemental24 Web App

## Description

The Elemental Web App is a full-stack web application that allows users to register new elements and view registered elements on a dashboard. The backend is built using Django and Django REST framework, while the frontend is developed with React.

## Features

- Add new elements via a form.
- View registered elements on a dashboard.
- Responsive design for better user experience on various devices.

## Prerequisites

- Python 3.x
- Node.js
- npm or yarn

## Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Elemental24
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the backend server:
   ```bash
   python manage.py runserver
   ```

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd elemental-web-app
   ```

2. Install frontend dependencies:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm start
   ```

## Project Structure

```
Elemental24/
├── element_project/         
│   ├── element_project/     
│   ├── elements/            
│   ├── db.sqlite3           
│   ├── manage.py            
├── elemental-web-app/       
│   ├── public/              
│   ├── src/                 
│   │   ├── components/      
│   │   ├── styles/          
│   │   ├── App.js           
│   │   ├── index.js         
│   ├── package.json         
├── venv/                    
├── requirements.txt         
```

## Usage

- Access the form to add new elements:
  Open your browser and navigate to http://localhost:3000.

- View the dashboard:
  Open your browser and navigate to http://localhost:3000/dashboard.

## API Endpoints

- GET /elements: Retrieve a list of registered elements.
- POST /elements: Add a new element.
- GET /elements/:id: Retrieve a specific element by ID.
- PUT /elements/:id: Update a specific element by ID.
- DELETE /elements/:id: Delete a specific element by ID.

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.
