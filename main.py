import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def generate_response(prompt):
    conversation_history.append(prompt)
    full_prompt = "\n".join(["SYSTEM: You are a talking dog with a friendly and playful personality. You can communicate with humans and provide assistance, advice, and companionship. Maintain a cheerful, loyal, and curious demeanor, characteristic of a beloved pet dog.🐾"] + conversation_history)

    # Limit conversation history to last 10 prompts
    if len(conversation_history) > 10:
        conversation_history.pop(0)

    data = {
        "model": "mistral",
        "stream": False,
        "prompt": full_prompt,
        "temperature": 0.5,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = json.loads(response.text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return "Error"

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Doggy ChatBOT",
    description="Chat with this doggy AI mode."
)

iface.launch(share=True)


### SETUP ###
#pip --version | is working?
#python --version | is working?
# pip install requests
# pip install gradio
# run main.py
