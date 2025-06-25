Elemental24 Frontend

Elemental24 is a modern, interactive web application designed for chemistry enthusiasts to explore, create, and manage elements in a dynamic periodic table. Built with React, TypeScript, and styled exclusively with Tailwind CSS, this frontend delivers a visually engaging, green-themed experience with an atomic-inspired design. It integrates with a Django REST Framework backend (not included) to handle user authentication and element management via API endpoints.
Features

Interactive Periodic Table: Display all registered elements on the landing page in a responsive grid layout mimicking the periodic table, with clickable cells revealing detailed modals.
User Authentication: Secure registration, login, and logout functionality with intuitive forms.
Element Registration: Form for users to submit new elements, including name, symbol, and description.
User Dashboard: Personalized view of user-submitted elements in a clean, card-based grid.
Green Atomic Theme: Vibrant green accents (emerald, lime) on a dark base, with dynamic gradients, bold hover effects, and a subtle animated atomic particle background.
Responsive Design: Mobile-first approach using Tailwind’s responsive utilities, ensuring seamless usability across devices.
Performance Optimized: Leverages Tailwind’s JIT mode, React’s useMemo/useCallback, and purged unused styles for fast load times.

Tech Stack

Framework: React (with TypeScript)
Styling: Tailwind CSS
State Management: React Context or Redux Toolkit (configurable)
API Integration: Axios/Fetch for Django REST Framework endpoints
Animations: CSS-based atomic particle background
Fonts: Poppins (via Google Fonts)
Build Tool: Vite or Create React App

Project Structure
elemental24-frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── assets/
│   │   └── styles.css
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── PeriodicTable.tsx
│   │   ├── ElementModal.tsx
│   │   ├── AuthForm.tsx
│   │   ├── ElementForm.tsx
│   │   ├── ElementCard.tsx
│   │   └── Footer.tsx
│   ├── contexts/
│   │   └── AuthContext.tsx
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Register.tsx
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   └── ElementSubmission.tsx
│   ├── services/
│   │   └── api.ts
│   ├── App.tsx
│   ├── main.tsx
│   └── types.ts
├── tailwind.config.js
├── tsconfig.json
├── package.json
└── README.md

Getting Started
Prerequisites

Node.js (v18 or higher)
npm or yarn
Django REST Framework Backend (running locally or deployed, with endpoints like /api/register/, /api/login/, /api/elements/)

Installation

Clone the Repository
git clone https://github.com/your-username/elemental24-frontend.git
cd elemental24-frontend


Install Dependencies
npm install

Or with yarn:
yarn install


Configure Environment
Create a .env file in the root directory and add the backend API URL:
VITE_API_URL=http://localhost:8000/api/


Run the Development Server
npm run dev

Or with yarn:
yarn dev

Open http://localhost:5173 in your browser to view the app.

Build for Production
npm run build

The optimized build will be output to the dist/ folder.


Usage

Landing Page: Explore the periodic table, where each element cell displays the symbol and name. Click a cell to open a modal with detailed information.
Register/Login: Navigate to the registration or login pages to create an account or sign in. Forms validate inputs and display loading states or errors.
Element Submission: Authenticated users can access the element submission form to add new elements, which are sent to the backend.
Dashboard: View your submitted elements in a grid of cards, each showing the name, symbol, description, and creation date.
Atomic Background: Enjoy a subtle, performance-optimized particle animation mimicking atomic orbits across the landing page.

API Integration
The frontend interacts with the following Django REST Framework endpoints:

POST /api/register/: Register a new user (username, email, password).
POST /api/login/: Authenticate a user and return a token.
POST /api/elements/: Submit a new element (name, symbol, description).
GET /api/elements/: Retrieve all registered elements for the periodic table.
GET /api/elements/user/: Fetch user-specific elements for the dashboard.

API requests are handled with Axios, including token-based authentication and error handling with user-friendly feedback.
Design Highlights

Color Palette: Dark base (bg-gray-900) with vibrant green accents (bg-green-600, bg-emerald-500, bg-lime-500) and secondary text highlights (text-green-400).
Typography: Poppins font with clear hierarchy (text-5xl font-extrabold for headers, text-xl for body, text-base for secondary text).
Animations: Bold hover effects (hover:scale-110, hover:shadow-2xl) and a lightweight CSS-based atomic particle background (text-green-500 opacity-20).
Responsiveness: Periodic table adjusts to grid-cols-9 on mobile and grid-cols-18 on desktop, with scrollable overflow for smaller screens.
Accessibility: ARIA labels, keyboard navigation, and high-contrast text ensure inclusivity.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request with a detailed description.

Please follow the coding standards (Prettier, ESLint) and ensure tests pass.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, reach out to:

Email: support@elemental24.com
GitHub Issues: Open an issue


Explore the Elemental24 Periodic Table and unleash your inner chemist!