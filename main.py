from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)
text = input("Enter your topic: ")

result = generator(
    text,
    max_length=100,
    num_return_sequences=1
)
print("\nGenerated Text:\n")

print(result[0]['generated_text'])
