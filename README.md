# Vision Language Search

Multimodal search combining vision and language

## Features

- Api
Cli
Encoders - Image
Encoders - Text
Index
Ranker
Search Engine

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/vision-language-search.git
cd vision-language-search
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
vision-language-search/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
