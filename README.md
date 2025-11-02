# README.md
# CUPS + Avahi AirPrint Bridge for Home Assistant


This add‑on turns **any CUPS‑compatible printer** on your LAN into an **AirPrint** printer discoverable by iOS/iPadOS/macOS.


## Features
- **Ingress support**: Manage CUPS securely inside the HA UI (no direct port needed)
- CUPS print server with optional web UI on **http://<HA-IP>:631** (if you keep the port open)
- Avahi mDNS broadcaster for native **AirPrint** discovery
- Auto‑generates Avahi service files for each **shared** CUPS queue
- Persists configuration in `/data/cups`; optional vendor PPDs in `/data/ppd`
- Broad driver set preinstalled: **Gutenprint, HPLIP, brlaser (Brother), ESC/P-R (Epson), Ricoh PPDs, Foomatic**


## Install
1. In *Settings → Add‑ons → Add-on Store*, click **⋮ → Repositories**, add your repo URL.
2. Install **CUPS AirPrint Bridge**.
3. Open the add‑on, set **Admin user/password**, and **Start**.
4. Open via **Ingress** ("Open Web UI" button), or go to `http://<HA-IP>:631` if you left port 631 exposed.
5. In CUPS Administration → **Add Printer** and add your network/USB printer. Check **Share This Printer**.
6. On an iPhone/iPad/Mac, open the print dialog. Your printer should appear automatically as *AirPrint*.


## Options
- `admin_user` / `admin_password`: CUPS admin credentials.
- `share_printers`: If true, printers are shared by default.
- `avahi_reflector`: If true, Avahi reflects mDNS across interfaces (use only if you understand the security and multicast implications).
- `allow_remote_admin`: When true and port 631 is exposed, LAN devices can reach the CUPS UI directly.


## Drivers
Preinstalled: `gutenprint`, `hplip` (HP), `brlaser` (Brother), `epson-inkjet-printer-escpr` (Epson), `ricoh-ppds` (Ricoh), `foomatic-db*`.
For Canon UFR/PPDs or other vendor packages, copy `.ppd` files into `/data/ppd` and select them when adding the printer.


## Repository packaging
```bash
# Create repo
mkdir homeassistant-addon-cups-airprint && cd $_
# copy the provided tree into this directory
git init -b main
git add .
git commit -m "feat: initial release (v0.2.0)"


git remote add origin git@github.com:<your-username>/homeassistant-addon-cups-airprint.git
git push -u origin main


# Tag and GitHub Release
git tag v0.2.0 -m "CUPS + Avahi AirPrint Bridge"
git push origin v0.2.0
```
Then create a Release in GitHub UI for tag **v0.2.0** with notes from `CHANGELOG.md`.


## Troubleshooting
- If AirPrint targets don’t show: confirm add‑on is **Started**, your HA host and iOS device are on the **same subnet/VLAN**, and no firewall blocks UDP **5353**.
- Ensure the printer queue in CUPS is **Shared**.
- For VLANs, use a network‑level mDNS reflector/relay (or enable `avahi_reflector`).


## Changelog
- **0.2.0** — Ingress support; added Brother/Canon/Epson/HP/Ricoh driver coverage via extra packages and PPD drop‑in path.
- **0.1.0** — Initial release: CUPS + Avahi with AirPrint service generation and persistent config.