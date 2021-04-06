

#captures datetime object.
def format_date(date):
    #converts date to string
    return date.strftime("%m/%d/%y")

#cleans up url to only domain name.
def format_url(url):
    return url.replace("http://", "").replace("https://", "").replace("www.", "").split("/")[0].split("?")[0]

#handles prural, if greater than 1 then adds "s"
def format_plural(amount, word):
    if amount != 1:
        return word + "s"
    
    return word

