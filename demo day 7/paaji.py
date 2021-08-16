
words="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapien, eget aliquam turpis urna at quam. Sed a&eros vel@ ante vestibulum vulputate. Suspendisse vitae vulputate velit. Suspendisse! ligula nisl, semper ut sodales et, ultricies porttitor felis. Nunc ac mattis erat, aliquet pretium risus"
res=""
for word in words:
      if word.isalnum() or word==" ":
         res+=word

final=[]
for i  in res.split():
     if res.split().count(i)<3 and i not in final:
         final.append(i)

print(final[-20:])
