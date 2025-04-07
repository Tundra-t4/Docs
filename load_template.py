import json
import os, os.path
import shutil
import sys
from pathlib import Path
menu = {}
try:
    rooturl = sys.argv[1]
except IndexError:
    rooturl = "/"
# <span class="sl-badge default small sidebar-icon-filled astro-daoe2ojf astro-nmkt7c5c"></span>  <- icon
menu["heading"] = """<ul class="top-level astro-daoe2ojf"> <li class="astro-daoe2ojf"> <details open="" class="astro-daoe2ojf"> <sl-sidebar-restore data-index="0"></sl-sidebar-restore> <summary class="astro-daoe2ojf"> <div class="group-label astro-daoe2ojf" bis_skin_checked="1"> <span class="large astro-daoe2ojf">{{Heading}}</span>"""
menu["svg_icon"] = """</div> <svg aria-hidden="true" class="caret astro-daoe2ojf astro-6ssdnj4h" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1.25rem;"><path d="{{svg_data}}"></path></svg>  </summary>"""
menu["first_entry"] = """<ul class="astro-daoe2ojf">"""
menu["selected_entry"] = """<li class="astro-daoe2ojf"> <a href=" """ + rooturl + """{{url_path}}" aria-current="page" class="astro-daoe2ojf"> <span class="astro-daoe2ojf">{{entry_name}}</span>  </a> </li>"""
menu["entry"] = """<li class="astro-daoe2ojf"> <a href=""" + rooturl + """{{url_path}}" aria-current="false" class="astro-daoe2ojf"> <span class="astro-daoe2ojf">{{entry_name}}</span>  </a> </li>"""
menu["header_ending"] = """</ul></ul>"""
menu["ending"] = """</details> </li> </ul>   <script aria-hidden="true">"""
content = {}
content["content_begin"] = """<div class="main-frame astro-tltpxb55" bis_skin_checked="1">  <script type="module">const a=document.getElementById("starlight__sidebar"),n=a?.querySelector("sl-sidebar-state-persist"),o="sl-sidebar-state",i=()=>{let t=[];const e=n?.dataset.hash||"";try{const s=sessionStorage.getItem(o),r=JSON.parse(s||"{}");Array.isArray(r.open)&&r.hash===e&&(t=r.open)}catch{}return{hash:e,open:t,scroll:a?.scrollTop||0}},c=t=>{try{sessionStorage.setItem(o,JSON.stringify(t))}catch{}},d=()=>c(i()),l=(t,e)=>{const s=i();s.open[e]=t,c(s)};n?.addEventListener("click",t=>{if(!(t.target instanceof Element))return;const e=t.target.closest("summary")?.closest("details");if(!e)return;const s=e.querySelector("sl-sidebar-restore"),r=parseInt(s?.dataset.index||"");isNaN(r)||l(!e.open,r)});addEventListener("visibilitychange",()=>{document.visibilityState==="hidden"&&d()});addEventListener("pageHide",d);</script> <div class="lg:sl-flex astro-5ki2okcc" bis_skin_checked="1"> <aside class="right-sidebar-container astro-5ki2okcc"> <div class="right-sidebar astro-5ki2okcc" bis_skin_checked="1"> <div class="lg:sl-hidden astro-vrlflj22" bis_skin_checked="1"><mobile-starlight-toc data-min-h="2" data-max-h="3" class="astro-mblf5lc3"><nav aria-labelledby="starlight__on-this-page--mobile" class="astro-mblf5lc3"><details id="starlight__mobile-toc" class="astro-mblf5lc3"><summary id="starlight__on-this-page--mobile" class="sl-flex astro-mblf5lc3"><div class="toggle sl-flex astro-mblf5lc3" bis_skin_checked="1">On this page<svg aria-hidden="true" class="caret astro-mblf5lc3 astro-6ssdnj4h" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="--sl-icon-size: 1rem;"><path d="m14.83 11.29-4.24-4.24a1 1 0 1 0-1.42 1.41L12.71 12l-3.54 3.54a1 1 0 0 0 0 1.41 1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l4.24-4.24a1.002 1.002 0 0 0 0-1.42Z"></path></svg> </div><span class="display-current astro-mblf5lc3"> {{content_heading}} </span></summary><div class="dropdown astro-mblf5lc3" bis_skin_checked="1"><ul class="isMobile astro-pkxw3w4h" style="--depth: 0;"> <li class="astro-pkxw3w4h" style="--depth: 0;"> <a href="#_top" class="astro-pkxw3w4h" style="--depth: 0;" aria-current="true"> <span class="astro-pkxw3w4h" style="--depth: 0;">{{content_heading}}</span> </a>  </li> </ul> </div></details></nav></mobile-starlight-toc><script type="module" src=" """ + rooturl + """_astro/MobileTableOfContents.astro_astro_type_script_index_0_lang.C181hMzK.js"></script></div><div class="right-sidebar-panel sl-hidden lg:sl-block astro-vrlflj22" bis_skin_checked="1"><div class="sl-container astro-vrlflj22" bis_skin_checked="1"><starlight-toc data-min-h="2" data-max-h="3"><nav aria-labelledby="starlight__on-this-page"><h2 id="starlight__on-this-page">On this page</h2><ul class="astro-pkxw3w4h" style="--depth: 0;"> <li class="astro-pkxw3w4h" style="--depth: 0;"> <a href="#_top" class="astro-pkxw3w4h" style="--depth: 0;" aria-current="true"> <span class="astro-pkxw3w4h" style="--depth: 0;">{{content_heading}}</span> </a>  </li> </ul> </nav></starlight-toc><script type="module" src=" """ + rooturl + """_astro/TableOfContents.astro_astro_type_script_index_0_lang.CKWWgpjV.js"></script></div></div> </div> </aside> <div class="main-pane astro-5ki2okcc" bis_skin_checked="1">  <main data-pagefind-body="" class="astro-zhmbqftb" lang="en" dir="ltr">    <div class="content-panel astro-xfeoyhqm" bis_skin_checked="1"> <div class="sl-container astro-xfeoyhqm" bis_skin_checked="1"> <h1 id="_top" class="astro-ddidmlph">{{content_heading}}</h1>  </div> </div>  <div class="content-panel astro-xfeoyhqm" bis_skin_checked="1"> <div class="sl-container astro-xfeoyhqm" bis_skin_checked="1"> <div class="sl-markdown-content" bis_skin_checked="1">"""
content["para_begin"] = """<p>"""
content["para_end"] = """</p>"""
content["bold_begin"] = """<strong>"""
content["bold_end"] = """</strong>"""
content["url_text"] = """<a href="{{url}}">{{text}}</a>"""
content["url_begin"] = content["url_text"].split("{{url}}")[0]
content["url_end"] = "\">"
content["url_text_end"] = "</a>"
content["code_content"] = """<div class="expressive-code" bis_skin_checked="1"><link rel="stylesheet" href=" """ + rooturl + """_astro/ec.x0ykv.css"><script type="module" src=" """ + rooturl + """_astro/ec.8zarh.js"></script><figure class="frame not-content"><figcaption class="header"></figcaption><pre data-language="tundra"><code><div class="ec-line" bis_skin_checked="1"><div class="code" bis_skin_checked="1"><span style="--0:#FFFFFF">{{code_content}}</span></div></div></code></pre><div class="copy" bis_skin_checked="1"><button title="Copy to clipboard" data-copied="Copied!" data-code="{{copy_content}}"><div bis_skin_checked="1"></div></button></div></figure></div>"""
content["code_begin"] = content["code_content"].split("{{code_content}}")[0]
content["code_end"] = content["code_content"].split("{{code_content}}")[1]
content["content_end"] = """</div>"""


menu_data = json.load(open("headings.json"))
setting_data = {}
to_del = []
for m in menu_data:
    if m.startswith("__"):
        setting_data[m.replace("__","")] = menu_data[m]
        to_del.append(m)
for td in to_del:
    del menu_data[td]


    
def generate_doc_page(whoami,first=False):
    tmpl = open(sys.argv[0].replace("load_template.py","") + "tmpl8.html").read()
    menu_construct = ""
    outpath = ""

    gen_path = ""
    to_mkdir = ""

    for heading in menu_data:

        menu_construct += menu["heading"].replace("{{Heading}}",heading)
        menu_construct += menu["svg_icon"].replace("{{svg_data}}","{{" + heading + "_svg_data" + "}}")
        menu_construct += menu["first_entry"]
        for entry in menu_data[heading]:
            if (entry[0] == "__svg"):

                menu_construct = menu_construct.replace("{{" + heading + "_svg_data" + "}}",entry[1])
                pass
            
            elif (entry[0] == "__internal_name"):
                to_mkdir = entry[1]
                try:
                    os.mkdir("build/" + to_mkdir + "/")
                except FileExistsError:
                    pass
                pass
            
            elif entry[0] == whoami:
                gen_path = entry[2]
                outpath = entry[1]
                menu_construct += menu["selected_entry"].replace("{{entry_name}}",entry[0]).replace("{{url_path}}",entry[1])
            else:
                menu_construct += menu["entry"].replace("{{entry_name}}",entry[0]).replace("{{url_path}}",entry[1])
        menu_construct += menu["header_ending"]
    menu_construct += menu["ending"]
    tmpl = tmpl.replace("{{menu}}",menu_construct)





    whoami_data = json.load(open(os.getcwd() + "/entries/" + gen_path))

    content_data = open(os.getcwd() + "/entry_data/" + whoami_data["Content"]).read()

    replace_rules = {
        "<para>":"para_begin",
        "</para>": "para_end",
        "<bold>": "bold_begin",
        "</bold>": "bold_end",
        "<code>": "code_begin",
        "</code>": "code_end",
        "<url>": "url_begin",
        "<urltext>": "url_end",
        "</url>": "url_text_end",
    }

    for rep in replace_rules:
        content_data = content_data.replace(rep,content[replace_rules[rep]])
    content_data = content["content_begin"] + content_data + content["content_end"]
    content_data = content_data.replace("\n","<br>") #+ "</span>"
    content_data = content_data.replace("{{content_heading}}",whoami_data["Title"])


    tmpl = tmpl.replace("{{content}}",content_data)
    tmpl = tmpl.replace("{{last_updated}}",whoami_data["Edited On"])
    tmpl = tmpl.replace("{{title}}",whoami_data["Title"])
    tmpl = tmpl.replace("{{content_heading}}",whoami_data["Title"])
    tmpl = tmpl.replace("{{documentation_name}}",setting_data["docsname"])
    next_name = ""
    next_url = ""
    f = False
    f2 = False
    for h in menu_data:
        for v in menu_data[h]:
            if v[0].startswith("__") == False:
                print("-----")
                print(v[0])
                print(whoami)
                print(f)
                print("-----")

                if f:
                    next_name = v[0]
                    next_url = v[1]
                    f2 = True
                    break
                if v[0] == whoami:
                    f = True
        if f2:
            break
        


    tmpl = tmpl.replace("{{next_name}}",next_name)
    tmpl = tmpl.replace("{{next_url}}",next_url)
    if "git" in setting_data.keys():
        tmpl = tmpl.replace("{{github_repo}}",setting_data["git"])
    if "discord" in setting_data.keys():
        tmpl = tmpl.replace("{{discord_url}}",setting_data["discord"])

    tmpl = tmpl.replace("{{rooturl}}",rooturl)

    if first:
        open("build/index.html","w+").write(f"""<script>window.location.replace("{outpath}");</script>""")
    open("build/" + outpath,"w+").write(tmpl)
    return setting_data["docsname"]


if Path(os.getcwd() + "/build/").is_dir():
    print("Removing old build")
    shutil.rmtree(os.getcwd() + "/build/")
print("Beginning build")
os.mkdir(os.getcwd() + "/build/")

name = ""
first = True
for h in menu_data:
    for e in menu_data[h]:
        if e[0].startswith("__") == False:


            print("Building - " + e[0])
            name = generate_doc_page(e[0], first)
            print("Built - " + e[0])
            if first:
                first = False

print("Adding astro assets")
shutil.copytree(sys.argv[0].replace("load_template.py","") + "_astro/",os.getcwd() + "/build/_astro/")
shutil.copytree(sys.argv[0].replace("load_template.py","") + "pagefind/",os.getcwd() + "/build/pagefind/")
print("Adding fonts")
shutil.copytree(sys.argv[0].replace("load_template.py","") + "fonts/",os.getcwd() + "/build/fonts/")
print("Zipping it up!")
shutil.make_archive(name + "-build","gztar",os.getcwd() + "/build/")
