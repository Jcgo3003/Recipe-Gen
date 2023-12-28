import sys
from openai import OpenAI

def recipe_creator(api_key, transcript):
    # Setting the api key

    client = OpenAI(api_key=api_key)

    file = transcript

    with open(file, 'r') as document:
        content = document.read()

    # Setting up system's behavieur
    messages = [
        {"role": "system", "content": "You are a very precise Kitchen book editor."},
    ]

    # Getting the ingredients 
    question = "Trascribe los ingredientes del siguiente texto: " + content

    messages.append({"role": "user", "content": question},)

    answer = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages)
        
    ingredients = chat.choices[0].message.content
    print(ingredients)
    messages.append({"role": "assistant", "content": ingredients})

    # Getting the process
    question = "Trascribe el procedimiento de la receta "

    messages.append({"role": "user", "content": question})

    answer = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )

    process = chat.choices[0].message.content
    print(process)
    messages.append({"role": "assistant", "content": process})

    # Getting the name
    question = "Que nombre le darias a esta receta "

    messages.append({"role": "user", "content": question},)

    answer = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
        
    name = chat.choices[0].message.content
    print(name)
    messages.append({"role": "assistant", "content": name})

    # Create a document
    file = name + ".txt"

    with open(file, 'w') as document:
        # Write the content
        document.write(f'{name}\n\n')
        document.write(f'Ingredientes:\n {ingredients}\n')
        document.write(f'Procedimiento:\n {process}\n')


if __name__ == '__main__':
    # Check if the input file is provided
    if len(sys.argv) < 3:
        print("Por favor escribe tu openai Api key")
        sys.exit(1)

    # Get the input file from command line arguments
    api_key = sys.argv[1]
    transcript = sys.argv[2]

    # Call the remove_timestamps function with the provided file path
    recipe_creator(api_key, transcript)


