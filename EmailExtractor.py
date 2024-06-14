import re

# Writing to the contacts file
with open("contacts.txt", 'w') as file:
    file.write("John Doe - john.doe@example.com\n")
    file.write("Jane Smith - jane.smith@gmail.com\n")
    file.write("For inquiries, please contact info@example.com\n")

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        # Regex pattern to match email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = set(re.findall(email_pattern, content))
        return list(emails)
    except FileNotFoundError:
        return []

def read_contact_list(filename):
    try:
        with open(filename, 'r') as file:
            email_data = []
            for line in file:
                if ' - ' in line:
                    name, emailaddress = line.strip().split(' - ')
                else:
                    # Skip lines that don't match the expected format
                    continue
                emailaddress_set = set(emailaddress.split(', '))
                email_data.append((name, emailaddress_set))
            return email_data
    except FileNotFoundError:
        return []

def analyze_unique_emailaddress(email_data):
    unique_emailaddress = set()
    for _, emailaddress in email_data:
        unique_emailaddress.update(emailaddress)
    return unique_emailaddress

def main():
    email_data = read_contact_list("contacts.txt")
    if not email_data:
        print("No email data available")
        return
    unique_emailaddress = analyze_unique_emailaddress(email_data)
    print("Unique Email Addresses:")
    for emailaddress in unique_emailaddress:
        print(emailaddress)
    
    print("\nExtracted Emails:")
    extracted_emails = extract_emails("contacts.txt")
    for email in extracted_emails:
        print(email)

if __name__ == "__main__":
    main()
