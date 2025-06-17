import httpx

LLAMA_API_URL = "http://llama:8080/completion"

def run_prompt(prompt: str) -> str:
    payload = {
        "prompt": f"[INST] {prompt} [/INST]",
        "max_tokens": 200,
        "temperature": 0.7
    }
    response = httpx.post(LLAMA_API_URL, json=payload, timeout=120)
    response.raise_for_status()
    result = response.json()
    return result.get('content', 'No response from LLM.')
