import requests
import json

def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "mistral",
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "stream": True  # Streaming modunu aktif ediyoruz
    }
    
    response = requests.post(url, json=data, stream=True)
    final_response = ""
    
    for line in response.iter_lines():
        if line:
            try:
                decoded_line = line.decode("utf-8").strip()
                # Eğer boş satır değilse JSON objesini çöz ve tokenı ekle
                if decoded_line:
                    json_obj = json.loads(decoded_line)
                    final_response += json_obj.get("response", "")
            except Exception as e:
                print("Hata:", e)
    
    return final_response

# Örnek kullanım:
if __name__ == "__main__":
    prompt = (
        "You are a student advisor at USF. You are given data about course performance. "
        "Based on this data, answer the following question.\n\n"
        "Context:\n- MAC2282 -921-C: A rate is 58%, total 50 students\n- MAC2282 -922-C: A rate is 69%, total 49 students\n\n"
        "Question:\nBu derste en iyi öğretmen hangisidir?\n\nAnswer: "
    )
    
    answer = query_ollama(prompt)
    print("Ollama Yanıtı:", answer)
