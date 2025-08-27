# Automated Daily WhatsApp Update

This project automates sending your daily Git commits as a WhatsApp message to a manager or team member using **WhatsApp Web**, **Selenium**, and **Brave Browser**.

Once set up, you can simply run:
```bash
send
```
from anywhere in your terminal to send your daily update automatically.

## Features

- 📊 Fetches Git commits for today (or a specified date) from a given repository
- 🧹 Cleans commit messages (removes `feat:`, `fix:`, etc. prefixes)
- 📝 Formats a professional daily update message
- 📱 Sends message via WhatsApp Web using a persistent Brave automation profile
- ✅ Keeps browser open for confirmation
- 🔄 Can be scheduled to run automatically

## Repository Structure

```
update/
├── update.py          # Main Python script
├── profile/           # Brave user data folder (persistent login)
└── venv/             # Python virtual environment
```

- `profile/` will be created during setup for Brave automation
- `venv/` will be created to isolate dependencies

## Prerequisites

- Python 3.11+
- Brave Browser installed
- Git installed
- ChromeDriver (matching your Brave version)

## Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/whatsapp-daily-update.git
cd whatsapp-daily-update/update
```

### 2️⃣ Create Python Virtual Environment

```bash
python3 -m venv venv
```

**Activate it:**

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install selenium
```

### 4️⃣ Set Up Brave Automation Profile

**Create a persistent profile folder:**

**macOS / Linux:**
```bash
mkdir -p profile
```

**Windows (PowerShell):**
```powershell
mkdir profile
```

**Open Brave once to scan WhatsApp Web QR code manually:**

**macOS / Linux:**
```bash
/Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser --user-data-dir="$(pwd)/profile"
```

**Windows (PowerShell):**
```powershell
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --user-data-dir="%cd%\profile"
```

> **Important:** Scan QR code only once. After this, login will be persistent.

### 5️⃣ Configure Your Script

Open `update.py` and modify:

```python
# WhatsApp number (include country code, no +)
phone_number = "918595145323"

# Git repository path
GIT_REPO_DIR = "/path/to/your/git/repo"
```

Replace with your manager's number and the full path to your repo.

### 6️⃣ Make Script Globally Executable (`send`)

**macOS / Linux:**

1. Add shebang at the top of `update.py`:
   ```python
   #!/usr/bin/env python3
   ```

2. Rename to `send`:
   ```bash
   mv update.py send
   ```

3. Make executable:
   ```bash
   chmod +x send
   ```

4. Move to `/usr/local/bin`:
   ```bash
   sudo mv send /usr/local/bin/
   ```

Now you can run from anywhere:
```bash
send
```

**Windows:**

1. Add the following line at the top of `update.py` (optional, for clarity):
   ```python
   #!/usr/bin/env python3
   ```

2. Create a batch file `send.bat` in a folder that's in your PATH (e.g., `C:\Windows\System32`):
   ```batch
   @echo off
   python "C:\full\path\to\update.py"
   ```

Now you can run `send` from any PowerShell or CMD window.

### 7️⃣ Test the Script

Run:
```bash
send
```

- Browser will open Brave with your automation profile
- Fetch commits for today and send message via WhatsApp Web
- Browser remains open for confirmation

### 8️⃣ Optional: Schedule Daily Execution

**macOS / Linux (Cron):**

```bash
crontab -e
```

Add:
```cron
0 18 * * * /usr/local/bin/send
```
*Runs every day at 6:00 PM.*

**Windows (Task Scheduler):**

1. Create a new task
2. Action: Run `send.bat` at desired time

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Login required every time** | Make sure `profile/` folder exists and you scanned the QR code manually once |
| **No commits detected** | Ensure `GIT_REPO_DIR` points to a valid repository and that there are commits for today |
| **ChromeDriver issues** | Make sure ChromeDriver version matches your Brave browser version |
| **Permission denied** | Make sure the script has executable permissions (`chmod +x send`) |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal productivity and should be used responsibly. Make sure to comply with your organization's policies regarding automated messaging and data sharing.
