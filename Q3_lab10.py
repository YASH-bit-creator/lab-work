full_name = input("Enter full name: ")
phone_number = input("Enter phone number: ")
email = input("Enter email address: ")
org = input("Enter organization (optional): ")

# Create vCard content
vcard = f"""BEGIN:VCARD
FN:{full_name}
TEL;TYPE=CELL:{phone_number}
EMAIL:{email}
ORG:{org}
END:VCARD
"""

# Save as .vcf file
filename = full_name.replace(" ", "_") + ".vcf"
with open(filename, "w") as file:
    file.write(vcard)

print(f"vCard saved as {filename}. You can import it into your phone contacts.")
