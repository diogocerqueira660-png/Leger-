import json, re
from PIL import Image, ImageDraw
src=open('src/app.html',encoding='utf-8').read()
head='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Léger">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#F2F4F7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1118" media="(prefers-color-scheme: dark)">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" href="icons/icon-192.png">
<style>[hidden]{display:none!important}img{max-width:100%}</style>
</head>
<body>
'''
open('index.html','w',encoding='utf-8').write(head+src+'\n</body>\n</html>\n')
json.dump({"name":"Léger – suivi minceur","short_name":"Léger","lang":"fr","start_url":"./","scope":"./","display":"standalone","background_color":"#F2F4F7","theme_color":"#F2F4F7",
 "icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},
 open('manifest.webmanifest','w',encoding='utf-8'),ensure_ascii=False,indent=1)
open('sw.js','w').write('''const C='leger-v1';const CORE=['./','index.html','manifest.webmanifest','icons/icon-192.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET'||u.origin!==location.origin)return;
 e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))))});
''')
import os; os.makedirs('icons',exist_ok=True)
def icon(size,path,pad=0):
    S=size*4; im=Image.new('RGB',(S,S),(19,26,38)); d=ImageDraw.Draw(im)
    c=S/2; R=S*0.30; w=S*0.085
    box=[c-R,c-R,c+R,c+R]
    d.arc(box,0,360,fill=(42,51,68),width=int(w))
    d.arc(box,-90,-90+223,fill=(233,90,48),width=int(w))
    d.arc(box,-90+223+12,270-12,fill=(15,154,130),width=int(w))
    im.resize((size,size),Image.LANCZOS).save(path)
icon(512,'icons/icon-512.png');icon(192,'icons/icon-192.png');icon(180,'icons/apple-touch-icon.png')
print('ok')
