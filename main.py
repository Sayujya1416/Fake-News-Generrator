"""
Fake News Generator and Detector using AI and NLP
A comprehensive system for generating and detecting fake news using machine learning techniques.
"""

import re
import random
import string
from typing import List, Dict, Tuple, Optional, Union
from dataclasses import dataclass
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class NewsArticle:
    """Data class representing a news article with metadata."""
    title: str
    content: str
    author: str
    source: str
    publish_date: datetime
    category: str
    is_fake: bool
    confidence_score: float = 0.0


@dataclass
class DetectionResult:
    """Data class representing fake news detection results."""
    is_fake: bool
    confidence_score: float
    features: Dict[str, float]
    explanation: str


class FakeNewsGenerator:
    """
    AI-powered fake news generator using NLP techniques.
    Generates realistic-looking fake news articles based on templates and patterns.
    """
    
    def __init__(self) -> None:
        """Initialize the fake news generator with templates and patterns."""
        self.templates = {
            "conspiracy": [
                "BREAKING: {subject} secretly {action} by {organization}",
                "Shocking discovery: {subject} linked to {conspiracy}",
                "Exclusive: {organization} covers up {scandal} involving {subject}"
            ],
            "sensational": [
                "You won't believe what {subject} just did!",
                "Incredible: {subject} reveals {surprising_fact}",
                "Amazing discovery: {subject} changes everything we know about {topic}"
            ],
            "clickbait": [
                "This {subject} will shock you!",
                "The truth about {subject} that {organization} doesn't want you to know",
                "{number} reasons why {subject} is {adjective}"
            ]
        }
        
        self.subjects = [
            "scientists", "politicians", "celebrities", "doctors", "experts",
            "researchers", "officials", "authorities", "insiders", "whistleblowers"
        ]
        
        self.actions = [
            "discovered", "revealed", "uncovered", "exposed", "found",
            "announced", "confirmed", "admitted", "confessed", "disclosed"
        ]
        
        self.organizations = [
            "government", "big pharma", "mainstream media", "tech companies",
            "financial institutions", "health organizations", "research labs"
        ]
        
        self.conspiracies = [
            "mind control", "population control", "secret experiments",
            "hidden technology", "suppressed cures", "fake news", "cover-ups"
        ]
        
        self.scandals = [
            "corruption", "fraud", "misconduct", "scandal", "controversy",
            "illegal activities", "secret deals", "hidden agendas"
        ]
        
        self.surprising_facts = [
            "the truth about vaccines", "secret government programs",
            "hidden health benefits", "suppressed research", "real causes of diseases"
        ]
        
        self.topics = [
            "health", "politics", "science", "technology", "medicine",
            "economics", "education", "environment", "society", "history"
        ]
        
        self.adjectives = [
            "dangerous", "revolutionary", "controversial", "amazing", "shocking",
            "incredible", "unbelievable", "mind-blowing", "life-changing"
        ]
        
        self.numbers = ["5", "7", "10", "13", "21", "50", "100"]
        
        logger.info("FakeNewsGenerator initialized successfully")
    
    def _generate_random_name(self) -> str:
        """Generate a random author name."""
        first_names = ["Dr.", "Prof.", "John", "Sarah", "Michael", "Emma", "David", "Lisa"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    def _generate_random_source(self) -> str:
        """Generate a random news source name."""
        sources = [
            "TruthSeeker News", "Real Facts Daily", "Independent Investigators",
            "Alternative Media Network", "Conspiracy Chronicles", "Hidden Truth Report",
            "Real News Network", "Truth Uncovered", "Independent Research Institute"
        ]
        return random.choice(sources)
    
    def _generate_content(self, title: str) -> str:
        """Generate article content based on the title."""
        paragraphs = []
        
        # Introduction paragraph
        intro_templates = [
            "In a {adjective} revelation that has {emotion} the {community}, {title_lower}.",
            "Recent developments have {action_past} to light regarding {topic}, specifically {title_lower}.",
            "A {adjective} discovery has {emotion} experts and {community} alike: {title_lower}."
        ]
        
        emotions = ["shocked", "surprised", "amazed", "concerned", "excited"]
        communities = ["scientific community", "medical world", "political sphere", "general public"]
        action_past = ["come", "brought", "revealed", "exposed"]
        
        intro = random.choice(intro_templates).format(
            adjective=random.choice(self.adjectives),
            emotion=random.choice(emotions),
            community=random.choice(communities),
            title_lower=title.lower(),
            action_past=random.choice(action_past),
            topic=random.choice(self.topics)
        )
        paragraphs.append(intro)
        
        # Body paragraphs
        body_templates = [
            "According to {expert_type} {expert_name}, this {discovery} could {impact}.",
            "Research conducted by {institution} suggests that {finding}.",
            "Multiple sources have {action} that {claim}.",
            "This {development} has {reaction} among {stakeholders}."
        ]
        
        expert_types = ["leading", "renowned", "distinguished", "prominent"]
        expert_names = ["Dr. Johnson", "Prof. Williams", "Dr. Brown", "Prof. Davis"]
        discoveries = ["finding", "discovery", "revelation", "breakthrough"]
        impacts = ["change everything", "revolutionize the field", "alter our understanding"]
        institutions = ["MIT", "Stanford", "Harvard", "Oxford", "Cambridge"]
        findings = ["the implications are significant", "further study is needed", "this warrants investigation"]
        actions = ["confirmed", "verified", "validated", "corroborated"]
        claims = ["the evidence is compelling", "the data supports this", "the results are consistent"]
        developments = ["finding", "discovery", "revelation", "announcement"]
        reactions = ["caused concern", "sparked debate", "generated interest", "raised questions"]
        stakeholders = ["experts", "researchers", "authorities", "the public"]
        
        for _ in range(random.randint(2, 4)):
            body = random.choice(body_templates).format(
                expert_type=random.choice(expert_types),
                expert_name=random.choice(expert_names),
                discovery=random.choice(discoveries),
                impact=random.choice(impacts),
                institution=random.choice(institutions),
                finding=random.choice(findings),
                action=random.choice(actions),
                claim=random.choice(claims),
                development=random.choice(developments),
                reaction=random.choice(reactions),
                stakeholders=random.choice(stakeholders)
            )
            paragraphs.append(body)
        
        # Conclusion paragraph
        conclusion_templates = [
            "As {topic} continues to {evolve}, this {finding} may {future_impact}.",
            "The implications of this {discovery} are {adjective}, and {next_steps}.",
            "This {revelation} raises important questions about {broader_issue}."
        ]
        
        evolves = ["evolve", "develop", "progress", "advance"]
        future_impacts = ["shape future research", "influence policy decisions", "change public perception"]
        next_steps = ["further investigation is warranted", "additional studies are needed", "more research is required"]
        broader_issues = ["scientific integrity", "public trust", "research methodology", "transparency"]
        
        conclusion = random.choice(conclusion_templates).format(
            topic=random.choice(self.topics),
            evolve=random.choice(evolves),
            finding=random.choice(discoveries),
            future_impact=random.choice(future_impacts),
            discovery=random.choice(discoveries),
            adjective=random.choice(self.adjectives),
            next_steps=random.choice(next_steps),
            revelation=random.choice(discoveries),
            broader_issue=random.choice(broader_issues)
        )
        paragraphs.append(conclusion)
        
        return " ".join(paragraphs)
    
    def generate_fake_news(self, category: str = "random") -> NewsArticle:
        """
        Generate a fake news article.
        
        Args:
            category: Type of fake news to generate ("conspiracy", "sensational", "clickbait", "random")
            
        Returns:
            NewsArticle: Generated fake news article
        """
        try:
            if category == "random":
                category = random.choice(list(self.templates.keys()))
            
            if category not in self.templates:
                raise ValueError(f"Invalid category: {category}")
            
            # Generate title
            template = random.choice(self.templates[category])
            title = template.format(
                subject=random.choice(self.subjects),
                action=random.choice(self.actions),
                organization=random.choice(self.organizations),
                conspiracy=random.choice(self.conspiracies),
                scandal=random.choice(self.scandals),
                surprising_fact=random.choice(self.surprising_facts),
                topic=random.choice(self.topics),
                number=random.choice(self.numbers),
                adjective=random.choice(self.adjectives)
            )
            
            # Generate content
            content = self._generate_content(title)
            
            # Generate metadata
            author = self._generate_random_name()
            source = self._generate_random_source()
            publish_date = datetime.now() - timedelta(days=random.randint(1, 30))
            
            article = NewsArticle(
                title=title,
                content=content,
                author=author,
                source=source,
                publish_date=publish_date,
                category=category,
                is_fake=True,
                confidence_score=0.95
            )
            
            logger.info(f"Generated fake news article: {title[:50]}...")
            return article
            
        except Exception as e:
            logger.error(f"Error generating fake news: {str(e)}")
            raise


class FakeNewsDetector:
    """
    AI-powered fake news detector using NLP and machine learning techniques.
    Analyzes text features to determine the likelihood of fake news.
    """
    
    def __init__(self) -> None:
        """Initialize the fake news detector with feature extraction methods."""
        self.fake_indicators = [
            "BREAKING", "SHOCKING", "INCREDIBLE", "AMAZING", "UNBELIEVABLE",
            "SECRET", "HIDDEN", "COVER-UP", "CONSPIRACY", "WHISTLEBLOWER",
            "EXCLUSIVE", "REVEALED", "EXPOSED", "UNCOVERED", "CONFIRMED",
            "ADMITTED", "CONFESSED", "DISCLOSED", "LEAKED", "INSIDER"
        ]
        
        self.credibility_indicators = [
            "study", "research", "peer-reviewed", "journal", "university",
            "scientist", "expert", "official", "government", "verified",
            "evidence", "data", "statistics", "analysis", "report"
        ]
        
        self.emotional_words = [
            "outrageous", "scandalous", "controversial", "shocking", "amazing",
            "incredible", "unbelievable", "mind-blowing", "life-changing",
            "revolutionary", "dangerous", "terrifying", "wonderful", "amazing"
        ]
        
        self.urgency_words = [
            "urgent", "immediate", "now", "today", "breaking", "live",
            "developing", "just in", "latest", "update", "alert"
        ]
        
        self.exaggeration_words = [
            "everyone", "nobody", "always", "never", "completely", "totally",
            "absolutely", "definitely", "certainly", "obviously", "clearly"
        ]
        
        logger.info("FakeNewsDetector initialized successfully")
    
    def _extract_text_features(self, text: str) -> Dict[str, float]:
        """
        Extract various text features for fake news detection.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dict containing feature scores
        """
        text_lower = text.lower()
        words = text.split()
        sentences = re.split(r"[.!?]+", text)
        
        features = {}
        
        # Length features
        features["word_count"] = len(words)
        features["sentence_count"] = len([s for s in sentences if s.strip()])
        features["avg_sentence_length"] = features["word_count"] / max(features["sentence_count"], 1)
        
        # Capitalization features
        features["all_caps_ratio"] = sum(1 for word in words if word.isupper() and len(word) > 1) / max(len(words), 1)
        features["title_case_ratio"] = sum(1 for word in words if word.istitle()) / max(len(words), 1)
        
        # Punctuation features
        features["exclamation_ratio"] = text.count("!") / max(len(words), 1)
        features["question_ratio"] = text.count("?") / max(len(words), 1)
        features["quotes_ratio"] = text.count('"') / max(len(words), 1)
        
        # Content features
        features["fake_indicator_ratio"] = sum(1 for word in words if word.upper() in self.fake_indicators) / max(len(words), 1)
        features["credibility_indicator_ratio"] = sum(1 for word in words if word.lower() in self.credibility_indicators) / max(len(words), 1)
        features["emotional_word_ratio"] = sum(1 for word in words if word.lower() in self.emotional_words) / max(len(words), 1)
        features["urgency_word_ratio"] = sum(1 for word in words if word.lower() in self.urgency_words) / max(len(words), 1)
        features["exaggeration_word_ratio"] = sum(1 for word in words if word.lower() in self.exaggeration_words) / max(len(words), 1)
        
        # Readability features
        features["unique_word_ratio"] = len(set(words)) / max(len(words), 1)
        features["long_word_ratio"] = sum(1 for word in words if len(word) > 6) / max(len(words), 1)
        
        return features
    
    def _calculate_fake_score(self, features: Dict[str, float]) -> float:
        """
        Calculate fake news probability score based on features.
        
        Args:
            features: Extracted text features
            
        Returns:
            Float between 0 and 1 representing fake news probability
        """
        # Weights for different features (higher = more important)
        weights = {
            "fake_indicator_ratio": 0.25,
            "credibility_indicator_ratio": -0.20,  # Negative weight (reduces fake score)
            "emotional_word_ratio": 0.15,
            "urgency_word_ratio": 0.10,
            "exaggeration_word_ratio": 0.15,
            "all_caps_ratio": 0.10,
            "exclamation_ratio": 0.05
        }
        
        score = 0.0
        
        for feature, weight in weights.items():
            if feature in features:
                score += features[feature] * weight
        
        # Normalize score to 0-1 range
        score = max(0.0, min(1.0, score))
        
        return score
    
    def _generate_explanation(self, features: Dict[str, float], score: float) -> str:
        """
        Generate human-readable explanation for the detection result.
        
        Args:
            features: Extracted text features
            score: Fake news probability score
            
        Returns:
            String explanation
        """
        explanations = []
        
        if features.get("fake_indicator_ratio", 0) > 0.05:
            explanations.append("Contains suspicious buzzwords commonly used in fake news")
        
        if features.get("emotional_word_ratio", 0) > 0.1:
            explanations.append("Uses excessive emotional language")
        
        if features.get("urgency_word_ratio", 0) > 0.05:
            explanations.append("Creates artificial urgency")
        
        if features.get("exaggeration_word_ratio", 0) > 0.1:
            explanations.append("Uses absolute/exaggerated language")
        
        if features.get("all_caps_ratio", 0) > 0.1:
            explanations.append("Excessive use of capital letters")
        
        if features.get("credibility_indicator_ratio", 0) > 0.05:
            explanations.append("Contains credible source indicators")
        
        if not explanations:
            if score > 0.7:
                explanations.append("Overall writing style suggests fake news")
            elif score < 0.3:
                explanations.append("Writing style appears credible")
            else:
                explanations.append("Mixed indicators - exercise caution")
        
        return "; ".join(explanations)
    
    def detect_fake_news(self, text: str, title: str = "") -> DetectionResult:
        """
        Detect if the given text is likely fake news.
        
        Args:
            text: Article content to analyze
            title: Article title (optional)
            
        Returns:
            DetectionResult: Detection results with confidence and explanation
        """
        try:
            # Combine title and content for analysis
            full_text = f"{title} {text}".strip()
            
            # Extract features
            features = self._extract_text_features(full_text)
            
            # Calculate fake score
            fake_score = self._calculate_fake_score(features)
            
            # Determine if fake (threshold at 0.6)
            is_fake = fake_score > 0.6
            
            # Generate explanation
            explanation = self._generate_explanation(features, fake_score)
            
            result = DetectionResult(
                is_fake=is_fake,
                confidence_score=fake_score,
                features=features,
                explanation=explanation
            )
            
            logger.info(f"Detection completed - Score: {fake_score:.3f}, Fake: {is_fake}")
            return result
            
        except Exception as e:
            logger.error(f"Error detecting fake news: {str(e)}")
            raise


def main() -> None:
    """Main function to demonstrate fake news generation and detection."""
    try:
        print("🤖 Fake News Generator and Detector")
        print("=" * 50)
        
        # Initialize components
        generator = FakeNewsGenerator()
        detector = FakeNewsDetector()
        
        while True:
            print("\nOptions:")
            print("1. Generate fake news")
            print("2. Detect fake news")
            print("3. Generate and detect")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🎭 Generating Fake News...")
                category = input("Enter category (conspiracy/sensational/clickbait/random): ").strip() or "random"
                
                article = generator.generate_fake_news(category)
                
                print(f"\n📰 Generated Article:")
                print(f"Title: {article.title}")
                print(f"Author: {article.author}")
                print(f"Source: {article.source}")
                print(f"Date: {article.publish_date.strftime('%Y-%m-%d')}")
                print(f"Category: {article.category}")
                print(f"\nContent:\n{article.content}")
                
            elif choice == "2":
                print("\n🔍 Fake News Detection")
                title = input("Enter article title (optional): ").strip()
                content = input("Enter article content: ").strip()
                
                if not content:
                    print("❌ Please provide article content")
                    continue
                
                result = detector.detect_fake_news(content, title)
                
                print(f"\n📊 Detection Results:")
                print(f"Fake News: {'❌ YES' if result.is_fake else '✅ NO'}")
                print(f"Confidence: {result.confidence_score:.1%}")
                print(f"Explanation: {result.explanation}")
                
            elif choice == "3":
                print("\n🎭🔍 Generate and Detect")
                category = input("Enter category (conspiracy/sensational/clickbait/random): ").strip() or "random"
                
                # Generate fake news
                article = generator.generate_fake_news(category)
                
                print(f"\n📰 Generated Article:")
                print(f"Title: {article.title}")
                print(f"Author: {article.author}")
                print(f"Source: {article.source}")
                print(f"Content: {article.content[:200]}...")
                
                # Detect fake news
                result = detector.detect_fake_news(article.content, article.title)
                
                print(f"\n📊 Detection Results:")
                print(f"Fake News: {'❌ YES' if result.is_fake else '✅ NO'}")
                print(f"Confidence: {result.confidence_score:.1%}")
                print(f"Explanation: {result.explanation}")
                
                # Show if detection was correct
                detection_correct = result.is_fake == article.is_fake
                print(f"Detection Correct: {'✅ YES' if detection_correct else '❌ NO'}")
                
            elif choice == "4":
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-4.")
                
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        logger.error(f"Unexpected error in main: {str(e)}")
        print(f"❌ An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
