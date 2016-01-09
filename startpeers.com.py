#405

likes = open("test.txt","r")

line = likes.readline()
while line:

    #line = line[86:92]
    print('<p> <a href="https://startpeeps.com/request.php?t=post&post_id='+line+'&a=like">'+line+'</a></p>')
    line = likes.readline()

likes.close()

## <a href="URL">...</a>


# f = open('power.txt')
# line = f.readline()
# while line:
#     print (line),
#     line = f.readline()
# f.close()
