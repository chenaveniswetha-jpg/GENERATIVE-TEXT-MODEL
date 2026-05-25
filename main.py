from transformers import pipeline

# load AI text generator
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# user input
text = input("Enter your topic: ")

# generate text
result = generator(
    text,
    max_length=100,
    num_return_sequences=1
)

# display output
print("\nGenerated Text:\n")

print(result[0]['generated_text'])