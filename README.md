# LAN Website Scanner

This is a Python tool that scans your local network ( for example: `192.168.2.x`) for active websites. It detects web interfaces running on common ports (HTTP 80, HTTPS 443) and automatically opens the live ones in your default browser.

---

## Use Cases

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
