# BuildMate AI 🏗️🚜

> **Tagline:** "Smart Equipment Decisions. Powered by AI."

BuildMate AI is an AI-powered assistant for construction and farming equipment users. The application helps users describe job requirements in natural language or upload site images, extracts intent and entities, recommends suitable heavy machinery, generates standardized booking requests, and provides factual equipment comparisons.

Developed for the **Snapdragon AI Lab Build & Present Challenge**.

---

## 🌟 Key Features

1. **AI Equipment Assistant**:
   - Natural language input parsing (e.g., *"I need a machine for foundation excavation for 2 days"*, *"Need tractor for ploughing 5 acres"*).
   - Extracts Task, Equipment, Category, Duration, Area/Quantity, and Location.
   - Generates instant structured recommendation cards.

2. **Equipment Knowledge Base & Catalog**:
   - Local structured database storing 22+ machines across **Construction**, **Agriculture**, **Material Handling**, and **Site Utilities**.
   - Details name, category, subcategory, description, typical uses, suitable tasks, rental units, power specs, and explicitly disclaimed **DEMO / EXAMPLE DATA** pricing.

3. **Site Image Analysis**:
   - Drag-and-drop site photo uploader (JPG, JPEG, PNG) with client-side preview.
   - Modular vision analysis service displaying a clear **Demo Analysis** or **AI Vision Analysis** badge.
   - Identifies detected activity, recommended equipment, engineering reasoning, and required site information.

4. **Booking Request Generator**:
   - Converts recommendations into a standardized booking summary format.
   - Interactive modal supporting **[Copy Request]**, **[Download Request]**, and **[Start New Request]**.

5. **Smart Equipment Comparison**:
   - Side-by-side factual matrix comparing any two machines (e.g. Excavator vs JCB, Tractor vs Harvester).
   - Evaluates mobility, work capacity, typical applications, and rental units without biased claims.

6. **Snapdragon Edge AI & Technical Architecture**:
   - Modular `AIProvider` base class supporting zero-dependency local demo rule engines, local open-source LLMs, and a Qualcomm AI Hub target NPU interface placeholder.
   - Edge AI privacy architecture designed for low-latency offline execution on Snapdragon-powered HP PCs.

---

## 🏗️ Project Architecture

```
buildmate-ai/
├── backend/
│   ├── app/
│   │   ├── main.py                     # FastAPI entrypoint & router registrations
│   │   ├── api/
│   │   │   ├── assistant.py            # Chat & query recommendation API
│   │   │   ├── vision.py               # Site image analysis API
│   │   │   ├── equipment.py            # Catalog search, filter, & compare API
│   │   │   └── booking.py              # Booking request generator API
│   │   ├── services/
│   │   │   ├── ai_orchestrator.py      # Modular AI provider manager
│   │   │   └── vision_service.py       # Modular image analysis service
│   │   ├── models/
│   │   │   └── schemas.py              # Pydantic data schemas
│   │   └── database/
│   │       └── db_loader.py            # Equipment repository & JSON loader
│   └── requirements.txt
├── frontend/
│   ├── index.html                      # Industrial dark-theme SPA shell
│   ├── css/
│   │   └── styles.css                  # Custom styling & scrollbar design
│   └── js/
│       └── app.js                      # UI routing, chat engine, & modal handlers
├── data/
│   └── equipment.json                  # 22+ Machine Knowledge Base
├── docs/
│   ├── ARCHITECTURE.md                 # Snapdragon target & Edge AI design doc
│   └── DEMO_GUIDE.md                   # Presentation walkthrough guide
├── README.md
├── .env.example
├── .gitignore
└── LICENSE
```

---

## ⚡ Snapdragon Target Deployment & Competition Notice

> **IMPORTANT COMPETITION STATEMENT**:
> - **Current Development**: Prototyped and tested locally on non-Snapdragon Windows host hardware.
> - **Hardware Testing**: Snapdragon hardware-specific optimization and NPU benchmark numbers are **planned target deployment work** and have NOT been falsely claimed as completed.
> - **Qualcomm Integration**: The application features a clean, modular `QualcommAIProvider` integration interface designed for future deployment via Qualcomm AI Hub and ONNX Runtime QNN on Snapdragon-powered HP PCs.

---

## 🚀 How to Run the Application

### 1. Requirements
- Python 3.10+ installed.

### 2. Launch the Application Server
Run the FastAPI application from the project root directory:

```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Open in Browser
Navigate to:
```
http://localhost:8000/
```

- Live interactive UI served directly at `http://localhost:8000/`
- API documentation available at `http://localhost:8000/docs`

---

## 💡 Quick Demo Examples

1. **Foundation Excavation**:
   - Query: `"I need a machine for foundation excavation for 2 days."`
   - Output: Task: *Foundation excavation*, Equipment: *Excavator / JCB*, Duration: *2 days*.

2. **Agriculture Tillage**:
   - Query: `"Need tractor for ploughing 5 acres."`
   - Output: Task: *Ploughing*, Equipment: *Tractor*, Area: *5 acres*.

3. **Structural Steel Lifting**:
   - Query: `"Need crane for lifting steel beams."`
   - Output: Task: *Lifting steel beams*, Equipment: *Hydraulic Mobile Crane*.

---

## 📄 License
Distributed under the MIT License.
