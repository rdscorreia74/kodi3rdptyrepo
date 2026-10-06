import os
import hashlib

def generate_repo():
    addons_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
    
    # Loop through subdirectories to find addon.xml files
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "addon.xml" and root != ".":
                xml_path = os.path.join(root, file)
                with open(xml_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    # Skip XML declaration header if present in individual addon.xml
                    for line in lines:
                        if not line.strip().startswith("<?xml"):
                            addons_xml += line
                addons_xml += "\n"
                
    addons_xml += "</addons>\n"
    
    # Save addons.xml
    with open("addons.xml", "w", encoding="utf-8") as f:
        f.write(addons_xml)
    print("Created addons.xml")

    # Generate MD5 hash
    md5_hash = hashlib.md5(addons_xml.encode("utf-8")).hexdigest()
    with open("addons.xml.md5", "w", encoding="utf-8") as f:
        f.write(md5_hash)
    print("Created addons.xml.md5")

if __name__ == "__main__":
    generate_repo()
