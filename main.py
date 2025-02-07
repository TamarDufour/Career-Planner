from symbol import continue_stmt
import csv
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# Enter your credentials - the zone name and password to Bright Data
AUTH = 'USER:PASS'

SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def save_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

def main():
    all_titles = []
    all_companies = []
    all_urls = []
    all_jod_details = []
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    driver = Remote(sbr_connection, options=ChromeOptions())

    num_of_listing_containers = 0
    while num_of_listing_containers<1000:
        try:
            # connect selenium dreiver to the site
            driver.get(f'https://www.indeed.com/jobs?q=developer')
            #driver.get(f'https://www.indeed.com')
        except Exception as e:
            print(f'Error: {e}')
            print("We all know that there is no reason to continue, so we are exiting...")
            driver.quit()
            return all_titles, all_companies, all_urls, all_jod_details

        time.sleep(6)  # Pause for 5 seconds before the next iteration, in case of CAPCHA or other issues
        #(driver.page_source returns the HTML it currently sees)
        job_listing_containers = BeautifulSoup(driver.page_source, 'html.parser').find_all('div', class_="job_seen_beacon")#should return a list of all job listings in the page
        if len(job_listing_containers) <1:
            print('No job listings found, exiting...')
            break
        num_of_listing_containers += len(job_listing_containers)
        for job_listing in job_listing_containers:
            # Extract the job title, company name, location, and job description
            job_all = job_listing.find_all_next('h2', class_='jobTitle')
            title = job_all[0].find('span').text

            company_span = job_listing.find('span', {'data-testid': 'company-name'})
            company_name = company_span.text if company_span else 'N/A'

            #the usrl is the url of the job (full description)
            job_link = job_listing.find('a', href = True)
            url = f'https://www.indeed.com{job_link["href"]}' if job_link else 'N/A'
            #url = f'https://il.indeed.com/viewjob?{job_all[0].find_all_next("a")[0]["href"].split("?")[1]}'
            print(f'Title: {title}\nCompany: {company_name}\nURL: {url}\n')
            all_titles.append(title)
            all_companies.append(company_name)
            all_urls.append(url)

        #collect the data from each job url
        for i, url in enumerate(all_urls):
            try: # Try to open the URL
                driver.get(url)
                print(f'Opened URL: {url}')
            except Exception as e:
                print(f'Error: {e}')
                continue
            time.sleep(6)
            """
            try:
                job_details = BeautifulSoup(driver.page_source, 'html.parser').find_all('div', class_='jobsearch-BodyContainer')
                all_jod_details.append(job_details.text if job_details else 'N/A')
                print("Job details found for job title: ", all_titles[i])
            except:
                print(f'Error: Could not find job details for job title: {all_titles[i]}')
                continue
            time.sleep(7)
            """
            try:
                job_details = BeautifulSoup(driver.page_source, 'html.parser').find('div', id='jobDescriptionText', class_='jobsearch-JobComponent-description')
                job_description_text = job_details.get_text(separator='\n', strip=True)
                all_jod_details.append(job_description_text)  # Save to list
                print("Full Job Description:")
                print(job_description_text)
            except:
                print(f'Error: Could not find job details for job title: {all_titles[i]}')
                continue
    driver.quit()
    return all_titles, all_companies, all_urls, all_jod_details



if __name__ == '__main__':
    all_titles, all_companies, all_urls, all_jod_details = main()
    save_to_csv('titles1.csv', all_titles)
    save_to_csv('companies1.csv', all_companies)
    save_to_csv('urls1.csv', all_urls)
    save_to_csv('job_details1.csv', all_jod_details)


