#!/usr/bin/env bash

source scripts/languages.bash

# Load environment variables from .env file
function load_env_vars() {
  if [ -f .env ]; then
    # shellcheck disable=SC2046
    export echo $(sed <.env 's/#.*//g' | xargs | envsubst)

    # Check if required variables are set and not equal to default values
    if [ "$NICKNAME" = "your_nickname" ] || [ "$LANGUAGE" = "choose_your_language" ]; then
      echo "Error: Required environment variables are set to default values."
      echo "Please update NICKNAME and LANGUAGE in the .env file with appropriate values."
      exit 1
    fi

    # Check if the specified language is valid

    if [[ ! "${!language_extensions[@]}" =~ $LANGUAGE ]]; then
      echo "Error: Invalid language specified in the .env file."
      echo "Please set LANGUAGE to one of the following valid languages:"
      echo "${!language_extensions[@]}"
      exit 1
    fi
  fi
}

# Check if a command is installed
function check_command() {
  local command="$1"
  if ! command -v "$command" &>/dev/null; then
    echo "The $command command is not installed."
    read -r -p "Do you want to install $command? (Y/n): " install_command
    case "$install_command" in
    [nN] | [nN][oO])
      echo "Installation of $command has been rejected. Exiting the script."
      exit 1
      ;;
    *)
      echo "Proceeding with the installation of $command..."
      brew install "$command"
      ;;
    esac
  fi
}

# Generates the solution code template with question details and author information
function make_solution_code() {
  local question_id=$1
  local question_name=$2
  local question_url=$3
  local code=$4
  local comment=${language_comments[$LANGUAGE]}
  local nickname
  if [ -n "$NICKNAME" ]; then
    nickname=$NICKNAME
  else
    nickname=Unknown
  fi
  local content
  content=$(
    cat <<EOF
${comment}
${comment}$question_id. $question_name
${comment}$question_url
${comment}Dale-Study
${comment}
${comment}Created by $nickname on $(date "+%Y/%m/%d").
${comment}

$code

EOF
  )
  echo "$content"
}

# Saves the solution code to a file in the appropriate directory based on the question slug and author's nickname
function save_file() {
  local DIR
  local title_slug="$1"
  local content="$2"
  local nickname
  local language_extension
  local solution_folder
  local solution_file

  if [ -n "$NICKNAME" ]; then
    nickname=$NICKNAME
  else
    nickname=Unknown
  fi

  DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
  language_extension=${language_extensions[$LANGUAGE]}

  solution_folder="$DIR/../$title_slug"
  mkdir -p "$solution_folder"

  solution_file="$solution_folder/$nickname.$language_extension"
  echo "$content" >"$solution_file"
  echo "File creation completed"
}
