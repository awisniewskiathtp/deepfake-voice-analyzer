#!/bin/sh
# commit.sh — by warp3r(2025)

if [ -z "$1" ]; then
  echo "❗ Usage: ./commit.sh \"commit message\""
  exit 1
fi

# 🧹 Cleanup
echo "🧹 Removing __pycache__..."
find . -name "__pycache__" -type d -exec rm -rf {} +

# 🔐 Permissions (only for script)
chmod +x commit.sh

# 📌 Git actions
echo "📌 Adding files..."
git add .

echo "🛠️  Committing changes..."
git commit -m "m: $1"

echo "⏳ Pushing to main..."
git push -u origin main

echo "✅ Done."
#EoF
