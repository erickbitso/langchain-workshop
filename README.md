# Langchain workshop

Welcome to the Langchain workshop. This is a basic explanation on how AI agents work and how to develop them using the Langchain and Langgraph framework.

## Requirements

### Install Python 3.12
```
brew install python@3.12
```

### Clone the repo
```
git clone https://github.com/erickbitso/langchain-workshop.git
cd langchain-workshop
```

### Using python3.12, create and activate a virtual environment
```
python3.12 -m venv myenv 
source myenv/bin/activate
```

### Upgrade pip
```
pip install --upgrade pip
```

### Install packages
```
pip install -r requirements.txt
```

### Set OPENAI env vars (if you have them)
```
export OPENAI_API_KEY=xxxx
```

### Set Langchain credentials (if you have them)
```
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="xxxx"
```

### Install ollama and make sure to have ollama3.2
```
$ ollama list
NAME               ID              SIZE      MODIFIED    
llama3.2:latest    a80c4f17acd5    2.0 GB    5 weeks ago    
```
