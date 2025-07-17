# Voice Analyzer

**Voice Analyzer** is an open-source tool for analyzing audio recordings, with a special focus on characteristics that may indicate speech synthesis or deepfake content. It generates detailed PDF reports including MFCC visualizations and heuristic evaluations.

---

## 🔧 Features

* Extraction of acoustic features (MFCC, ZCR, energy)
* MFCC visualization as a chart
* PDF report generation including:

  * Case identifier
  * Analyst details
  * Heuristic evaluation of synthetic traits
  * MFCC plot
* Multilingual support (PL/EN) using `gettext`

---

## 🚀 Installation

### Requirements:

```bash
Python 3.8+
pip install -r requirements.txt
sudo apt install ffmpeg libmagic1 gettext
```

---

## ⚙️ Usage

```bash
python3 voice_analyzer.py <audio_file> <CASE_ID> <ANALYST_NAME> <EMAIL> <LANG_CODE>
```

### Example:

```bash
python3 voice_analyzer.py recording.wav CASE-2025 "Helmut Kaczynski" "helmut.kaczynski@nowogrodzka.site" en
```

Output: `report.pdf` + `mfcc_plot.png`

---

## 🌍 Language Support

The `gettext` system uses the `locale/` directory structure:

```
locale/
├── pl/
│   └── LC_MESSAGES/
│       └── messages.po
└── en/
    └── LC_MESSAGES/
        └── messages.po
```

Compile translation:

```bash
msgfmt messages.po -o messages.mo
```

---

## 📄 Project Files

* `voice_analyzer.py` — main analysis script
* `locale/` — translation files
* `report.pdf` — generated analysis report
* `mfcc_plot.png` — MFCC image from the recording

---

## 👁️ License

This project is licensed under the **MIT License**.

---

## 🙌 Contributing

We welcome all contributions! Translate, report bugs, or open pull requests.
See `CONTRIBUTING.md` for details.

---

## 🌐 Authors

* Andrzej Wiśniewski
  [a.wisniewski@yourwebdesign.be]

* ChatGPT (technical assistant)
  OpenAI

