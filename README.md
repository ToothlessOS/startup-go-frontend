# startup-go-frontend

Frontend for team "Startup Go" @ HackDKU25

## Overview

This is the frontend web application for comatch.ai, a platform for AI-powered cofounder matching. It is built with Flask (Python) for server-side rendering and uses HTML, Tailwind CSS, and JavaScript for the UI. The frontend communicates with a backend API (see [startup-go-backend](https://github.com/ToothlessOS/startup-go-backend)) for authentication, user profiles, chat, and project management.

## Features

- **Authentication**: User registration, login, logout (JWT-based, via backend API)
- **Profile Management**: Edit personal info, avatar upload, skills multi-select, social links, etc.
- **Discover**: Browse and filter potential cofounders and projects
- **Chat**: View chat list, search/filter chats, one-on-one chat pages

## Project Structure

```
├── app.py                # Flask app entry point and routes
├── models.py             # (Optional) SQLAlchemy models for local use
├── requirements.txt      # Python dependencies
├── templates/            # Jinja2 HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── profile.html
│   ├── discover.html
│   ├── chat.html
│   ├── michaelChen.html
│   └── ...
├── static/
│   ├── styles/
│   │   ├── main.css
│   │   ├── login.css
│   │   └── signup.css
│   └── scripts/
│       └── login.js
└── README.md
```

## How to Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend API**  
   Make sure the backend (see [startup-go-backend](https://github.com/ToothlessOS/startup-go-backend)) is running at `http://127.0.0.1:8000`.

3. **Run the frontend Flask app**  
   ```bash
   python app.py
   ```

4. **Open in browser**  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## API Integration

All user authentication, profile, and chat data are fetched from and sent to the backend API.  
See the backend's `README.md` for detailed API endpoints and data formats.

## Notable UI Features

- **Device Frame**: All pages are rendered inside a mobile device-like frame for a consistent mobile UX.
- **Profile Page**: Includes avatar upload, editable fields, multi-select skills, and social links.
- **Chat Page**: Chat list with search, horizontal avatar bar, and one-on-one chat simulation.
- **Discover Page**: Card-based user/project discovery with modal details.

## Development Notes

- The frontend expects the backend API to be available at `http://127.0.0.1:8000`.
- JWT tokens are stored in Flask session and sent as `Authorization: Bearer ...` headers.
- Avatar upload uses multipart/form-data and updates the preview immediately.
- All UI is responsive and optimized for mobile display.
