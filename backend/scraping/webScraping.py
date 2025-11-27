import requests
from bs4 import BeautifulSoup
from scraping.helpingPrograms.extractAllLink import get_links
from scraping.helpingPrograms.extractTncLink import extract_required_link
from scraping.helpingPrograms.termsAndConditionExtractor import scrape_terms_and_conditions
from scraping.helpingPrograms.companyName import extract_company_name
from scraping.helpingPrograms.saveAsFile import save_as_file
from scraping.helpingPrograms.similarTncPhases import terms_and_conditions_alternatives



def scrape_tnc(url:str, headers: dict)->str:
    try:
        company_name = extract_company_name(url)
        save_as_file(url, "scraping/data/hello.html")


        href_of_site = get_links(url, headers)
        if not href_of_site:
            return "No links found on this website"
        
        req_link = extract_required_link(href_of_site, terms_and_conditions_alternatives, company_name.replace(".com", ""))

        if not req_link:
            return "No TnC link found on the website"
        
        if not req_link.startswith("http://") and not req_link.startswith("https://"):
            req_link = "https://" + company_name + req_link

        terms = scrape_terms_and_conditions(
            req_link, 
            f"scraping/data/{company_name.replace('.com','')}.csv",
            headers
        )
        if not terms:
            return "Could not extract TnC content"
        
        return terms
    

    
    
    except Exception as e:
        return f"Error during scraping : {str(e)}"
    
