# Contributing to Voice Analyzer

Thank you for considering contributing to **Voice Analyzer**! We welcome contributions of all kinds:

* 🔐 Bug reports
* 🌍 New translations
* 🚀 Feature suggestions or code improvements
* 📄 Documentation updates

---

## ✍️ How to Contribute

1. **Fork the repository**
2. **Create a feature branch**:

   ```bash
   git checkout -b feature/my-improvement
   ```
3. **Make your changes**
4. **Test the script** with your language and a sample audio file
5. **Commit** and push your branch:

   ```bash
   git commit -m "Add MFCC histogram feature"
   git push origin feature/my-improvement
   ```
6. **Create a Pull Request (PR)** and describe your changes

---

## 🌐 Translating Voice Analyzer

We use `gettext` and `.po` files located in `locale/`. To add a new language:

1. Copy `locale/en/` as a template:

   ```bash
   cp -r locale/en locale/de  # For German
   ```
2. Edit `messages.po` with a translation tool (e.g., Poedit)
3. Compile with:

   ```bash
   msgfmt messages.po -o messages.mo
   ```

Please test your translation using:

```bash
python3 voice_analyzer.py ... <your_language_code>
```

---

## ✉️ Contact

If you're unsure how to contribute, feel free to open an issue or email:

* Andrzej Wiśniewski[a.wisniewski@yourwebdesign.be]

Thanks again! 🙏

