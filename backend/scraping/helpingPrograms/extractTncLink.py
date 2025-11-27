terms_and_conditions_alternatives = {
    "terms", "termsandcondition","privacy","agreement", "contract", "termsofservice", "serviceagreement", "useragreement",
    "serviceterms", "conditionsofuse", "enduserlicenseagreement", "usepolicy", 
    "rulesandregulations", "legalagreement", "userpolicy", "customeragreement", 
    "termsofuse", "usageagreement", "usageguidelines", "legalterms", "termsofsale", 
    "siteterms", "conditionsofservice", "termsofengagement", "policyagreement", 
    "subscriberagreement", "servicepolicy", "userterms", "generalconditions", 
    "userconditions", "serviceconditions", "legalnotice", "licensingterms", 
    "licensingagreement", "sitepolicies", "subscriptionagreement", "contractualagreement", 
    "usageconditions", "platformterms", "platformagreement", "accessagreement", 
    "userguidelines", "guidelinesofuse", "usagepolicies", "consumeragreement", 
    "consumerterms", "legalcontract", "policyterms", "servicerules", "consumercontract",
    "conditionsofcontract", "termsofsubscription", "subscribersterms", "clientagreement",
    "clientterms", "websiteterms", "applicationterms", "appterms", "customerterms",
    "termsofaccess", "datapolicy", "membershipagreement", "purchaseagreement", 
    "rulesofengagement", "operationalconditions", "usercontract", "userserviceagreement", 
    "websiteusepolicy", "appusepolicy", "customerpolicies", "usercomplianceagreement", 
    "legalrequirements", "serviceuseguidelines", "engagementterms", "purchaseconditions", 
    "salesagreement", "salescontract", "licenseagreement", "websiterules", "datausageagreement", 
    "platformguidelines", "accesspolicy", "platformconditions", "productterms", "productagreement", 
    "onlineagreement", "servicelicensing", "enduseragreement", "userlicensingagreement", 
    "softwareterms", "softwarelicense", "websiteusageterms", "appusageterms", 
    "operationalguidelines", "siteusageguidelines", "purchasepolicies", "conditionsforuse", 
    "platformrules", "webserviceterms", "digitalserviceagreement", "compliancepolicy", 
    "salesterms", "commercialterms","tnc", "tc", "tos", "tou", "eula", "sla", "ula", 
    "thefineprint", "usagerules", "conditionsyoumustaccept", "yourrightsandobligations", 
    "whatyoureagreeingto", "rulesforusingtheservice", "contractualobligations", 
    "servicestipulations", "theguidelinesyouagreeto", "yourcommitment", "thelegalstuff", 
    "rulesoftheroad", "engagementrules", "termsyouagreeto", "yourlegalresponsibilities", 
    "mandatoryterms", "policiesforusers", "userresponsibilities", "usagelimitations", 
    "yourserviceagreement", "conditionsforserviceuse", "usagecontract", "thelegalframework", 
    "groundrulesforservice", "conditionsyoumustfollow", "usercommitments", "rulesofservice", 
    "theagreementtofollow", "servicerestrictions", "contractualcommitments", 
    "termsyouresigningupfor", "thecontract", "servicerequirements", "rulesofengagement", 
    "whatsrequiredofyou", "servicespecificrules", "youruseragreement", 
    "thepoliciesyouagreeto", "obligationsforservice", "contractualpolicies", 
    "usagespecificconditions", "consumerresponsibilities", "termsyouconsentto", 
    "thestipulationsforuse", "servicepolicyframework", "usagerulesyouagreeto", 
    "obligatoryconditions", "yourcontractwithus", "thesmallprint", "whatyouneedtofollow", 
    "engagementobligations", "servicerulesandobligations", "regulatoryterms", 
    "accessrestrictions", "thelegalagreement", "thefinedetails", "serviceusageregulations", 
    "obligationsyouconsentto", "whatyouagreetofollow", "conditionsforaccess", 
    "serviceoperationrules", "youruserpolicy", "legalrestrictions", "mandatoryconditions", 
    "whatgovernsyouruse", "theuserframework", "conditionsofengagement", "accessterms", 
    "whatyoureboundby", "agreementyouresubjectto", "termsandrequirements", 
    "whatyousignupfor", "consumerpolicies", "termsofyouraccess", "generaltermsforservice", 
    "conditionsofmembership", "servicerulesframework", "yourobligations", 
    "servicespecificconditions", "requirementsforusers", "youruserresponsibilities", 
    "whatyoureagreeingtofollow", "policiesforengagement", "servicetermsframework", 
    "conditionsofusage", "legalstipulations", "whatgovernsyouractions", "rulesforaccess", 
    "contractualusage", "therulesyoufollow", "usagespecificrules", "servicetermsofaccess", 
    "obligatoryterms", "whatdefinestheagreement"
}



def extract_required_link(href_of_site, terms_and_conditions_alternatives, company_name
):
    for link in href_of_site:
        # print(link)
        modified_url=""
        if link:
            for char in link:
                if char == "?":
                    modified_url += "/"
                else:
                    modified_url += char
        subStr = modified_url.split("/")
        # print(subStr)
        if subStr:
            for s in subStr:
                clear_s = ""
                for i in s:
                    if i.isalpha():
                        clear_s+=i
                # print(clear_s)
                if company_name in clear_s:
                    clear_s = clear_s.replace(company_name, "")
                    # print(clear_s)

                if clear_s and clear_s in terms_and_conditions_alternatives:
                    return link
    return []                   




print(extract_required_link(["https://github.com/","https://meet.google.com/kjw-pivz-tmk","https://one.google.com/terms-of-service?hl=en_in",  "https://www.facebook.com/r.php"], terms_and_conditions_alternatives, "github"))
