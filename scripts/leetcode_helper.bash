#!/usr/bin/env bash

# Extract the title-slug from the LeetCode URL
function extract_problem_name() {
  local url="$1"
  echo "$url" | sed -n 's/.*\/problems\/\([^/]*\)\/.*/\1/p'
}

# Generates the GraphQL query to fetch problem details based on the provided title-slug
function make_query() {
  local question_slug=$1
  # shellcheck disable=SC2016
  local query='{
  "query": "query selectProblem($titleSlug: String!) { question(titleSlug: $titleSlug) { questionFrontendId title titleSlug codeSnippets { langSlug code } } }",
  "variables": {
    "titleSlug": "'"$question_slug"'"
  }
}'
  echo "$query"
}

# Sends a POST request to the LeetCode GraphQL API with the generated query
function request() {
  local query="$1"
  local response
  response=$(curl -s -X POST -H "Content-Type: application/json" --data "$query" https://leetcode.com/graphql)
  echo -E "$response"
}

# Creates a file for the LeetCode problem
#
# Parses the JSON response from the LeetCode API, extracts relevant problem details,
# generates the solution code template using the `make_solution_code()` function,
# and saves the file using the `save_file()` function.
function create_file() {
  local json_data="$1"
  local question_id
  local title
  local title_slug
  local code_snippet
  local content

  question_id=$(echo -E "$json_data" | jq -r '.data.question.questionFrontendId')
  title=$(echo -E "$json_data" | jq -r '.data.question.title')
  title_slug=$(echo -E "$json_data" | jq -r '.data.question.titleSlug')

  # Generate the code snippet
  code_snippet=$(echo -E "$json_data" | jq -r ".data.question.codeSnippets[] | select(.langSlug == \"$LANGUAGE\") | .code")

  # Generate the entire code
  content=$(make_solution_code "$question_id" "$title" "https://leetcode.com/problems/$title_slug/description/" "$code_snippet")

  save_file "$title_slug" "$content"
}
