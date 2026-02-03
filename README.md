# 📄 AI Resume Analyzer — Smart Resume Screening with AI

AI Resume Analyzer is a full‑stack AI‑powered web application that helps users analyze resumes against job descriptions using AI.  
It provides **ATS-style matching**, **skill gap analysis**, and **AI feedback** to improve resumes.

The project is built using **Flask**, **Tailwind CSS**, **Google Gemini**, and **Supabase** and is deployed on **Vercel**.

🌐 Live Demo: 

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🧠 AI‑based Resume Analysis using Google Gemini
- 📊 ATS Score Generation
- 🔍 Skill Match & Missing Skill Detection
- 📝 AI Suggestions to Improve Resume
- 🗂 Resume History Stored per User
- 🔐 Authentication using Supabase (Email + Google)
- 🌙 Premium Dark UI with Tailwind CSS
- ☁️ Deployed on Vercel (Free tier)

---

## 🧠 How the Project Works (High‑Level Flow)

1. User logs in (Email / Google)
2. User uploads a resume PDF
3. Resume text is extracted
4. User provides Job Description
5. Resume + JD are sent to Gemini
6. Gemini returns:
   - ATS Score
   - Matched Skills
   - Missing Skills
   - Suggestions
7. Results are stored in Supabase
8. User can revisit past analyses

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask

**AI**
- Google Gemini API

**Database / Auth / Storage**
- Supabase PostgreSQL
- Supabase Auth
- Supabase Storage (Resume PDFs)

**Frontend**
- HTML + Jinja
- Tailwind CSS

**Deployment**
- Vercel

---

## 🔑 Prerequisites

### 1️⃣ Google Gemini API
- Create API key from Google AI Studio
- Enable Gemini API

### 2️⃣ Supabase Account
- Create project at https://supabase.com
- Get:
  - Project URL
  - Service Role Key

---

## 🗄️ Supabase SQL Schema

Run the following SQL in **Supabase SQL Editor**:

```sql
-- Users table (linked with Supabase Auth)
create table public.users (
  id uuid primary key,
  email text,
  created_at timestamp default now()
);

-- Resume files
create table public.resumes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.users(id),
  filename text,
  storage_path text,
  created_at timestamp default now()
);

-- Resume analysis results
create table public.resume_analysis (
  id uuid primary key default gen_random_uuid(),
  resume_id uuid references public.resumes(id),
  ats_score integer,
  matched_skills text,
  missing_skills text,
  suggestions text,
  created_at timestamp default now()
);
```

---

## ⚙️ Environment Variables

Create a `.env` file in project root:

```env
FLASK_SECRET=supersecretkey

# Gemini
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXX

# Supabase
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOi...
SUPABASE_KEY=eEINCJsjjndnNJN...
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
python run.py
```

---

## ☁️ Deployment (Vercel)

- Push project to GitHub
- Import repository in Vercel
- Add environment variables
- Deploy 🚀

---