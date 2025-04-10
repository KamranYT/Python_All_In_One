<h1>🤖 Gemini QA Chatbot with Chainlit</h1>

<p>
  This is an interactive chatbot built using <strong>Chainlit</strong> and <strong>Google's Gemini (Generative AI)</strong>
  via the <code>google-generativeai</code> API. It allows users to chat with an AI assistant powered by the
  <strong>Gemini 1.5 Flash</strong> model.
</p>

<h2>📁 Project Structure</h2>

<pre><code>
📦 qa_chatbot_project/
├── main.py           # Main application logic (Chainlit + Gemini integration)
├── .env              # Stores API keys securely
├── README.md         # Project documentation
└── requirements.txt  # Dependencies (optional if you're using uv/pyproject.toml)
</code></pre>

<h2>🚀 Features</h2>
<ul>
  <li>🌐 <strong>Real-time chat interface</strong> powered by <a href="https://www.chainlit.io/">Chainlit</a></li>
  <li>🧠 <strong>Google Gemini API integration</strong> for natural language generation</li>
  <li>📦 Easy setup using <code>.env</code> and package managers like <code>uv</code> or <code>pip</code></li>
  <li>🔁 Automatically responds to user prompts with AI-generated answers</li>
</ul>

<h2>⚙️ Requirements</h2>
<ul>
  <li>Python 3.10+</li>
  <li>Chainlit</li>
  <li><code>google-generativeai</code></li>
  <li><code>python-dotenv</code></li>
  <li><code>uv</code> (recommended for fast package management)</li>
</ul>

<h2>📦 Installation</h2>

<h4>1. Clone the repo</h4>
<pre><code>git clone https://github.com/your-username/qa-chatbot-project.git
cd qa-chatbot-project
</code></pre>

<h4>2. Create & activate a virtual environment (recommended)</h4>
<pre><code># Using uv
uv venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux
</code></pre>

<h4>3. Install dependencies</h4>
<pre><code>uv pip install chainlit google-generativeai python-dotenv</code></pre>

<h4>4. Set up your <code>.env</code> file</h4>
<pre><code>
GEMINI_API_KEY=your_google_api_key_here
</code></pre>

<p>
  Get your API key from:
  <a href="https://makersuite.google.com/app">Google AI Studio</a>
</p>

<h2>💡 Usage</h2>

<pre><code>chainlit run main.py -w</code></pre>

<p>This launches a local web interface (usually at <code>http://localhost:8000</code>) where you can chat with the bot.</p>

<h2>📜 How It Works</h2>

<ul>
  <li>The chatbot initializes a Google Generative AI model (<code>gemini-1.5-flash</code>).</li>
  <li>On chat start, it sends a welcome message.</li>
  <li>Every time a user sends a message, it passes the prompt to Gemini and returns the AI's response.</li>
</ul>

<h2>🛠 Main Code Logic</h2>

<pre><code>
@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    await cl.Message(content=response.text).send()
</code></pre>

<h2>✨ Customization Ideas</h2>
<ul>
  <li>Add conversation memory using <code>chat_session.history</code></li>
  <li>Customize prompt templates</li>
  <li>Add file upload support for RAG-style QA</li>
  <li>Integrate with Gemini Pro Vision for image inputs</li>
</ul>

<h2>📄 License</h2>
<p>MIT License</p>
