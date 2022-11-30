import markdown
import os

posts = os.listdir("posts")
posts.sort()
posts.reverse()

posts = list(filter(lambda x: "~" not in x, posts))

def read_file(path):
    with open(path) as f:
        return f.read()

page = []

markdown_posts = []

for post in posts:
    markdown_posts.append(markdown.markdown(read_file(f"posts/{post}")))

page.append(read_file("template/pre.html"))

for post in markdown_posts:
    page.append("<article class=\"textretty\">")
    page.append(post)
    page.append("</article><hr/>")

page.append(read_file("template/post.html"))

with open("index.html", "w") as f:
    f.write("\n".join(page))

print("\n".join(page))
        #markdown.
