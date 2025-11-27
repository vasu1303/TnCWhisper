from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scraping.webScraping import scrape_tnc
from summarize import summarization
from db import summaries

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["chrome-extension://<your-extension-id>"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UrlRequest(BaseModel):
    url:str

@app.post("/analyze")
async def analyze_url(data:UrlRequest):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url =  data.url
    domain  = url.split("/")[2] if url.startswith(("http", "https")) else url

    #checking if summary is there
    existing = summaries.find_one({"domain":domain})
    # if existing:
    #     return{
    #         "received_url":url,
    #         "tnc_text":tnc_text,
    #         "summary":existing.get("summary","")

    #     }
    # scraping tnc if it does not exist
    tnc_text = scrape_tnc(data.url, headers)

    

  

    #ab store karenge
    s = summarization(tnc_text)
    summaries.insert_one({
        "domain":domain,
        "tnc_text":tnc_text,
        "summary": s

    })
    return {"received_url":url, "summary":s}