# multi-agent-cv-review
Multi-agent workforce that analyzes CVs, evaluates candidates, and generates hiring recommendations.

## Setup

### 1. Install Dependencies

```bash
pip install navaia-forge
```

### 2. Create a `.env` File

Create a file named `.env` in the project root directory:

```text
multi-agent-cv-review/
├── main.py
├── README.md
├── .env
```

Add your Navaia Forge API key to the file:

```env
NAVAIA_API_KEY=your_api_key_here
```

You can generate an API key from:

```text
Settings → API Keys
https://fareegi.navaia.sa/settings/api-keys
```

### 3. Run the Project

```bash
python main.py
```

### Example `.env`

```env
NAVAIA_API_KEY=nf_xxxxxxxxxxxxxxxxx
```
