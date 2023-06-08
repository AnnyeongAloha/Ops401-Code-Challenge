#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO:  
# Date:        TODO: 8 June 2023
# Modified by: TODO: Demo code, ChatGPT and Justin 'Sage'

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

def get_all_forms(url):
    """
    Retrieves all the HTML forms on the specified URL.

    Args:
        url (str): The URL to retrieve forms from.

    Returns:
        list: A list of BeautifulSoup objects representing the forms.
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Extracts details from a form.

    Args:
        form (BeautifulSoup): The BeautifulSoup object representing the form.

    Returns:
        dict: A dictionary containing the form details.
    """
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """
    Submits a form with the specified values.

    Args:
        form_details (dict): The details of the form.
        url (str): The URL of the form.
        value (str): The value to be submitted.

    Returns:
        requests.Response: The response of the form submission.
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Scans a URL for XSS vulnerabilities.

    Args:
        url (str): The URL to scan.

    Returns:
        bool: True if XSS vulnerability is detected, False otherwise.
    """
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerability Detected");</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))


### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
