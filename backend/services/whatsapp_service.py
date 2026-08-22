import re
from datetime import datetime

# Supports Android export format:
# 12/12/25, 6:32 PM - Mom: Message

pattern = re.compile(
    r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}\s?[APMapm]{2})\s-\s([^:]+):\s(.*)"
)

def parse_whatsapp_chat(file_path):
    messages = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            match = pattern.match(line)

            if match:
                date, time, sender, message = match.groups()

                messages.append({
                    "sender": sender,
                    "timestamp": f"{date} {time}",
                    "text": message
                })
            elif messages:
                # Continue multiline message
                messages[-1]["text"] += "\n" + line

    return messages