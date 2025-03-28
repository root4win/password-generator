import requests as r
import bs4
import argparse
import re
import secrets

def get_raw_content(url:str) -> list:
    response = r.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        clean_txt = re.findall(r'\b[A-Za-z]{5,}\b', text)
        return clean_txt
    return []
    

def generate_passwords(words:list, num_words=200, separator="\n", add_numbers=True):
    selected_words = [secrets.choice(words).capitalize() for _ in range(num_words)] 
    password = separator.join(selected_words)
    if add_numbers:
        password += str(secrets.randbelow(10000))
    return password
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Extract URLs")
    parser.add_argument("-url", required=True, help="URL to extract")
    
    args = parser.parse_args()
    url = args.url
    
    words = get_raw_content(url)
    if words:
        passwords = generate_passwords(words)
        with open("password.txt", "w") as f:
            f.write(passwords)
            f.close()
    print("[+] Passwords generated successfully!")
