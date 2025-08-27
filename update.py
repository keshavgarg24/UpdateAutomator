#!/usr/bin/env python3
import os
import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse
from datetime import date

# -------------------------------
# Automatically activate venv
# -------------------------------
VENV_PATH = "your_venv_path"
activate_script = os.path.join(VENV_PATH, "bin", "activate_this.py")
if os.path.exists(activate_script):
    with open(activate_script) as f:
        exec(f.read(), dict(__file__=activate_script))

# -------------------------------
# Paths
# -------------------------------
BRAVE_PATH = "your_brave_path"
CHROMEDRIVER_PATH = "your_chromedriver_path"
USER_DATA_DIR = "your_user_data_dir"

# -------------------------------
# Git repository path
# -------------------------------
GIT_REPO_DIR = "your_git_repo_dir"

# -------------------------------
# Manager WhatsApp number
# -------------------------------
phone_number = "91XXXXXXXXXX"

# -------------------------------
# Date for commits
# -------------------------------
COMMIT_DATE = str(date.today())  # automatically uses today

# -------------------------------
# Function to get git commits
# -------------------------------
def get_commits_for_date(date_str):
    result = subprocess.run(
        [
            "git",
            "log",
            f"--since={date_str} 00:00",
            f"--until={date_str} 23:59",
            "--pretty=format:%s"
        ],
        capture_output=True,
        text=True,
        cwd=GIT_REPO_DIR
    )
    commits = result.stdout.strip().split("\n")
    commits = [c for c in commits if c]
    return commits

# -------------------------------
# Clean commit messages
# -------------------------------
def clean_commit(msg):
    prefixes = ["feat:", "fix:", "chore:", "docs:", "refactor:", "style:", "test:"]
    for prefix in prefixes:
        if msg.lower().startswith(prefix):
            msg = msg[len(prefix):].strip()
    if msg:
        msg = msg[0].upper() + msg[1:]
    return msg

# -------------------------------
# Prepare message
# -------------------------------
commits = get_commits_for_date(COMMIT_DATE)
commits = [clean_commit(c) for c in commits]

if not commits:
    message = f"Daily Update for {COMMIT_DATE}:\nNo commits on this day."
else:
    message = f"Daily Update for {COMMIT_DATE}:\n"
    for i, c in enumerate(commits, 1):
        message += f"{i}. {c}\n"

encoded_msg = urllib.parse.quote(message)
wa_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_msg}"

# -------------------------------
# Setup Selenium
# -------------------------------
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
options.add_argument("--profile-directory=Default")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# -------------------------------
# Open WhatsApp and send message
# -------------------------------
driver.get(wa_url)
print("⏳ Using automation profile... scan QR only the first time")

try:
    input_box = WebDriverWait(driver, 80).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    input_box.send_keys(Keys.ENTER)
    print(f"✅ Daily update for {COMMIT_DATE} sent successfully!")
except Exception as e:
    print("❌ Could not send:", e)

time.sleep(10)
# driver.quit()
