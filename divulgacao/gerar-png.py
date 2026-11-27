#!/usr/bin/env python3
"""Gera os PNGs de divulgação a partir do header do site.

Uso (na pasta do projeto):   python3 divulgacao/gerar-png.py
Requisitos: Google Chrome ou Chromium instalado e internet (para carregar as fontes).
Saída: divulgacao/forkxx-1080p-horizontal.png, forkxx-youtube-quadrado.png, forkxx-stories-vertical.png
(e as versões em inglês com sufixo -en). Também gera as imagens de agradecimento da nuvem de apoiadores: forkxx-obrigado-*.png. O botão "Imagens de divulgação" no rodapé do site baixa esses arquivos.
Os valores vêm de data.json, então rode de novo sempre que atualizar as doações.
Também dá para abrir index.html?export=wide|square|story no navegador e tirar print.
"""
import os, shutil, subprocess, sys, threading, http.server, socketserver, functools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "divulgacao")
FORMATOS = [("wide", 1920, 1080, "forkxx-1080p-horizontal"),
            ("square", 1080, 1080, "forkxx-youtube-quadrado"),
            ("story", 1080, 1920, "forkxx-stories-vertical")]
# imagens de agradecimento (nuvem de apoiadores): mesma página com &view=thanks
ALVOS = [(f, w, h, n, "") for f, w, h, n in FORMATOS] + \
        [(f, w, h, n.replace("forkxx-", "forkxx-obrigado-"), "&view=thanks") for f, w, h, n in FORMATOS]
CANDIDATOS = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]

def achar_chrome():
    for c in CANDIDATOS:
        p = shutil.which(c) or (c if os.path.exists(c) else None)
        if p: return p
    sys.exit("Chrome/Chromium não encontrado. Instale o Google Chrome e tente de novo.")

def main():
    chrome = achar_chrome()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    handler.log_message = lambda *a, **k: None
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    porta = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    for pagina, suf in (("index.html", ""), ("en.html", "-en")):
      for fmt, w, h, nome, extra in ALVOS:
        saida = os.path.join(OUT, nome + suf + ".png")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-sandbox",
               "--force-prefers-reduced-motion", f"--window-size={w},{h}", "--virtual-time-budget=9000",
               f"--screenshot={saida}", f"http://127.0.0.1:{porta}/{pagina}?export={fmt}{extra}"]
        for tentativa in range(3):  # o Chrome headless às vezes trava; tenta de novo
            try:
                subprocess.run(cmd, check=True, timeout=40, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                break
            except subprocess.TimeoutExpired:
                if tentativa == 2: raise
        print("ok", saida)
    srv.shutdown()

if __name__ == "__main__":
    main()
