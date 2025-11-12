# PS script to create a one-folder Windows build using PyInstaller

python -m pip install --upgrade pyinstaller
pyinstaller --noconfirm --onedir --windowed -n ai-desktop-solver src\\main.py

Write-Host "Build finished. See dist\\ai-desktop-solver"