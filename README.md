# RegretNet

An AI-powered system designed to help users analyze and navigate their regrets through multi-agent conversations. RegretNet uses specialized AI agents to provide diverse perspectives on regrettable decisions and situations.

## Overview

RegretNet leverages multiple AI agents to simulate different viewpoints on regret scenarios:
- **Emotion Agent**: Explores the emotional aspects of the regret
- **Future Self Agent**: Provides perspective from how this will feel in the future
- **Growth Agent**: Focuses on learning and personal development opportunities
- **Outcome Agent**: Analyzes potential outcomes and consequences
- **Risk Agent**: Evaluates risks and uncertainties

## Project Structure

```
regretnet/
├── backend/                 # Python FastAPI backend
│   ├── agents/             # Multi-agent implementation
│   │   ├── emotion_agent.py
│   │   ├── future_self_agent.py
│   │   ├── growth_agent.py
│   │   ├── outcome_agent.py
│   │   └── risk_agent.py
│   ├── api/                # API endpoints
│   │   └── simulate.py
│   ├── services/           # Business logic & utilities
│   │   ├── orchestrator.py
│   │   ├── openrouter_client.py
│   │   ├── parser.py
│   │   ├── logger.py
│   │   └── retry.py
│   ├── models/             # Data schemas
│   │   └── schemas.py
│   ├── config.py           # Configuration
│   ├── main.py             # Application entry point
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Docker configuration
│
└── frontend/               # Next.js frontend
    ├── app/
    │   ├── page.tsx        # Main page
    │   ├── layout.tsx      # Layout component
    │   ├── globals.css     # Global styles
    │   └── simulate/       # Simulation API route
    ├── public/             # Static assets
    ├── package.json        # Node dependencies
    ├── next.config.ts      # Next.js configuration
    └── tsconfig.json       # TypeScript configuration
```

## Tech Stack

**Backend:**
- Python 3.x
- FastAPI
- OpenRouter API (LLM integration)
- Uvicorn (ASGI server)

**Frontend:**
- Next.js
- TypeScript
- React
- PostCSS

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the `backend/` directory with required API keys and settings.

5. Run the backend server:
```bash
uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `POST /api/simulate` - Main endpoint for regret analysis simulation
  - Takes user input describing a regrettable situation
  - Returns multi-agent analysis from all specialized agents

## Features

- **Multi-agent Analysis**: Get perspectives from 5 different AI agents on your regret
- **Emotional Intelligence**: Understand the emotional dimensions of your situation
- **Future Perspective**: See how today's regret might feel at different time horizons
- **Growth Opportunities**: Identify learning and development potential
- **Risk Assessment**: Evaluate uncertainties and potential consequences
- **Clean UI**: User-friendly interface for exploring regret scenarios

## Docker Support

To run the application in Docker:

```bash
cd backend
docker build -t regretnet-backend .
docker run -p 8000:8000 regretnet-backend
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Created**: January 2026
**Repository**: https://github.com/lukekoshy/RegretNet.git
