from ollama import chat

print("Synora - A chatbot that Remembers")
messages=[]
messages.append({
    "role": "system",
    "content": "answer in a sentence of around 50 words max"
})
while True:
    question = input("You: ").strip()
    if question.lower() == "exit":
        print("Good Bye")
        break
    elif question.lower() == "history":
        print("\n------chat History-----")
        for message in messages:
            if message["role"]=="user":
                print("you: ",message["content"])
            elif message["role"]=="assistant":
                print("Bot:",message["content"])
            print("-----------\n")
    else:
        messages.append({
            "role": "user",
            "content": question
        })
        response = chat(model = "gemma3:1b", messages=messages)
        answer = response.message.content
        messages.append({
            "role": "assistant",
            "content": answer
        }) 
        print("Synora: " , answer)