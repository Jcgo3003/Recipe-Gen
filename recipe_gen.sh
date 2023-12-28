#!/bin/bash

echo "Hola, introduce un link a un video de cocina en Youtube"

# Access an environment variable
read yt_link

# Check if the variable is set
if [ -z "$yt_link" ]; then
  echo "No has escrito el link"

else
  # Run the script and capture its output
  yt-dlp --convert-subs srt --write-auto-sub --sub-lang es --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' --skip-download --output "%(uploader)s-%(title)s.%(ext)s" "$yt_link"

  generated_file=$(ls -t | head -n1)

  # Check if yt-dlp as created a file
  if [ -z "$generated_file" ]; then
    echo "Error! No se genero un subtitulo revisa el link"
  else
    python3 subs_cleaner.py "$generated_file"
    rm "$generated_file"

    str_file=$(ls -t | head -n1)
    mv "$str_file" "recipe.txt"
    # subl "recipe.txt"

  fi
fi

# Getting the api key
echo "\n\n### ------------------------ ###"
echo "Ahora introduce tu openai api key"

# Access an environment variable
read api_key

# Check if the variable is set
if [ -z "$api_key" ]; then
  echo "No has escrito tu api key"
else
  # Create the recipe with AI
  python3 ai.py "$api_key" "recipe.txt"

  # Recipe_file=$(ls -t | head -n1)
  # subl "$Recipe_file"
fi

# Say goodbye
cowsay "Buen provecho"
