# Voice Analyzer

**Voice Analyzer** to open-source narzędzie do analizy nagrań audio, ze szczególnym uwzględnieniem cech charakterystycznych dla syntezatorów mowy i potencjalnych deepfake’ów. Narzędzie generuje szczegółowe raporty PDF z wykresem MFCC i oceną heurystyczną.

---

## 🔧 Funkcjonalności

* Ekstrakcja cech akustycznych (MFCC, ZCR, energia)
* Wizualizacja MFCC jako wykres
* Generowanie raportu PDF z:

  * Identyfikatorem sprawy
  * Danymi analityka
  * Heurystyczną oceną potencjalnej syntetyczności
  * Zrzutem MFCC
* Obsługa wielu języków (PL/EN) przez `gettext`

---

## 🚀 Instalacja

### Wymagania:

```bash
Python 3.8+
pip install -r requirements.txt
sudo apt install ffmpeg libmagic1 gettext
```

---

## ⚙️ Użycie

```bash
python3 voice_analyzer.py <plik_audio> <CASE_ID> <ANALYST_NAME> <EMAIL> <LANG_CODE>
```

### Przykład:

```bash
python3 voice_analyzer.py nagranie.wav SPRAWA-2025 "Helmut Kaczynski" "helmut.kaczynski@nowogrodzka.site" pl
```

Wynik: `report.pdf` + `mfcc_plot.png`

---

## 🌍 Obsługa języków

System `gettext` obsługuje katalog `locale/`, np.:

```
locale/
├── pl/
│   └── LC_MESSAGES/
│       └── messages.po
└── en/
    └── LC_MESSAGES/
        └── messages.po
```

Kompilacja:

```bash
msgfmt messages.po -o messages.mo
```

---

## 📝 Pliki

* `voice_analyzer.py` — główny skrypt analizy
* `locale/` — katalogi tłumaczeń
* `report.pdf` — generowany raport z analizy
* `mfcc_plot.png` — obraz MFCC z nagrania

---

## 👁️ Licencja

Projekt jest dostępny na licencji **MIT**.

---

## 🙏 Współudział

Chcesz pomóc? Tłumacz, zgłaszaj problemy lub rozwijaj kod – PR-y mile widziane!

---

## 🌐 Autorzy

* Andrzej Wiśniewski
  [a.wisniewski@yourwebdesign.be]

* ChatGPT (asystent techniczny)
  OpenAI

