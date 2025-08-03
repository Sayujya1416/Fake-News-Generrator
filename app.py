"""
Fake News Generator and Detector Web Application
A Flask-based web interface for the fake news generator and detector.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from main import FakeNewsGenerator, FakeNewsDetector, NewsArticle, DetectionResult
import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "fake_news_detector_secret_key_2024"

# Initialize components
generator = FakeNewsGenerator()
detector = FakeNewsDetector()


@app.route("/")
def index() -> str:
    """Main page with navigation to different features."""
    return render_template("index.html")


@app.route("/generate")
def generate_page() -> str:
    """Page for generating fake news."""
    return render_template("generate.html")


@app.route("/detect")
def detect_page() -> str:
    """Page for detecting fake news."""
    return render_template("detect.html")


@app.route("/api/generate", methods=["POST"])
def api_generate() -> str:
    """API endpoint for generating fake news."""
    try:
        data = request.get_json()
        category = data.get("category", "random")
        
        # Generate fake news
        article = generator.generate_fake_news(category)
        
        # Convert to JSON-serializable format
        result = {
            "title": article.title,
            "content": article.content,
            "author": article.author,
            "source": article.source,
            "publish_date": article.publish_date.strftime("%Y-%m-%d"),
            "category": article.category,
            "is_fake": article.is_fake,
            "confidence_score": article.confidence_score
        }
        
        logger.info(f"Generated fake news via API: {article.title[:50]}...")
        return jsonify({"success": True, "article": result})
        
    except Exception as e:
        logger.error(f"Error generating fake news via API: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/detect", methods=["POST"])
def api_detect() -> str:
    """API endpoint for detecting fake news."""
    try:
        data = request.get_json()
        title = data.get("title", "")
        content = data.get("content", "")
        
        if not content:
            return jsonify({"success": False, "error": "Content is required"}), 400
        
        # Detect fake news
        result = detector.detect_fake_news(content, title)
        
        # Convert to JSON-serializable format
        detection_result = {
            "is_fake": result.is_fake,
            "confidence_score": result.confidence_score,
            "explanation": result.explanation,
            "features": result.features
        }
        
        logger.info(f"Detection completed via API - Score: {result.confidence_score:.3f}")
        return jsonify({"success": True, "result": detection_result})
        
    except Exception as e:
        logger.error(f"Error detecting fake news via API: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/generate-and-detect", methods=["POST"])
def api_generate_and_detect() -> str:
    """API endpoint for generating and detecting fake news."""
    try:
        data = request.get_json()
        category = data.get("category", "random")
        
        # Generate fake news
        article = generator.generate_fake_news(category)
        
        # Detect fake news
        detection_result = detector.detect_fake_news(article.content, article.title)
        
        # Check if detection was correct
        detection_correct = detection_result.is_fake == article.is_fake
        
        # Convert to JSON-serializable format
        result = {
            "article": {
                "title": article.title,
                "content": article.content,
                "author": article.author,
                "source": article.source,
                "publish_date": article.publish_date.strftime("%Y-%m-%d"),
                "category": article.category,
                "is_fake": article.is_fake
            },
            "detection": {
                "is_fake": detection_result.is_fake,
                "confidence_score": detection_result.confidence_score,
                "explanation": detection_result.explanation,
                "features": detection_result.features
            },
            "detection_correct": detection_correct
        }
        
        logger.info(f"Generate and detect completed - Detection correct: {detection_correct}")
        return jsonify({"success": True, "result": result})
        
    except Exception as e:
        logger.error(f"Error in generate and detect via API: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    print("🤖 Fake News Generator and Detector Web App")
    print("=" * 50)
    print("🌐 Starting web server on http://localhost:5000")
    print("📱 Open your browser and navigate to the URL above")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True) 