import sys
import re

def extract_walkthrough(html_content):
match = re.search(r’const rawWalkthroughText = `(.*?)`;’, html_content, re.DOTALL)
if not match:
print(‘ERROR: Could not find rawWalkthroughText in the input file.’, file=sys.stderr)
sys.exit(1)
return match.group(1)

def build_new_html(walkthrough_text):
return (
‘<!DOCTYPE html>\n’
‘<html lang="en">\n’
‘<head>\n’
’    <meta charset="UTF-8">\n’
’    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n’
’    <meta name="apple-mobile-web-app-capable" content="yes">\n’
’    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n’
’    <meta name="apple-mobile-web-app-title" content="Sekiro Tracker">\n’
’    <meta name="theme-color" content="#0a0a0a">\n’
’    <title>Sekiro: Shadows Die Twice - Platinum Tracker</title>\n’
’    <link rel="preconnect" href="https://fonts.googleapis.com">\n’
’    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@700;900&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">\n’
’    <style>\n’
’        :root {\n’
’            –bg: #0a0a0a;\n’
’            –surface: #141414;\n’
’            –surface-hover: #1c1c1c;\n’
’            –border: #222;\n’
’            –text: #d4d0c8;\n’
’            –text-dim: #5a5650;\n’
’            –text-checked: #3a3835;\n’
’            –accent: #8b1a1a;\n’
’            –accent-bright: #c62828;\n’
’            –accent-glow: rgba(198, 40, 40, 0.15);\n’
’            –achievement: #b8860b;\n’
’            –achievement-dim: #5c4306;\n’
’        }\n’
’        * { box-sizing: border-box; margin: 0; padding: 0; }\n’
’        body {\n’
’            font-family: “DM Sans”, -apple-system, sans-serif;\n’
’            background: var(–bg); color: var(–text);\n’
’            line-height: 1.65; min-height: 100vh;\n’
’            -webkit-text-size-adjust: 100%;\n’
’            padding-top: env(safe-area-inset-top);\n’
’        }\n’
’        header {\n’
’            position: sticky; top: 0; z-index: 100;\n’
’            background: rgba(10,10,10,0.92);\n’
’            -webkit-backdrop-filter: blur(16px);\n’
’            backdrop-filter: blur(16px);\n’
’            border-bottom: 1px solid var(–border);\n’
’            padding: 14px 16px 12px;\n’
’        }\n’
’        .hi { max-width: 860px; margin: 0 auto; }\n’
’        .tr {\n’
’            display: flex; align-items: center;\n’
’            justify-content: space-between; gap: 10px; flex-wrap: wrap;\n’
’        }\n’
’        h1 {\n’
’            font-family: “Noto Serif JP”, serif;\n’
’            font-weight: 900; font-size: 1.15em;\n’
’            letter-spacing: 0.02em;\n’
’        }\n’
’        h1 span { color: var(–accent-bright); }\n’
’        .hc { display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }\n’
’        .btn {\n’
’            font-family: “DM Sans”, sans-serif;\n’
’            font-size: 0.72em; font-weight: 600;\n’
’            padding: 6px 12px; border-radius: 4px;\n’
’            border: 1px solid var(–border);\n’
’            background: var(–surface);\n’
’            color: var(–text-dim); cursor: pointer;\n’
’            transition: all 0.15s ease; white-space: nowrap;\n’
’            -webkit-tap-highlight-color: transparent;\n’
’        }\n’
’        .btn:hover, .btn:active { background: var(–surface-hover); color: var(–text); border-color: #333; }\n’
’        .btn-a { border-color: var(–accent); color: var(–accent-bright); }\n’
’        .btn-a:hover, .btn-a:active { background: var(–accent-glow); border-color: var(–accent-bright); }\n’
’        .pr { display: flex; align-items: center; gap: 12px; margin-top: 10px; }\n’
’        .pt { flex: 1; height: 5px; background: var(–border); border-radius: 3px; overflow: hidden; }\n’
’        .pf {\n’
’            height: 100%;\n’
’            background: linear-gradient(90deg, var(–accent), var(–accent-bright));\n’
’            width: 0%; transition: width 0.4s ease; border-radius: 3px;\n’
’        }\n’
’        .pl {\n’
’            font-size: 0.78em; font-weight: 600; color: var(–text-dim);\n’
’            min-width: 100px; text-align: right; font-variant-numeric: tabular-nums;\n’
’        }\n’
’        main { max-width: 860px; margin: 0 auto; padding: 16px 16px 80px; }\n’
’        .sec {\n’
’            margin-bottom: 10px; border: 1px solid var(–border);\n’
’            border-radius: 6px; overflow: hidden; background: #0f0f0f;\n’
’        }\n’
’        .sh {\n’
’            display: flex; align-items: center; padding: 13px 14px;\n’
’            cursor: pointer; user-select: none; gap: 10px;\n’
’            transition: background 0.15s ease;\n’
’            -webkit-tap-highlight-color: transparent;\n’
’        }\n’
’        .sh:hover { background: var(–surface-hover); }\n’
’        .st {\n’
’            font-size: 0.7em; color: var(–text-dim);\n’
’            transition: transform 0.25s ease;\n’
’            flex-shrink: 0; width: 16px; text-align: center;\n’
’        }\n’
’        .sec.c .st { transform: rotate(-90deg); }\n’
’        .sn {\n’
’            font-family: “Noto Serif JP”, serif;\n’
’            font-weight: 700; font-size: 0.92em; flex: 1;\n’
’        }\n’
’        .sp {\n’
’            font-size: 0.73em; font-weight: 600; color: var(–text-dim);\n’
’            font-variant-numeric: tabular-nums;\n’
’        }\n’
’        .sp .d { color: var(–accent-bright); }\n’
’        .sb { overflow: hidden; transition: max-height 0.3s ease; }\n’
’        .sec.c .sb { max-height: 0 !important; }\n’
’        .sbi { padding: 4px 6px 6px; }\n’
’        .it {\n’
’            display: flex; align-items: flex-start; gap: 10px;\n’
’            padding: 10px; margin-bottom: 3px; border-radius: 5px;\n’
’            cursor: pointer; transition: background 0.15s ease;\n’
’            border: 1px solid transparent;\n’
’            -webkit-tap-highlight-color: transparent;\n’
’        }\n’
’        .it:hover { background: var(–surface-hover); border-color: var(–border); }\n’
’        .it.ck { opacity: 0.4; }\n’
’        .it.ck .tx {\n’
’            text-decoration: line-through; text-decoration-color: var(–text-checked);\n’
’        }\n’
’        .it input[type=“checkbox”] {\n’
’            margin-top: 3px; width: 20px; height: 20px; min-width: 20px;\n’
’            accent-color: var(–accent-bright); cursor: pointer;\n’
’        }\n’
’        .tx { flex: 1; font-size: 0.88em; white-space: pre-wrap; line-height: 1.6; }\n’
’        .it.ac {\n’
’            border-left: 3px solid var(–achievement-dim);\n’
’            background: rgba(184,134,11,0.03);\n’
’        }\n’
’        .it.ac:hover { background: rgba(184,134,11,0.06); }\n’
’        .it.ac .tx { color: var(–achievement); }\n’
’        .it.ac.ck .tx { color: var(–achievement-dim); }\n’
’        #sb {\n’
’            position: fixed; bottom: 20px; right: 20px;\n’
’            width: 42px; height: 42px; border-radius: 50%;\n’
’            background: var(–surface); border: 1px solid var(–border);\n’
’            color: var(–text-dim); font-size: 1.3em; cursor: pointer;\n’
’            display: none; align-items: center; justify-content: center;\n’
’            transition: all 0.15s ease; z-index: 50;\n’
’        }\n’
’        #sb:hover { background: var(–surface-hover); color: var(–text); }\n’
’        #sb.v { display: flex; }\n’
’        .ov {\n’
’            position: fixed; inset: 0; background: rgba(0,0,0,0.75);\n’
’            z-index: 200; display: none; align-items: center; justify-content: center;\n’
’        }\n’
’        .ov.o { display: flex; }\n’
’        .dl {\n’
’            background: var(–surface); border: 1px solid var(–border);\n’
’            border-radius: 8px; padding: 24px; max-width: 340px; width: 88%; text-align: center;\n’
’        }\n’
’        .dl h3 { font-family: “Noto Serif JP”, serif; margin-bottom: 8px; color: var(–accent-bright); }\n’
’        .dl p { font-size: 0.85em; color: var(–text-dim); margin-bottom: 18px; }\n’
’        .db { display: flex; gap: 8px; justify-content: center; }\n’
’        .dl .btn { padding: 8px 20px; font-size: 0.8em; }\n’
’        @media (max-width: 600px) {\n’
’            header { padding: 12px 12px 10px; }\n’
’            h1 { font-size: 0.95em; }\n’
’            .btn { padding: 5px 10px; font-size: 0.68em; }\n’
’            main { padding: 12px 8px 60px; }\n’
’            .it { padding: 9px 7px; gap: 8px; }\n’
’            .tx { font-size: 0.84em; }\n’
’            .pl { min-width: 75px; font-size: 0.7em; }\n’
’        }\n’
’    </style>\n’
‘</head>\n’
‘<body>\n’
‘<header><div class="hi">\n’
’    <div class="tr">\n’
’        <h1>影 <span>Sekiro</span> Tracker</h1>\n’
’        <div class="hc">\n’
’            <button class="btn btn-a" id="br">▶ Resume</button>\n’
’            <button class="btn" id="be">Expand</button>\n’
’            <button class="btn" id="bc">Collapse</button>\n’
’            <button class="btn" id="bx">Reset</button>\n’
’        </div>\n’
’    </div>\n’
’    <div class="pr">\n’
’        <div class="pt"><div class="pf" id="pf"></div></div>\n’
’        <div class="pl" id="pl">0%</div>\n’
’    </div>\n’
‘</div></header>\n’
‘<main id="cl"></main>\n’
‘<button id="sb">↑</button>\n’
‘<div class="ov" id="ro"><div class="dl">\n’
’    <h3>Reset Progress?</h3>\n’
’    <p>This will uncheck every step. This cannot be undone.</p>\n’
’    <div class="db">\n’
’        <button class="btn" id="rc">Cancel</button>\n’
’        <button class="btn btn-a" id="ry">Reset</button>\n’
’    </div>\n’
‘</div></div>\n’
‘<script>\n’
‘const rawWalkthroughText = `' + walkthrough_text + '`;\n’
‘\n’
‘const SD=[\n’
’    [“Part 1:”,“Part 1: Wolf and the Divine Heir”],\n’
’    [“Part 2:”,“Part 2: Ashina Outskirts & Hirata Estate”],\n’
’    [“Part 3:”,“Part 3: Ashina Castle”],\n’
’    [“Part 4:”,“Part 4: Senpou Temple: Mt. Kongo”],\n’
’    [“Part 5:”,“Part 5: Sunken Valley & Ashina Depths”],\n’
’    [“Part 6:”,“Part 6: Ashina Castle Revisited”],\n’
’    [“Part 7:”,“Part 7: Fountainhead Palace”],\n’
’    [“Part 8:”,“Part 8: Ashina Castle Re-revisited”],\n’
’    [“Subsequent Playthroughs”,“Subsequent Playthroughs”]\n’
‘];\n’
‘const AP=[/Defeated\s*”/,/Acquired\s*(the|all)\s*/,/Attained\s*the\s*”/,/Caught\s*the/,/Encountered\s*the/,/Received\s*the\s*”/,/Traveled\s*to\s*all/,/Used\s*(the\s*Mortal|Lapis)/,/Fully\s*upgraded/,/Upgraded\s*(Vitality|all\s*Prosthetic)/,/Grasped\s*the\s*inner/,/All\s*achievements\s*have/,/^\d+\s*guide/,/^Collectable\s*-/,/^Story\s*Completed/];\n’
‘function isA(t){return AP.some(p=>p.test(t))}\n’
’const ch=rawWalkthroughText.split(/\n\s*\n/).map(c=>c.trim()).filter(c=>c.length>0);\n’
‘const secs=[];let cur={t:“Introduction”,c:[]};\n’
‘ch.forEach(k=>{const m=SD.find(s=>k.startsWith(s[0]));if(m){if(cur.c.length>0)secs.push(cur);cur={t:m[1],c:[]}}else cur.c.push(k)});\n’
‘if(cur.c.length>0)secs.push(cur);\n’
“let pr=JSON.parse(localStorage.getItem(‘sekiroTrackerData’)||’{}’);\n”
“const cl=document.getElementById(‘cl’),pf=document.getElementById(‘pf’),pl=document.getElementById(‘pl’);\n”
‘let gi=0;const all=[],se=[];\n’
‘function render(){\n’
“cl.innerHTML=’’;gi=0;all.length=0;se.length=0;\n”
‘secs.forEach((s,si)=>{\n’
“const sd=document.createElement(‘div’);sd.className=‘sec’;\n”
“const hd=document.createElement(‘div’);hd.className=‘sh’;\n”
“const tg=document.createElement(‘span’);tg.className=‘st’;tg.textContent=’\u25BC’;\n”
“const nm=document.createElement(‘span’);nm.className=‘sn’;nm.textContent=s.t;\n”
“const pg=document.createElement(‘span’);pg.className=‘sp’;pg.id=‘p’+si;\n”
‘hd.append(tg,nm,pg);\n’
“const bd=document.createElement(‘div’);bd.className=‘sb’;\n”
“const bi=document.createElement(‘div’);bi.className=‘sbi’;\n”
‘const sc=[];\n’
‘s.c.forEach(k=>{\n’
‘const i=gi++;const ck=!!pr[i];const ac=isA(k);\n’
“const it=document.createElement(‘div’);\n”
“it.className=‘it’+(ck?’ ck’:’’)+(ac?’ ac’:’’);it.dataset.i=i;\n”
“const cb=document.createElement(‘input’);cb.type=‘checkbox’;cb.checked=ck;\n”
“const tx=document.createElement(‘div’);tx.className=‘tx’;tx.textContent=k;\n”
“it.addEventListener(‘click’,e=>{\n”
‘if(e.target!==cb)cb.checked=!cb.checked;\n’
“pr[i]=cb.checked;it.classList.toggle(‘ck’,cb.checked);\n”
“localStorage.setItem(‘sekiroTrackerData’,JSON.stringify(pr));up()});\n”
‘it.append(cb,tx);bi.appendChild(it);all.push({cb,it,si});sc.push(cb)});\n’
‘bd.appendChild(bi);\n’
“hd.addEventListener(‘click’,()=>{\n”
“const c=sd.classList.toggle(‘c’);if(!c)bd.style.maxHeight=bd.scrollHeight+‘px’});\n”
‘sd.append(hd,bd);cl.appendChild(sd);se.push({d:sd,b:bd,s:sc,p:pg})});\n’
“requestAnimationFrame(()=>se.forEach(s=>{s.b.style.maxHeight=s.b.scrollHeight+‘px’}));up()}\n”
‘function up(){\n’
‘let t=all.length,c=0;all.forEach(({cb})=>{if(cb.checked)c++});\n’
“const p=t===0?0:Math.round(c/t*100);\n”
“pf.style.width=p+’%’;pl.textContent=p+’% \u2014 ‘+c+’/’+t;\n”
‘se.forEach(s=>{let st=s.s.length,sc=0;s.s.forEach(cb=>{if(cb.checked)sc++});\n’
“s.p.innerHTML=sc===st?’<span class="d">\u2713 ‘+st+’/’+st+’</span>’:sc+’/’+st})}\n”
“document.getElementById(‘br’).addEventListener(‘click’,()=>{\n”
‘const f=all.find(({cb})=>!cb.checked);if(f){\n’
“const s=se[f.si];s.d.classList.remove(‘c’);s.b.style.maxHeight=s.b.scrollHeight+‘px’;\n”
“setTimeout(()=>{f.it.scrollIntoView({behavior:‘smooth’,block:‘center’});\n”
“f.it.style.outline=‘2px solid var(–accent-bright)’;\n”
“setTimeout(()=>f.it.style.outline=’’,2000)},150)}});\n”
“document.getElementById(‘be’).addEventListener(‘click’,()=>se.forEach(s=>{s.d.classList.remove(‘c’);s.b.style.maxHeight=s.b.scrollHeight+‘px’}));\n”
“document.getElementById(‘bc’).addEventListener(‘click’,()=>se.forEach(s=>s.d.classList.add(‘c’)));\n”
“document.getElementById(‘bx’).addEventListener(‘click’,()=>document.getElementById(‘ro’).classList.add(‘o’));\n”
“document.getElementById(‘rc’).addEventListener(‘click’,()=>document.getElementById(‘ro’).classList.remove(‘o’));\n”
“document.getElementById(‘ry’).addEventListener(‘click’,()=>{\n”
“document.getElementById(‘ro’).classList.remove(‘o’);\n”
“pr={};localStorage.setItem(‘sekiroTrackerData’,JSON.stringify(pr));\n”
“all.forEach(({cb,it})=>{cb.checked=false;it.classList.remove(‘ck’)});up()});\n”
“const sb=document.getElementById(‘sb’);\n”
“window.addEventListener(‘scroll’,()=>sb.classList.toggle(‘v’,window.scrollY>500));\n”
“sb.addEventListener(‘click’,()=>window.scrollTo({top:0,behavior:‘smooth’}));\n”
‘render();\n’
‘</script>\n’
‘</body>\n’
‘</html>’
)

def main():
if len(sys.argv) < 2:
print(‘Usage: python3 upgrade_tracker.py <input.html> [–output <output.html>]’, file=sys.stderr)
sys.exit(1)
input_file = sys.argv[1]
output_file = None
if ‘–output’ in sys.argv:
idx = sys.argv.index(’–output’)
if idx + 1 < len(sys.argv):
output_file = sys.argv[idx + 1]
with open(input_file, ‘r’, encoding=‘utf-8’) as f:
original_html = f.read()
walkthrough = extract_walkthrough(original_html)
new_html = build_new_html(walkthrough)
if output_file:
with open(output_file, ‘w’, encoding=‘utf-8’) as f:
f.write(new_html)
print(’Done: wrote improved tracker to ’ + output_file, file=sys.stderr)
else:
print(new_html)

if **name** == ‘**main**’:
main()
