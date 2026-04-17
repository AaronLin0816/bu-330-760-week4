# Week 4 Starter: Math Agent

A ReAct agent that solves questions using tool calls.

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it.

2. Copy `.env.example` to `.env` and add your API key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and replace `your-key-here` with your Anthropic API key from [Anthropic Console](https://console.anthropic.com/).

   To use a different provider, change the `MODEL` variable in `agent.py` and set the matching key in `.env`. The default model is `anthropic:claude-sonnet-4-6` (requires `ANTHROPIC_API_KEY`).

3. Make sure `.env` is in your `.gitignore` so you don't commit your key.

## Run

```bash
uv run agent.py
```

uv will install dependencies automatically on first run. Alternatively, install dependencies with `pip install pydantic-ai python-dotenv` and run with `python agent.py`.

The agent will work through each question in `math_questions.md` and print the ReAct trace (Reason / Act / Result) for each one.

## Videos

- [Week 4 Lecture](https://youtu.be/IBs_QfH7imo)

## Files

- `agent.py` - the ReAct agent with `calculator_tool` and `product_lookup` tools
- `calculator.py` - evaluates math expressions safely
- `lookup_function.py` - reads `products.json` and returns product prices
- `products.json` - product catalog with prices (Alpha, Beta, Gamma, Delta, Epsilon Widgets)
- `math_questions.md` - the questions the agent solves
- `.env.example` - template for your API key
