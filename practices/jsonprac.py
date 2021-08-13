# import json
# from pathlib import Path
# id = [{"username": "alex", "password": 'abc123'}]
# data = json.dumps(id)
# Path("practice.json").write_text(data)
import json
from pathlib import Path


# data = Path('id.json').read_text()
# id = json.loads(data)
# n = len(id)
# for i in range(n):
#     print(id[i]['username'])

author = "alex"
title = "article_1"
content = "这是alex的第一篇文章\n"
title_2 = "article_2"
content_2 = "这是alex的第二篇文章"

with open(f"{title}.json", mode="w", encoding="utf-8") as f:
    # json.dump(content, f)
    f.write(content)

# with open(f"{title_2}.json", mode="w", enconding="utf-8") as f:
#     json.dump(content_2, f)

with open("article_list.json", mode="w", encoding="utf-8") as f:
    f.write("article_1\n")
    f.write("article_2\n")


with open("article_1.json", encoding="utf-8") as f:
    content = f.read()
    print(content)


--- article
    --- article_1
    --- article_2
    --- ...
--- user
    --- alex
    --- Bob
--- article_list(file)



# article_list
Alex | article_1
Alex | article_2
Bob | artilce_3
....



vue + flask


<div class=article>
    <div class="title" >{{ title }}</div>
    <div >{{ article_content }}</div>
</div>


axois


Vue.$http = axios

this.$http.get(url).then((reponse) => {
    this.article_content = response;
})


url = "api/article/article_1"


mounted() {
    this.getArticle();
}





@bp.route("api/article/<article_name>", methods=["GET"])
def get_article(article_name):
    go
    to
    article
    fold, get
    article_name
    file,
    read
    it and
    return the
    content
    with open(article_name, "r", encoding="utf-8") as f:
        content = f.read()

    return render-template("new.html")