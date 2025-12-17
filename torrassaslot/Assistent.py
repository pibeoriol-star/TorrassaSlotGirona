import openai
from openai import OpenAI

# Substitueix per la teva clau API
client = OpenAI(api_key="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")

def xat():
    print("Benvingut al teu assistent ChatGPT! (escriu 'sortir' per tancar)")
    while True:
        pregunta = input("Tu: ")
        if pregunta.lower() in ["sortir", "exit", "quit"]:
            print("Fins aviat!")
            break

        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pregunta}]
        )
        print("Assist: " + resposta.choices[0].message.content)

if __name__ == "__main__":
    xat()