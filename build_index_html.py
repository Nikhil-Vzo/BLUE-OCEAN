#!/usr/bin/env python3
"""
build_index_html.py
Reads template.html, injects data_bundle.json into __SAFE_BUNDLE_JSON__, and writes index.html.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BUNDLE_PATH = os.path.join(ROOT_DIR, 'data_bundle.json')
TEMPLATE_PATH = os.path.join(ROOT_DIR, 'template.html')
OUTPUT_PATH = os.path.join(ROOT_DIR, 'index.html')

if not os.path.exists(BUNDLE_PATH):
    print("Error: data_bundle.json not found! Run build_data_bundle.py first.")
    sys.exit(1)

if not os.path.exists(TEMPLATE_PATH):
    print("Error: template.html not found!")
    sys.exit(1)

with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
    bundle_json_str = f.read()

safe_bundle_json = bundle_json_str.replace('</script', '<\\/script')

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_content = f.read()

if '__SAFE_BUNDLE_JSON__' not in template_content:
    print("Error: __SAFE_BUNDLE_JSON__ placeholder not found in template.html")
    sys.exit(1)

final_html = template_content.replace('__SAFE_BUNDLE_JSON__', safe_bundle_json)

print(f"Writing index.html to {OUTPUT_PATH}...")
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(final_html)

sz = os.path.getsize(OUTPUT_PATH)
print(f"index.html successfully generated! Size: {sz:,} bytes.")
