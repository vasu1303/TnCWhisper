# 🌟 TnCWhisper

<div align="center">

**AI-Powered Terms & Conditions Analyzer Browser Extension**

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

</div>

---

## 📖 Overview

**TnCWhisper** is an intelligent browser extension that automatically scrapes, analyzes, and summarizes lengthy Terms & Conditions documents using advanced AI technology. Say goodbye to reading pages of legal jargon—get instant, concise bullet-point summaries with a single click!

### ✨ Key Features

- 🤖 **AI-Powered Summarization** - Leverages Facebook's BART-large-CNN model for accurate text summarization
- 🔍 **Intelligent Web Scraping** - Automatically detects and extracts T&C content from any website
- ⚡ **Instant Analysis** - Get comprehensive summaries in seconds
- 🎨 **Beautiful UI** - Modern, responsive design with Tailwind CSS and Shadcn/UI
- 💾 **Smart Caching** - MongoDB integration for storing and retrieving previously analyzed documents
- 🔐 **Privacy-Focused** - All processing happens on your backend—no third-party data sharing

---

## 🏗️ Project Structure

```
TnCWhisper/
├── frontend/                    # Chrome Extension (React + TypeScript)
│   ├── src/
│   │   ├── popup/
│   │   │   ├── Popup.tsx       # Main popup UI component
│   │   │   └── popup.html      # Popup HTML template
│   │   ├── scripts/
│   │   │   ├── background.ts   # Background service worker
│   │   │   └── contentScript.ts # Content script for tab interaction
│   │   ├── styles/
│   │   │   └── tailwind.css    # Tailwind styling
│   │   └── manifest.json       # Chrome extension manifest
│   ├── package.json
│   ├── webpack.config.js        # Webpack bundler configuration
│   └── tsconfig.json
│
└── backend/                     # FastAPI Server (Python)
    ├── main.py                  # FastAPI application entry point
    ├── db.py                    # MongoDB connection and configuration
    ├── summarize.py             # BART model summarization logic
    ├── chunking.py              # Text chunking utilities
    ├── requirements.txt         # Python dependencies
    └── scraping/
        ├── webScraping.py       # Main scraping orchestrator
        ├── data/                # Scraped data storage
        └── helpingPrograms/
            ├── extractAllLink.py           # Link extraction
            ├── extractTncLink.py           # T&C link identification
            ├── termsAndConditionExtractor.py # Content extraction
            ├── companyName.py              # Domain name extraction
            ├── saveAsFile.py               # File saving utilities
            └── similarTncPhases.py         # T&C keyword patterns
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **MongoDB** (Atlas or local instance)
- **Chrome Browser**

---

### 🔧 Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB:**
   - Update the MongoDB connection string in `db.py` with your credentials:
   ```python
   client = MongoClient("your-mongodb-connection-string")
   ```

5. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`

---

### 🎨 Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Build the extension:**
   ```bash
   npm run build
   ```
   
   This will generate the `dist/` folder with the compiled extension.

4. **Load the extension in Chrome:**
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable **Developer mode** (top-right toggle)
   - Click **Load unpacked**
   - Select the `frontend/dist/` folder

---

## 📚 How It Works

### 🔄 Architecture Flow

```
┌─────────────────┐
│  User clicks    │
│  Extension Icon │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Popup UI (React)       │
│  - Gets current tab URL │
│  - Sends to Backend API │
└────────┬────────────────┘
         │
         ▼
┌───────────────────────────┐
│  FastAPI Backend          │
│  1. Check MongoDB cache   │
│  2. If not found, scrape  │
│  3. Summarize with BART   │
│  4. Store in MongoDB      │
│  5. Return summary        │
└────────┬──────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Display bullet-point   │
│  summary in popup       │
└─────────────────────────┘
```

### 🧠 AI Summarization Process

1. **Text Cleaning** - Removes excessive whitespace and formatting
2. **Smart Chunking** - Splits text into token-optimized chunks (max 1024 tokens)
3. **BART Summarization** - Each chunk is summarized using `facebook/bart-large-cnn`
4. **Post-Processing** - Converts summaries into bullet points for readability

---

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling
- **Shadcn/UI** - Component library
- **Lucide React** - Icon library
- **Webpack 5** - Module bundler

### Backend
- **FastAPI** - Modern Python web framework
- **PyMongo** - MongoDB driver
- **Transformers (HuggingFace)** - BART model for summarization
- **PyTorch** - Deep learning framework
- **BeautifulSoup4** - HTML parsing
- **Requests** - HTTP library

---

## 🔌 API Endpoints

### `POST /analyze`

Analyzes a URL and returns a summarized version of its Terms & Conditions.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "received_url": "https://example.com",
  "summary": "- Key point 1\n- Key point 2\n- Key point 3"
}
```

---

## 🎯 Key Features Breakdown

### 🔍 Intelligent Link Detection
The scraper uses an extensive list of T&C-related keywords to identify the correct links:
- `terms`, `privacy`, `agreement`, `termsofservice`, etc.
- Over 100+ variations and patterns

### 💾 MongoDB Caching
- Stores analyzed summaries by domain
- Prevents redundant processing
- Fast retrieval for previously analyzed sites

### 🧩 Smart Text Chunking
- Respects sentence boundaries
- Token-aware splitting (BART's 1024 token limit)
- Maintains context across chunks

### 🎨 Modern UI Design
- Gradient backgrounds
- Loading states with animations
- Responsive design
- Cookie analysis feature (expandable)

---

## 🔐 Environment Variables

Create a `.env` file in the backend directory:

```env
MONGODB_URI=your_mongodb_connection_string
MODEL_NAME=facebook/bart-large-cnn
MAX_TOKENS=1024
```

---

## 🧪 Development

### Running in Development Mode

**Backend:**
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build:css  # Build Tailwind CSS
npm run build      # Build extension
```

### Build for Production

**Frontend:**
```bash
npm run build
```

The production-ready extension will be in `frontend/dist/`

---

## 🐛 Troubleshooting

### Common Issues

**1. MongoDB Connection Failed**
- Verify your connection string in `db.py`
- Check network access in MongoDB Atlas

**2. Model Download Issues**
- Ensure sufficient disk space (BART model is ~1.6GB)
- Check internet connection during first run

**3. Extension Not Loading**
- Ensure `manifest.json` is copied to `dist/`
- Check webpack build logs for errors
- Verify all permissions in manifest

**4. CORS Issues**
- Backend CORS is configured for `*` (all origins)
- For production, specify your extension ID

---

## 📈 Future Enhancements

- [ ] Support for multiple languages
- [ ] Sentiment analysis of T&C content
- [ ] Risk scoring system
- [ ] Comparison between different versions
- [ ] PDF support
- [ ] Export summaries to PDF/Markdown
- [ ] User annotations and highlights

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Vasu Singh**
- GitHub: [@vasu1303](https://github.com/vasu1303)

---

## 🙏 Acknowledgments

- [Facebook AI's BART Model](https://huggingface.co/facebook/bart-large-cnn)
- [Tailwind CSS](https://tailwindcss.com/)
- [Shadcn/UI](https://ui.shadcn.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Vasu Singh

</div>
