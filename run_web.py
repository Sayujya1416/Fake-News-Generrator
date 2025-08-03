#!/usr/bin/env python3
"""
Fake News Generator and Detector Web Application Startup Script
Run this file to start the web server.
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def install_requirements():
    """Install required packages."""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error installing packages")
        return False

def main():
    """Main startup function."""
    print("🤖 Fake News Generator and Detector Web App")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if Flask is installed
    try:
        import flask
        print("✅ Flask is already installed")
    except ImportError:
        print("📦 Flask not found, installing requirements...")
        if not install_requirements():
            sys.exit(1)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found")
        print("Please ensure you're in the correct directory")
        sys.exit(1)
    
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found")
        print("Please ensure you're in the correct directory")
        sys.exit(1)
    
    print("🚀 Starting web server...")
    print("🌐 The application will be available at: http://localhost:5000")
    print("📱 Open your web browser and navigate to the URL above")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Import and run the Flask app
        from app import app
        app.run(host="0.0.0.0", port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 