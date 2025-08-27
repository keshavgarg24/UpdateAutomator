\# Automated Daily WhatsApp Update

This project automates sending your daily Git commits as a WhatsApp message to a manager or team member using \*\*WhatsApp Web\*\*, \*\*Selenium\*\*, and \*\*Brave Browser\*\*.

Once set up, you can simply run:

\`\`\`bash

send

from anywhere in your terminal to send your daily update automatically.

Features

Fetches Git commits for today (or a specified date) from a given repository.

Cleans commit messages (feat:, fix:, etc.).

Formats a daily update message.

Sends message via WhatsApp Web using a persistent Brave automation profile.

Keeps browser open for confirmation.

Repository Structure

bash

Copy

Edit

update/

├── update.py # Main Python script

├── profile/ # Brave user data folder (persistent login)

└── venv/ # Python virtual environment

profile/ will be created during setup for Brave automation.

venv/ will be created to isolate dependencies.

Prerequisites

Python 3.11+

Brave Browser installed

Git installed

Chromedriver (matching your Brave version)

Setup Instructions

1️⃣ Clone the Repository

bash

Copy

Edit

git clone https://github.com/yourusername/whatsapp-daily-update.git

cd whatsapp-daily-update/update

2️⃣ Create Python Virtual Environment

bash

Copy

Edit

python3 -m venv venv

Activate it:

macOS / Linux

bash

Copy

Edit

source venv/bin/activate

Windows (PowerShell)

powershell

Copy

Edit

venv\\Scripts\\Activate.ps1

3️⃣ Install Dependencies

bash

Copy

Edit

pip install selenium

4️⃣ Set Up Brave Automation Profile

Create a persistent profile folder:

macOS / Linux

bash

Copy

Edit

mkdir -p profile

Windows (PowerShell)

powershell

Copy

Edit

mkdir profile

Open Brave once to scan WhatsApp Web QR code manually:

macOS / Linux

bash

Copy

Edit

/Applications/Brave\\ Browser.app/Contents/MacOS/Brave\\ Browser --user-data-dir="$(pwd)/profile"

Windows (PowerShell)

powershell

Copy

Edit

"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --user-data-dir="%cd%\\profile"

Scan QR code only once. After this, login will be persistent.

5️⃣ Configure Your Script

Open update.py and modify:

python

Copy

Edit

\# WhatsApp number (include country code, no +)

phone_number = "918595145323"

\# Git repository path

GIT_REPO_DIR = "/path/to/your/git/repo"

Replace with your manager's number and the full path to your repo.

6️⃣ Make Script Globally Executable (send)

macOS / Linux

Add shebang at the top of update.py:

python

Copy

Edit

#!/usr/bin/env python3

Rename to send:

bash

Copy

Edit

mv update.py send

Make executable:

bash

Copy

Edit

chmod +x send

Move to /usr/local/bin:

bash

Copy

Edit

sudo mv send /usr/local/bin/

Now you can run from anywhere:

bash

Copy

Edit

send

Windows

Add the following line at the top of update.py (optional, for clarity):

python

Copy

Edit

#!/usr/bin/env python3

Create a batch file send.bat in a folder that’s in your PATH (e.g., C:\\Windows\\System32):

bat

Copy

Edit

@echo off

python "C:\\full\\path\\to\\update.py"

Now you can run send from any PowerShell or CMD window.

7️⃣ Test the Script

Run:

bash

Copy

Edit

send

Browser will open Brave with your automation profile.

Fetch commits for today and send message via WhatsApp Web.

Browser remains open for confirmation.

8️⃣ Optional: Schedule Daily Execution

macOS / Linux (Cron)

bash

Copy

Edit

crontab -e

Add:

cron

Copy

Edit

0 18 \* \* \* /usr/local/bin/send

Runs every day at 6:00 PM.

Windows (Task Scheduler)

Create a new task.

Action: Run send.bat at desired time.

Troubleshooting

Login required every time: Make sure profile/ folder exists and you scanned the QR code manually once.

No commits detected: Ensure GIT_REPO_DIR points to a valid repository and that there are commits for today.
