import xml.etree.ElementTree as ET

# 1. Création de la structure XML
root = ET.Element("PaymentRequest")  # Élément racine

# Ajouter les sous-éléments
ET.SubElement(root, "PaymentID").text = "12345"
ET.SubElement(root, "Amount").text = "200.75"
ET.SubElement(root, "Currency").text = "EUR"

# Ajout des informations sur le Payer
payer = ET.SubElement(root, "Payer")
ET.SubElement(payer, "Name").text = "Alice Dupont"
ET.SubElement(payer, "Account").text = "FR7630006000011234567890189"

# Ajout des informations sur le Payee
payee = ET.SubElement(root, "Payee")
ET.SubElement(payee, "Name").text = "Bob Martin"
ET.SubElement(payee, "Account").text = "BE68539007547034"

# 2. Écriture dans un fichier
tree = ET.ElementTree(root)
with open("PaymentRequest.xml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)

print("Fichier XML créé : PaymentRequest.xml")
