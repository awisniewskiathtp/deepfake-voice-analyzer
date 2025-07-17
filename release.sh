#!/bin/sh
# release.sh – by warp3r(2025)

# ✅ Sprawdź, czy podano numer wersji
if [ -z "$1" ]; then
  echo "❗ Usage: ./release.sh vX.Y.Z"
  exit 1
fi

VERSION=$1

# 🔍 Upewnij się, że plik CHANGELOG istnieje
if [ ! -f CHANGELOG.md ]; then
  echo "❌ CHANGELOG.md not found."
  exit 1
fi

# 📝 Wyodrębnij opis bieżącej wersji
echo "📄 Extracting changelog for $VERSION..."
CHANGELOG=$(awk "/^## \\[$VERSION\\]/,/^## \\[/" CHANGELOG.md | sed '$d')

# ❓ Jeśli changelog pusty, zapytaj
if [ -z "$CHANGELOG" ]; then
  echo "⚠️ No changelog found for $VERSION. Continue? (y/n)"
  read CONFIRM
  [ "$CONFIRM" != "y" ] && exit 1
fi

# 🏷️ Dodaj tag
echo "🏷️ Tagging release: $VERSION"
git tag -a "$VERSION" -m "$VERSION release"

# ⏫ Wypchnij tag
echo "🚀 Pushing tag to remote..."
git push origin "$VERSION"

# ✅ Potwierdzenie
echo "✅ Release $VERSION tagged and pushed."

# 🖨️ Pokaż changelog
if [ -n "$CHANGELOG" ]; then
  echo "\n📦 CHANGELOG for $VERSION:"
  echo "$CHANGELOG"
fi
#EoF
