# 🕵️‍♂️ WebSniff – LAN Website Scanner

**WebSniff** is a fast, lightweight Python tool that scans your local network (`192.168.2.x`) for active websites. It detects web interfaces running on common ports (HTTP 80, HTTPS 443) and automatically opens the live ones in your default browser.

---

## 🚀 Features

- ⚡ Fast multithreaded scanning
- 🌐 Detects both HTTP and HTTPS services
- 🔒 Ignores SSL warnings (self-signed certs? no problem)
- 🧭 Automatically opens found websites
- 🛠️ Built with Python 3 + `requests`

---

## 🔧 Use Cases

- Find web interfaces of devices like:
  - Routers, Raspberry Pis, ESP32s
  - Local dev servers or IoT dashboards
- Test websites across devices on your LAN
- Quickly discover reachable admin panels or UI endpoints

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/websniff.git
cd websniff
