# OrdFlöde

**OrdFlöde** is an AI-powered Swedish writing assistant that offers real-time grammar and spell-checking, smart rewrite suggestions, and tone analysis. Built with Angular, Node.js, and Python, OrdFlöde helps you write clearly and confidently. Perfect for both native speakers and learners.

## Key Features

- **Real-Time Grammar and Spell Checking**: Automatically detects and corrects grammatical errors and spelling mistakes.
- **Contextual Rewrite Suggestions**: Highlight text to receive contextually appropriate rewrite suggestions.
- **Tone and Clarity Analysis**: Gain insights into the tone and clarity of your writing and get suggestions for improvement.
- **Proofreading Assistance**: Comprehensive document scanning to catch errors and suggest improvements across your entire text.
- **Interactive UI with Tooltips**: User-friendly interface enriched with tooltips that guide users through the app’s features.

## Tech Stack

- **Frontend**: Angular, TypeScript, Tailwind CSS
- **Backend**: Node.js, Express, TypeScript
- **Database**: PostgreSQL with TypeORM
- **NLP Microservice**: Python, FastAPI, spaCy (via REST API)
- **Authentication**: JWT (JSON Web Tokens)
- **DevOps**: Docker, Heroku/AWS/GCP, GitHub Actions
- **Testing**: Jasmine/Karma, Jest, Cypress

## Getting Started

### Prerequisites

- **Node.js**: Ensure that Node.js and npm are installed on your machine.
- **Python**: Install Python 3 and pip for the NLP microservice.
- **PostgreSQL**: Set up a PostgreSQL database.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ordflode.git
   cd ordflode
   ```

2. **Install Frontend Dependencies**:

   ```bash
   cd frontend/ordflode-frontend
   npm install
   ```

3. **Install Backend Dependencies**:

   ```bash
   cd ../../backend
   npm install
   ```

4. **Install NLP Microservice Dependencies**:
   ```bash
   cd ../nlp-service
   python3 -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scriptsctivate`
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Backend**:

   ```bash
   cd backend
   npm run dev
   ```

2. **Start the Frontend**:

   ```bash
   cd ../frontend/ordflode-frontend
   ng serve
   ```

3. **Start the NLP Microservice**:

   ```bash
   cd ../../nlp-service
   uvicorn main:app --reload
   ```

4. **Open the Application**:
   - Visit `http://localhost:4200` for the frontend.
   - The backend runs on `http://localhost:3000`.
   - The NLP microservice API documentation is available at `http://localhost:5000/docs`.

## Contributing

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
