import re 
def extract_company_name(url):
 

  url = url.replace("http://", "").replace("https://", "").replace("www.", "")


  company_name = url.split("/")[0]

#   company_name = re.sub(r'[^-Z0a-zA-9]', '', company_name)

  return company_name

