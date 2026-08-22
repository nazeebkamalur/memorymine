from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def generate_answer(question, memories):
    if not memories:
        return "No relevant memory found."

    # IMPORTANT: send the FULL extracted text
    context = "\n\n".join([m["text"] for m in memories])

    prompt = f"""
You are MemoryMine AI.

Answer ONLY from the provided context.
If the question asks for names, list every person's name.
Do not invent information.

Question:
{question}

Context:
{context}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=False
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)