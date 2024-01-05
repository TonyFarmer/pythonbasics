import requests
import lxml.html

html = """<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>"""

tree = lxml.html.document_fromstring(html) #Создаем объект дерева

title = tree.xpath("/html/body/tag1/tag2/text()")[0] #Получаем нужный объект по его xpath. В конце стоит text(), чтобы получить текст

print(title)