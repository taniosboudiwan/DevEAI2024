import xml.etree.ElementTree as ET

# Lire et analyser le fichier XML
tree = ET.parse("PaymentRequest.xml")
root = tree.getroot()

# Extraire les informations
payment_id = root.find("PaymentID").text
amount = root.find("Amount").text
currency = root.find("Currency").text

payer_name = root.find("./Payer/Name").text
payer_account = root.find("./Payer/Account").text

payee_name = root.find("./Payee/Name").text
payee_account = root.find("./Payee/Account").text

# Afficher les informations
print("Informations extraites du fichier XML :")
print(f"ID de Paiement : {payment_id}")
print(f"Montant : {amount} {currency}")
print(f"Payer : {payer_name}, Compte : {payer_account}")
print(f"Payee : {payee_name}, Compte : {payee_account}")
