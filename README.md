# Fake-News-Generator
📰 Fake News Generator using GPT-3.5
A simple yet powerful Fake News Generator built using OpenAI's GPT-3.5 API. This project demonstrates how generative AI models can be used (and misused), and is intended for educational and research purposes only.

🚀 Features
🔥 Generates fake news articles from a given prompt using GPT-3.5.

🎨 User-friendly GUI using Tkinter or Streamlit.

💡 Easily extendable for multilingual content or topic-specific generation.

🔐 Securely integrates with OpenAI API.

⚠️ Disclaimer
This project is intended strictly for educational purposes to understand the dangers of AI-generated misinformation. Do NOT use this tool to spread real fake news. Use responsibly.

🧠 Technologies Used
Python 3.x

OpenAI GPT-3.5 API

Tkinter (GUI) or Streamlit (GUI)

dotenv (for managing API keys)

📦 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/fake-news-generator.git
cd fake-news-generator
pip install -r requirements.txt
🔑 Setup
Get your OpenAI API key from https://platform.openai.com/account/api-keys.

Create a .env file in the root directory:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
🧪 How to Run
Option 1: Run from command line (basic script)
bash
Copy
Edit
python gpt_generator.py
Option 2: Run the GUI (Streamlit)
bash
Copy
Edit
streamlit run gui_streamlit.py
Option 3: Run the GUI (Tkinter)
bash
Copy
Edit
python gui_tkinter.py
✍️ Example Prompt
"Write a fake news article about aliens landing in Paris."

Generated Output:

"On Monday morning, residents of Paris woke up to an astonishing sight — a fleet of alien spacecraft hovering over the Eiffel Tower..."

📁 Project Structure
bash
Copy
Edit
fake-news-generator/
│
├── gpt_generator.py         # Core script for fake news generation
├── gui_tkinter.py           # GUI using Tkinter
├── gui_streamlit.py         # GUI using Streamlit
├── .env                     # Your API key (not to be shared)
├── requirements.txt         # Required Python libraries
└── README.md                # You're here!
🛠 To-Do (Optional Extensions)
Add multilingual support

Integrate news article scraping for prompt generation

Add generation filters (topic, tone, length)

Log generations for analysis

🙏 Acknowledgements
OpenAI for their powerful language model

Streamlit and Tkinter community

Educational inspiration from misinformation research studies

📜 License
MIT License. See LICENSE file for more details.
