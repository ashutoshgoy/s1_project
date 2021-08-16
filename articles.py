import requests
import json
import operator
def get_articles(limit):


   res={}
   page=1
   total_pages=1
   title_final=[]


   while page<=total_pages:
       apiRequest=requests.get('https://jsonmock.hackerrank.com/api/articles?page=' + str(page))
       articles=apiRequest.json()['data']



       if page==1:
         total_pages=apiRequest.json()['total_pages']

       for value in articles:

           numcomment=value['num_comments']

           title=value['title']

           storytitle=value['story_title']

           if numcomment is None:
               numcomment=0
               if title is not None:
                   res[title]=numcomment

               elif  title is None and storytitle is not None:
                   res[storytitle]=numcomment
           else:
               if title is not None:
                   res[title]=numcomment
               elif title is None and storytitle is not None:
                   res[storytitle]=numcomment


       page+=1
   # sorted_dict=   dict(sorted(res.items(),key=operator.itemgetter(1),reverse=True))
   a = [0] * (len(res))
   j = 0
   for i in res:
       a[j] = [i, res[i]]
       j += 1
   a = sorted(a, key=lambda x: x[0])
   a = sorted(a, key=lambda x: x[1],
              reverse=True)

   x=0
   for i in range(len(a)):

        if x<limit:
            title_final.append(a[i][0])
            x=x+1


   # for t in sorted_dict.keys():
   #      if x<limit:
   #       title_final.append(t)
   #       x+=1


   return title_final

print(get_articles(2))















