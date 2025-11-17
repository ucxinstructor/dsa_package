#!/usr/bin/env bash
set -e

# --- SETTINGS ---
BUILD_DIR="docs/build/html"
BRANCH="gh-pages"
TMP_DIR=".gh-pages-tmp"

# --- CHECK BUILD DIR EXISTS ---
if [ ! -d "$BUILD_DIR" ]; then
    echo "❌ Build directory $BUILD_DIR does not exist. Run 'make html' first."
    exit 1
fi

# --- CLEAN TMP DIR ---
rm -rf "$TMP_DIR"
mkdir "$TMP_DIR"

# --- COPY BUILT HTML INTO TMP DIR ---
cp -r $BUILD_DIR/* "$TMP_DIR"/

# --- SWITCH TO GH-PAGES ---
git fetch
git checkout "$BRANCH"

# --- REMOVE OLD FILES IN GH-PAGES (SAFE: ONLY INSIDE THE BRANCH) ---
git rm -rf . >/dev/null 2>&1 || true

# --- COPY NEW FILES INTO GH-PAGES ROOT ---
cp -r "$TMP_DIR"/* .

# --- COMMIT & PUSH ---
git add .
git commit -m "Update documentation"
git push origin "$BRANCH"

# --- SWITCH BACK TO MAIN ---
git checkout -

# --- CLEAN TMP DIR ---
rm -rf "$TMP_DIR"

echo "✅ Documentation deployed to GitHub Pages."
