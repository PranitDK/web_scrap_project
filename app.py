from bs4 import BeautifulSoup 
import requests 
from flask import Flask ,render_template,request
app=Flask(__name__)
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
@app.route('/', methods=['GET', 'POST'])
def main():
    # url='https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage'
    if request.method == 'GET':
        url = request.args.get('url')

        def get_tittle(url):
            try:
                response=requests.get(url,headers=HEADERS)
                response.raise_for_status()
                soup=BeautifulSoup(response.content,'html.parser')
                headline=soup.find('h1')
                if headline:
                    return headline.text.strip()
                else:
                    print('Headline not found')
            except requests.exceptions.RequestException as e:
                print(f'An error occurred:{e}')
                
                
        def get_content(url):
            try:
                response=requests.get(url,headers=HEADERS)
                response.raise_for_status()
                soup=BeautifulSoup(response.content,'html.parser')
                content=soup.find_all('p')
                
                x=''
                for i in content:
        #             print(i.text)
                    x= x +''.join(i.text.strip())
                if x:
                    return x
                else:
                    print('content not found')
                    
            except requests.exceptions.RequestException as e:
                print(f'An error occurred: {e}')
        tittle = get_tittle(url)
        # print("tittle:", tittle)
                
        content = get_content(url)
        # print("content:", content)

        return render_template('template.html', title=tittle, content=content)
    return render_template('template.html')
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


