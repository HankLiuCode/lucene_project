import pysolr
from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html',locals())
    #result就是回傳的結果
    
def searchpage(request):
    result=''
    if(request.POST):
        query = request.POST['query'] #輸入的query用這個存
        solr = pysolr.Solr('http://140.119.19.23:8983/solr/demo/',timeout=10)

        results = solr.search('title:' + query)
        result = results.docs
        for r in results:
            r['url']=r['url'][0]
    return render(request,'search.html',locals())