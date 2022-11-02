from BeautifulSoup4.bs4 import BeautifulSoup #I had to clone beautifulsoup4 in my folder directory because either pip is being weird. Alternatively try "from bs4." 
import mechanize, http.cookiejar as baking


def anon_link_fetch(url, userAgent, proxy): 
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False) 
    br.set_proxies(proxy)
    br.addheaders = userAgent
    soup = BeautifulSoup(br.open(url), "html5lib") 
    for links in soup.find_all("a"): 
        print(links.get('href'))
        
    #print(soup.prettify())
    #baking.CookieJar.clear_all_session_cookies()
        

#Set default values for future arguments
fetch_url = "https://www.capella.edu"
#testing multiple proxies
#proxy_is_set = {'http':'216.155.139.115:3128'}
proxy_is_set = {'http':'142.4.203.248'}
userAgent_is_set = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')]


#user input concerning url address, proxy address, and user agent string
'''
parameter_alteration_request = input("Would you like to alter these default parameters? \n\n URL: " \
                                     + fetch_url + " \n proxy IP address: " + proxy_is_set["https"] + " \n UserAgent:"\
                                     + userAgent_is_set[0][1] + "\nEnter 'y' or 'Y' for 'yes' \n Any other key for  'no'\n\n")



if parameter_alteration_request == 'y' or parameter_alteration_request == 'Y':
    alter_url = input("Would you like to alter this URL? \n" + fetch_url + "\nEnter 'y' or 'Y' for 'yes' \n Any other key for  'no'\n\n")
    if alter_url == 'y' or alter_url == 'Y':
        fetch_url = input("Please insert the new URL address: \n\n")
    alter_proxy = input("Would you like to alter this proxy address? \n" + proxy_is_set["https"] + "\nEnter 'y' or 'Y' for 'yes' \n Any other key for  'no'\n\n")
    if alter_proxy == 'y' or alter_proxy == 'Y':
        proxy_is_set = input("Please insert the new proxy address: \n\n")
    alter_userAgent = input("Would you like to alter this user agent string? \n" + userAgent_is_set[0][1] + "\nEnter 'y' or 'Y' for 'yes' \n any other key for  'no'\n\n")
    if alter_userAgent == 'y' or alter_userAgent == 'Y':
        fetch_url = input("Please insert the new URL address: \n\n")
else:

    print("Function shall run with default arguments, \n Fetching university web links: \n")
'''
#executes the function with the desired arguments
anon_link_fetch(fetch_url, userAgent_is_set, proxy_is_set)
    