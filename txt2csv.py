import pandas as pd
import re
import os

def process_file(input_file, output, country, search_word):
    # Lists to store extracted data
    titles = []
    companies = []
    urls = []
    job_descriptions = []

    # Read the text file
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Initialize variables to track job description
    current_description = []
    is_collecting_description = False

    # Process each line
    for line in lines:
        # Extract Title, Company, and URL
        title_match = re.search(r"Title:?\s*(.+)", line, re.IGNORECASE)
        company_match = re.search(r"Company:?\s*(.+)", line, re.IGNORECASE)
        url_match = re.search(r"URL:?\s*(https?://\S+)", line, re.IGNORECASE)

        # Start collecting job description
        if "Full Job Description" in line:
            if current_description:
                job_descriptions.append(' '.join(current_description).strip())
            is_collecting_description = True
            current_description = []
            continue

        if "Error: Message:" in line:
            is_collecting_description = False
            if current_description:
                job_descriptions.append(' '.join(current_description).strip())
            job_descriptions.append('Error')
            current_description = []
            continue

        # Collect description if flag is set
        if is_collecting_description:
            current_description.append(line.strip())

        # Append extracted fields
        if title_match:
            titles.append(title_match.group(1).strip())
        if company_match:
            companies.append(company_match.group(1).strip())
        if url_match:
            urls.append(url_match.group(1).strip())

    # Append the last collected description if any
    if current_description:
        job_descriptions.append(' '.join(current_description).strip())

    # Ensure all lists are the same length
    max_length = max(len(titles), len(companies), len(urls), len(job_descriptions))
    titles.extend(['N/A'] * (max_length - len(titles)))
    companies.extend(['N/A'] * (max_length - len(companies)))
    urls.extend(['N/A'] * (max_length - len(urls)))
    job_descriptions.extend(['N/A'] * (max_length - len(job_descriptions)))

    # Create a pandas DataFrame
    df = pd.DataFrame({
        "Title": titles,
        "Company": companies,
        "URL": urls,
        "Full Job Description": job_descriptions
    })

    df['Country'] = country
    df['Search Word'] = search_word

    # Save to a CSV file
    df.to_csv(f"tables/{output}.csv", index=False)

    print(f"Data successfully extracted!")

    return df


if __name__ == '__main__':
    folder_path = 'txt files scrapping'
    all_dfs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.splitext(filename)[0]
            country, search_word = output_file.split('_')
            df = process_file(input_file, output_file, country, search_word)
            all_dfs.append(df)
    for i in range(1, len(all_dfs)):
        all_dfs[0] = pd.concat([all_dfs[0], all_dfs[i]], ignore_index=True)
    all_dfs[0].to_csv('all_data.csv', index=False)